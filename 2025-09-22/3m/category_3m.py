import requests
from parsel import Selector
from pymongo import MongoClient
import logging
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY

logging.basicConfig(level=logging.INFO)
class Category:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_CATEGORY]

    def start(self):
        response = requests.get('https://www.3m.com/', headers=headers)
        if response.status_code==200:
            self.parse_item(response)

    def parse_item(self,response):
        sel=Selector(text=response.text)
        category_urls=sel.xpath("//ul[@id='products-list']//li/a/@href").getall()
        for url in category_urls:
            id=url.split('en_US',1)[1]
            full_url=f"https://www.3m.com{url}"

            item={}
            item['id']=id
            item['link']=full_url
            self.collection.insert_one(item)

if __name__=='__main__':
    category=Category()
    category.start()