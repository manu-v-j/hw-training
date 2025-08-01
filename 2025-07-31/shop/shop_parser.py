from curl_cffi import requests
from parsel import Selector
from pymongo import MongoClient
import json
import re
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION
from shop_items import Product_Item
import logging
logging.basicConfig(level=logging.INFO)

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        

    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get('link')
            response=requests.get(url,headers=headers,impersonate='chrome')
            if response.status_code==200:
                self.parse_item(response,url)

    def parse_item(self,response,url):
        sel=Selector(text=response.text)

        #XPATH
        UNIQUE_ID="//div[@class='pdpr-ArticleNumber']/text() "
        PRODUCT_NAME_XAPTH="//h1[@class='pdpr-Title']/text()"
        BRAND_XPATH="//span[contains(@class,'pdpr-Brand__Link__Content')]/span/text()"
        COUNTRY_OF_ORIGIN_XPATH="//h3[contains(text(),'Ursprungsland')]/following-sibling::text() | //h3[contains(text(),'Ursprung')]/following-sibling::text()"
        SELLING_PRICE_XPATH="//meso-data[@data-price]/@data-price"
        PRODUCT_DESCRIPTION_XPATH="//div[@class='pdpr-ArticleNumber']/text() | //div[@class='pdpr-ProductContent__Content']//text()"
        BREADCRUMB_XPATH="//a[contains(@class,'lr-breadcrumbs__link')]//text()"
        INGREDIENTS_XPATH="//h3[contains(text(),'Zutaten')]/following-sibling:: text()"
        ROWS_XPATH="//table[contains(@class,'pdpr-NutritionTable')]//tbody/tr"
        STORAGE_INSTRUCTIONS_XPATH="//h3[contains(text(),'Aufbewahrungshinweise')]/following-sibling:: text()"
        SCRIPT_XPATH="//script[@type='application/ld+json']/text()"

        #CLEAN
        unique_id_raw=sel.xpath(UNIQUE_ID).get()
        product_name=sel.xpath(PRODUCT_NAME_XAPTH).get()
        brand=sel.xpath(BRAND_XPATH).get()
        country_of_origin=sel.xpath(COUNTRY_OF_ORIGIN_XPATH).get()
        selling_price_raw=sel.xpath(SELLING_PRICE_XPATH).get()
        product_description=sel.xpath(PRODUCT_DESCRIPTION_XPATH).getall()
        breadcrumb=sel.xpath(BREADCRUMB_XPATH).getall()
        ingredients=sel.xpath(INGREDIENTS_XPATH).get()
        rows=sel.xpath(ROWS_XPATH)
        storage_instructions=sel.xpath(STORAGE_INSTRUCTIONS_XPATH).get()
        script=sel.xpath(SCRIPT_XPATH).get()

        #CLEAN
        unique_id=unique_id_raw.replace('Artikelnummer ','')
        match = re.search(r"(\d+)\s*(g|kg|ml|l)", product_name.lower())
        grammage_quantity=''
        grammage_unit=''
        if match:
            grammage_quantity = match.group(1)
            grammage_unit = match.group(2)
        selling_price=selling_price_raw.replace('€','')
        breadcrumb='>'.join([item.strip() for item in breadcrumb])
        product_description=','.join(product_description)
        nutritions={}
        for row in rows:
            key = (row.xpath("./td[1]/text()").get() or "").strip()
            value = (row.xpath("./td[2]/text()").get() or "").strip()
            nutritions[key] = value
        data=json.loads(script)
        image_url=data.get('image','')

        item={}
        item['unique_id']=unique_id
        item['product_name']=product_name
        item['brand']=brand
        item['grammage_quantity']=grammage_quantity
        item['grammage_unit']=grammage_unit
        item['pdp_url']=url
        item['selling_price']=selling_price
        item['currency']='Euro'
        item['country_of_origin']=country_of_origin
        item['product_description']=product_description
        item['breadcrumb']=breadcrumb
        item['ingredients']=ingredients
        item['nutritions']=nutritions
        item['storage_instructions']=storage_instructions
        item['image_url']=image_url

        product_item=Product_Item(**item)
        product_item.save()
        logging.info(item)


if __name__=='__main__':
    parser=Parser()
    parser.start()