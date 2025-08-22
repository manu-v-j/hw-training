import requests
from parsel import Selector
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_ERROR
import logging,json,re
logging.basicConfig(level=logging.INFO)
from pymongo import MongoClient
from aldi_items import Product_Item

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]

    def start(self):
        for item in self.db[COLLECTION].find():
            url = item.get('link')
            response=requests.get(url,headers=headers)
            if response.status_code==200:
                self.parse_item(response)
            
    def parse_item(self,response):
        sel=Selector(text=response.text)

        #XPATH
        SCRIPT_XPATH="//script[@ type='application/ld+json'][2]/text()"
        GRAMMAGE_RAW_XPATH="//span[@class='product-details__unit-of-measurement']/text()"
        COUNTRY_XPATH="//div[@class='base-accordion-item__content-inner']/text()"
        BREADCRUMB_XPATH="//a[@class='base-link base-breadcrumbs__crumb']/text()"

        #EXTRACT
        script_text=sel.xpath(SCRIPT_XPATH).get()
        grammage_raw=sel.xpath(GRAMMAGE_RAW_XPATH).get()
        country_of_origin=sel.xpath(COUNTRY_XPATH).get()
        breadcrumb=sel.xpath(BREADCRUMB_XPATH).getall()

        #CLEAN
        data=json.loads(script_text)
        product_id=data.get('productID','')
        product_name=data.get('name','')
        brand=data.get('brand',{}).get('name','')
        selling_price=data.get('offers',{}).get('price','')
        regular_price=''
        currency=data.get('offers',{}).get('priceCurrency','')
        product_description=data.get('description','')
        image_url=data.get('image',[])
        grammage_quantity = ''
        grammage_unit = ''

        if grammage_raw:
            match = re.search(r'\d+', grammage_raw)
            if match:
                grammage_quantity = match.group()

            grammage_unit = grammage_raw.replace(grammage_quantity or '', '').strip()
        breadcrumb=' > '.join(breadcrumb)

        item={}
        item['product_id']=product_id
        item['product_name']=product_name
        item['brand']=brand
        item['grammage_quantity']=grammage_quantity
        item['grammage_unit']=grammage_unit
        item['selling_price']=selling_price
        item['regualar_price']=selling_price
        item['currency']=currency
        item['breadcrumb']=breadcrumb
        item['country_of_origin']=country_of_origin
        item['product_description']=product_description
        item['image_url']=image_url

        product_item=Product_Item(**item)
        product_item.save()

        logging.info(item)

if __name__=='__main__':
    parser=Parser()
    parser.start()
