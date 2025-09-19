import requests
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_DETAILS
from  portwest_item import Product_Item
from pymongo import MongoClient
from parsel import Selector
import re
import logging 
logging.basicConfig(level=logging.INFO)

class Parser:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_DETAILS]

    def start(self):
        for item in self.db[COLLECTION].find().limit(1000):
            base_url=item.get('link')
            response=requests.get(base_url,headers=headers)
            sel=Selector(text=response.text)

            #XPATH
            PRODUCT_NAME_XAPTH="//div[@class='col-lg-6']/div/h2/text()"
            SIZE_XPATH="//div[@class='std_titles']/text()"
            COLOUR_XPATH="//div[@class='ratings-container']/h2/text()"
            PRODUCT_DESCRIPTION_XPATH="//p[@class='text-justify']/text()"
            FEATURES_XPATH="//h3[text()='Features']/following-sibling::li/text()"
            IMAGES_XPATH="//img[@class='product-single-image']/@src"
            DATASHEETS_XPATH="//a[text()='Datasheets']/@href"
            DECLARATION_CONFORMITY_EU_XAPTH="//a[text()='Declaration of Conformity (EU)']/@href"
            DECLARATION_CONFORMITY_UK_XAPTH="//a[text()='Declaration of Conformity (UK)']/@href"
            SIZING_XPATH="//a[text()='Sizing Chart']/@href"
            MATERIAL_XPATH="//div[@style='display: inline-block;']/text()"

            #EXTRACT
            product_name_raw=sel.xpath(PRODUCT_NAME_XAPTH).getall()
            size=sel.xpath(SIZE_XPATH).get()
            colour_raw=sel.xpath(COLOUR_XPATH).getall()
            product_description=sel.xpath(PRODUCT_DESCRIPTION_XPATH).get()
            features_raw=sel.xpath(FEATURES_XPATH).getall()
            material_raw=sel.xpath(MATERIAL_XPATH).getall()
            images=sel.xpath(IMAGES_XPATH).get()
            datasheets=sel.xpath(DATASHEETS_XPATH).get()
            declaration_conformity_eu=sel.xpath(DECLARATION_CONFORMITY_EU_XAPTH).get()
            declaration_conformity_uk=sel.xpath(DECLARATION_CONFORMITY_UK_XAPTH).get()
            sizing_chart=sel.xpath(SIZING_XPATH).get()

            #CLEAN
            if size:
                size=size.strip()
            features=' '.join(features_raw)
            material =' '.join([re.sub(r"\s+", " ", m).strip() for m in material_raw])
            colour =' '.join([re.sub(r"\s+", " ", m).strip() for m in colour_raw])
            product_name =' '.join([re.sub(r"\s+", " ", m).strip() for m in product_name_raw])

            item={}
            item['product_name']=product_name
            item['size']=size
            item['colour']=colour
            item['product_description']=product_description
            item['features']=features
            item['material']=material
            item['pdp_url']=base_url
            item['images']=images
            item['datasheets']=datasheets
            item['declaration_conformity_eu']=declaration_conformity_eu
            item['declaration_conformity_uk']=declaration_conformity_uk
            item['sizing_chart']=sizing_chart

            logging.info(item)

            product_item=Product_Item(**item)
            product_item.save()

if __name__=='__main__':
    parser=Parser()
    parser.start()