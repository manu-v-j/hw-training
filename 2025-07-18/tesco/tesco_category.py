import requests
from parsel import Selector
from settings import base_url,headers,MONGO_URL,MONGO_DB,CATEGORY_COLLECTION
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

class Category:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[CATEGORY_COLLECTION]

    def start(self):
        response=requests.get(base_url,headers=headers)
        if response.status_code==200:
            self.parse_item(response)
    
    def parse_item(self,response):
        sel=Selector(text=response.text)
        category_urls=sel.xpath("//a[contains(@class,'styled__RoundelWrapper-sc-1imrqlh-1 fAVFEp ddsweb-link')]/@href").getall()
        for url in category_urls:
            if url=='https://www.tesco.com/groceries/en-GB':
                continue
            self.collection.insert_one({'link':url})
            logging.info(url)

if __name__=='__main__':
    category=Category()
    category.start()

