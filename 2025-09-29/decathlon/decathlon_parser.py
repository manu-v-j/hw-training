from curl_cffi import requests
from parsel import Selector
from json import loads
from pymongo import MongoClient
import logging
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_ERROR
from decathlon_item import Product_Item
logging.basicConfig(level=logging.INFO)

class Parser:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_ERROR]

    def start(self):
        for item in self.db[COLLECTION].find().limit(200):
            base_url=item.get('link')
            response=requests.get(base_url,headers=headers,impersonate='chrome')

            if response.status_code==200:
                self.parse_item(response,base_url)
            else:
                self.collection.insert_one({'link':base_url})

    def parse_item(self,response,base_url):
        sel=Selector(text=response.text)

        #XPATH
        UNIQUE_XPATH="//div[@class='product-info__product-id']/span/text()"
        SCRIPT_XPATH="//script[@type='application/ld+json']/text()"
        SELLING_PRICE_XPATH="//span[contains(@class,'price-base__current-price')]/text()"
        REGULAR_PRICE_XPATH="//span[contains(@class,'price-base__previous-price')]/text()"
        BREADCRUMB_XPATH="//a[@class='breadcrumb-item']/span/text()"
        COLOR_XPATH="//div[@class='variant-selector-headline__value']/span/text()"
        SIZE_XPATH="//label[@class='variant-tile-radio__label']/span/text()"
        WARRANTY_XPATH="//span[contains(text(),'Garantie')]/text()"
        CARE_INSTRUCTIONS_XPATH="//h3[contains(@class,'care-instructions__title ')]/following-sibling::div//text()"
        MATERIAL_XPATH="//p[@class='specifications__item vp-body-s']/text()"
        PROMOTION_XPATH="//span[@class='price-base__commercial-message']/text()"

        #EXTRACT
        unique_id_raw=sel.xpath(UNIQUE_XPATH).getall()
        script=sel.xpath(SCRIPT_XPATH).get()
        data=loads(script)

        product_name=data.get('name','')
        brand=data.get('brand',{}).get('name','')
        product_description=data.get('description','')
        rating_raw=data.get('aggregateRating',{}).get('ratingValue','')
        review_raw=data.get('aggregateRating',{}).get('reviewCount','')
        image_url=data.get('image','')

        selling_price_raw=sel.xpath(SELLING_PRICE_XPATH).get()
        regular_price_raw=sel.xpath(REGULAR_PRICE_XPATH).get()
        breadcrumb_raw=sel.xpath(BREADCRUMB_XPATH).getall()
        color=sel.xpath(COLOR_XPATH).get()
        size_raw=sel.xpath(SIZE_XPATH).getall()
        warranty_raw=sel.xpath(WARRANTY_XPATH).get()
        care_instructions_raw=sel.xpath(CARE_INSTRUCTIONS_XPATH).getall()
        material_composition=sel.xpath(MATERIAL_XPATH).get()
        promotion_description=sel.xpath(PROMOTION_XPATH).get()

        #CLEAN
        unique_id = ''.join(item.strip() for item in unique_id_raw if item.strip() != 'ID')

        if selling_price_raw:
            selling_price=selling_price_raw.replace('€','').replace(',','.')

        if regular_price_raw:
            regular_price=regular_price_raw.replace('€','').replace(',','.')
        else:
            regular_price=selling_price

        breadcrumb=' > '.join([item.strip() for item in breadcrumb_raw if item.strip()])

        warranty=''
        if warranty_raw:
            warranty=warranty_raw.replace(' Jahr(e) Garantie','')

        size=''
        if size_raw:
            size=','.join(size_raw)

        care_instructions=''
        if care_instructions_raw:
            care_instructions=' '.join([item.strip() for item in care_instructions_raw if item.strip()])

        rating=str(rating_raw) if rating_raw else ''
        review=str(review_raw) if review_raw else ''

        item={}
        item['unique_id']=unique_id
        item['product_name']=product_name
        item['brand']=brand
        item['selling_price']=selling_price
        item['regular_price']=regular_price
        item['currency']='EUR'
        item['pdp_url']=base_url
        item['product_description']=product_description
        item['rating']=rating
        item['review']=review
        item['breadcrumb']=breadcrumb
        item['color']=color
        item['size']=size
        item['warranty']=warranty
        item['promotion_description']=promotion_description
        item['care_instructions']=care_instructions
        item['material_composition']=material_composition
        item['image_url']=image_url

        product_item=Product_Item(**item)
        product_item.save()

        logging.info(item)

if __name__=='__main__':
    parser=Parser()
    parser.start()
