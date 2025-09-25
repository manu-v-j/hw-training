import requests
import logging
from parsel import Selector
import json,re
from pymongo import MongoClient
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_DETAILS,COLLECTION_ERROR
from coursesu_item import Product_Item

logging.basicConfig(level=logging.INFO)

class Parser:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_DETAILS]
        self.collection_error=self.db[COLLECTION_ERROR]

    def start(self):
        for item in self.db[COLLECTION].find():
            base_url=item.get('link')
            response=requests.get(base_url,headers=headers)

            if response.status_code==200:
                self.parse_item(response,base_url)
            else:
                self.collection_error.insert_one({'link':base_url})

    def parse_item(self,response,base_url):
        sel=Selector(text=response.text)

        #XPATH
        SCRIPT_XAPTH="//script[@type='application/ld+json']/text()"
        RATING_XPATH="//span[contains(@class,'bv-rating-stars-container')]/@aria-label"
        REVIEW_XPATH="//span[contains(@class,'review-link')]/text()"
        NETWEIGHT_XPATH="//p[@class='pdp-description-text' and contains(text(), 'Poids net')]/text()"
        LEGAL_NAME_XPATH="//p[@class='pdp-description-text' and contains(text(), 'Dénomination légale')]/text()"
        INGREDIENTS_XPATH="//h3[text()='Ingrédients']/parent::li/following-sibling::li//p[2]/text()"
        STORAGE_XPATH="//h3[text()='Instruction de conservation']/parent::li/following-sibling::li/p/text()"
        BREADCRUMB_XPATH="//ol[contains(@class,'breadcrumb')]/li//a//text()"
        ORIGIN_XPATH="//h3[text()='Origine']/parent::li/following-sibling::li/p/text()"


        #EXTRACT
        script=sel.xpath(SCRIPT_XAPTH).get()
        rating=sel.xpath(RATING_XPATH).get()
        review=sel.xpath(REVIEW_XPATH).get()
        netweight_raw=sel.xpath(NETWEIGHT_XPATH).get()
        legal_name_raw=sel.xpath(LEGAL_NAME_XPATH).get()
        ingredients=sel.xpath(INGREDIENTS_XPATH).get()
        storage_instructions=sel.xpath(STORAGE_XPATH).get()
        breadcrumb_raw=sel.xpath(BREADCRUMB_XPATH).getall()
        country_of_origin=sel.xpath(ORIGIN_XPATH).get()

        #CLEAN

        if script:
            data = json.loads(script)
            product_name=data.get('name','')
            unique_id=data.get('mpn','')
            image_url=data.get('image',[])

        netweight=''
        if netweight_raw:
            netweight=netweight_raw.replace('Poids net: ','')    
        grammage_quantity=''
        grammage_unit=''
        if netweight:
            match = re.search(r'([\d.,]+)\s*([a-zA-Z]+)', netweight)
            grammage_quantity = match.group(1)   
            grammage_unit = match.group(2) 

        legal_name=''
        if legal_name_raw:
            legal_name = re.sub(r"\s+", " ", legal_name_raw).strip()
            legal_name = legal_name.replace("Dénomination légale : ", "")

        breadcrumb=' > '.join([item.strip() for item in breadcrumb_raw if item.strip()])

        item={}
        item['product_name']=product_name
        item['unique_id']=unique_id
        item['grammage_quantity']=grammage_quantity
        item['grammage_unit']=grammage_unit
        item['pdp_url']=base_url
        item['rating']=rating
        item['review']=review
        item['netweight']=netweight
        item['country_of_origin']=country_of_origin
        item['breadcrumb']=breadcrumb
        item['legal_name']=legal_name
        item['ingredients']=ingredients
        item['storage_instructions']=storage_instructions
        item['image_url']=image_url

        product_item=Product_Item(**item)
        product_item.save()

        logging.info(item)

if __name__=='__main__':
    parser=Parser()
    parser.start()