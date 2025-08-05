import requests
from parsel import Selector
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION
from lego_items import Product_Item
import json
import re
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]

    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get('link')
            response=requests.get(url,headers=headers,verify=False)
            if response.status_code==200:
                self.parse_item(response,url)
    def parse_item(self,response,url):
        sel=Selector(text=response.text)

        #XPATH
        PRODUCT_NAME_XPATH="//h1[contains(@class,'ProductOverviewstyles__NameText-sc-1wfukzv-5')]/span/text()"
        SELLING_PRICE_XPATH_RAW="//span[@data-test='product-price-sale']/text()"
        REGULAR_PRICE_XPATH_RAW="//span[@data-test='product-price']/text()"
        IMAGE_URL_XAPTH_RAW="//picture[@class='ProductGallery_styledPicture__wQV8N']/source/@srcset"
        AVAILABILTY_XPATH="//span[@class='ds-body-md-medium']/text()"
        SCRIPT_XPATH="//script[@id='__NEXT_DATA__']/text()"

        #EXTRACT
        product_name=sel.xpath(PRODUCT_NAME_XPATH).get()
        selling_price_raw=sel.xpath(SELLING_PRICE_XPATH_RAW).get()
        regular_price_raw=sel.xpath(REGULAR_PRICE_XPATH_RAW).get()
        image_url_raw=sel.xpath(IMAGE_URL_XAPTH_RAW).get()
        availability=sel.xpath(AVAILABILTY_XPATH).get()
        script=sel.xpath(SCRIPT_XPATH).get()

        #CLEAN
        selling_price=''
        regular_price=''
        if selling_price_raw:
            selling_price=selling_price_raw.replace('£','')
        if regular_price_raw:
            regular_price=regular_price_raw.replace('£','')
            
        data = json.loads(script)
        details=data.get('props',{}).get('pageProps',{}).get('__APOLLO_STATE__',{})
        single_variant_keys = [key for key in details.keys() if key.startswith('SingleVariantProduct:')]
        key=single_variant_keys[0] 
        product_details=data.get('props',{}).get('pageProps',{}).get('__APOLLO_STATE__',{}).get(f'{key}',{})

        unique_id=product_details.get('productCode','')
        id=product_details.get('variant',{}).get('id','')
        match = re.search(r'\d+', id)
        if match:
            id=match.group()
        product_description=product_details.get('featuresText','')
        if product_description:
            product_description=product_description.strip()
        desc_selector = Selector(text=product_description)
        product_description = " ".join(desc_selector.xpath("//p/text() | //li/text()").getall()).strip()
        product_attribute=data.get('props',{}).get('pageProps',{}).get('__APOLLO_STATE__',{}).get(f'ProductVariant:{id}',{})
        features_script=data.get('props',{}).get('pageProps',{}).get('__APOLLO_STATE__',{}).get(f'$ProductVariant:{id}.attributes',{})
        feature={}
        feature['age'] = features_script.get('ageRange', '')
        feature['pieces'] = features_script.get('pieceCount', '')
        feature['points'] = product_attribute.get('vipPoints', '')
        feature['items']=unique_id
        
        urls = re.findall(r'https://[^\s,]+', image_url_raw)
        image_url=urls[-1]

        item={
            'unique_id':unique_id,
            'competitor_name':'lego',
            'product_name':product_name,
            'brand':'lego',
            'selling_price':selling_price,
            'regular_price':regular_price,
            'percentage_discount':'',
            'pdp_url':url,
            'features':feature,
            'color':'',
            'product_description':product_description,
            'availability':availability,
            'image':image_url

        }

        product_item=Product_Item(**item)
        product_item.save()

        logging.info(product_description)

if __name__=='__main__':
    parser=Parser()
    parser.start()