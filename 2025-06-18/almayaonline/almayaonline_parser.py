import requests
from parsel import Selector
from settings import headers,MONGO_URI,DB_NAME,COLLECTION,COLLECTION_DETAILS
from pymongo import MongoClient
import re
import logging
from almayaonline_items import ProductItem
logging.basicConfig(level=logging.INFO)

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[DB_NAME]
        self.collection=self.db[COLLECTION_DETAILS]

    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get('link')
            response=requests.get(url,headers=headers)
            if response.status_code==200:
                self.parse_item(response,url)

    def parse_item(self,response,url):
        sel=Selector(text=response.text)
        # XPATH
        product_name_xpath="//div[contains(@class,'product-name')]/h1/text()"
        price_raw_xpath="//div[@class='product-price']/span/text()"
        product_decsription_xpath="//div[@class='full-description']/text()"
        image_url_xpath="//div[@class='picture']/img/@src"

        product_name=sel.xpath(product_name_xpath).get()
        price_raw=sel.xpath(price_raw_xpath).get()
        if not price_raw:
            logging.warning(f"Price not found for URL: {url}")
            return
        product_decsription=sel.xpath(product_decsription_xpath).get()
        currency=re.search("AED",price_raw).group()
        regular_price=price_raw.replace('AED','').strip()
        image_url=sel.xpath(image_url_xpath).get()


        # CLEAN
        grammage_quantity_match=re.search(r'\d+\s*[xX]\s*\d+|\d+',product_name) 
        grammage_quantity = grammage_quantity_match.group() if grammage_quantity_match else ""
        grammage_unit_match=re.search(r'(kg|gm|ml)',product_name)
        grammage_unit=grammage_unit_match.group() if grammage_unit_match else ""

        # ITEM YEILD
        item={}
        item['url']=url
        item['product_name']=product_name
        item['grammage_quantity']=grammage_quantity
        item['grammage_unit']=grammage_unit
        item['product_decsription']=product_decsription
        item['currency']=currency
        item['regular_price']=regular_price
        item['image_url']=image_url

        product_item=ProductItem(**item)
        product_item.save()

        logging.info(item)

if __name__=='__main__':
    parser=Parser()
    parser.start()