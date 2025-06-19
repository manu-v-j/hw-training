import requests
from parsel import Selector
from settings import headers,MONGO_URI,DB_NAME,COLLECTION,COLLEC_DETAILS
from pymongo import MongoClient
import re

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[DB_NAME]
        self.collection=self.db[COLLEC_DETAILS]

    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get('link')
            response=requests.get(url,headers=headers)
            if response.status_code==200:
                self.parse_item(response)

    def parse_item(self,response):
        sel=Selector(text=response.text)
        product_name=sel.xpath("//div[contains(@class,'product-name')]/h1/text()").get()
        grammage_quantity_match=re.search(r'\d+x\d+',product_name) 
        grammage_quantity = grammage_quantity_match.group() if grammage_quantity_match else ""

        # grammage_unit=re.search(r'(kg|g|ml|l)',product_name).group()
        # price_raw=sel.xpath("//div[@class='product-price']/span/text()").get()
        # regular_price=re.search("AED",price_raw).group()
        # currency=re.search(r'\d+\.\d+',price_raw).group()
        # product_decsription=sel.xpath("//div[@class='full-description']/text()").get()
        # image_url=sel.xpath("//div[@class='picture']/img/@src").get()
        print(grammage_quantity)


if __name__=='__main__':
    parser=Parser()
    parser.start()