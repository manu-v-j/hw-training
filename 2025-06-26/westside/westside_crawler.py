import requests
from parsel import Selector
from settings import base_url,headers,MONGO_URI,MONGO_DB,COLLECTION,COLLECTION_CATEGORY
import json
import re
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]

    def start(self):
        for item in self.db[COLLECTION_CATEGORY].find():
            base_url=item.get('link','')
            response=requests.get(base_url,headers=headers)
            self.parse_item(response)

    def parse_item(self,response):
        sel=Selector(text=response.text)
        script_text=sel.xpath("//script[contains(text(), 'var meta')]/text()").get()
        match = re.search(r'var\s+meta\s*=\s*({.*?});', script_text, re.DOTALL)
        if match:
            json_text = match.group(1)
            data = json.loads(json_text)
            products_list=data.get("products",[])
            for product in products_list:
                varient_list=product.get("variants",[])
                item=varient_list[0]
                id=item.get('id','')
                name_raw=item.get('name','')
                sku_raw=item.get('sku','')
                sku=sku_raw.replace('001','')
                name=re.sub(r'\-\s*\w*\s*\/\s*\w*|&','',name_raw)
                name=re.sub(r'\s+','-',name.strip().lower())
                url = f"https://www.westside.com/products/{name}-{sku}?variant={id}"
                item={}
                item['link']=url
                self.collection.insert_one(item)
                logging.info(item)

if __name__=='__main__':
    crawler=Crawler()
    crawler.start()