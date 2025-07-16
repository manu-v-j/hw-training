import requests
from parsel import Selector
from settings import headers,base_url,MONGO_URI,MONGO_DB,COLLECTION_CATEGORY
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

class Category:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_CATEGORY]
        self.collection.create_index('link',unique=True)

    def start(self):
        response=requests.get(base_url,headers=headers)
        if response.status_code==200:
            self.parse_item(response)

    def parse_item(self,response):
        sel=Selector(text=response.text)
        category_urls=sel.xpath("//a[@class='left cat-duplicateLink']/@href").getall()
        category_id =sel.xpath("//a[@class='left cat-duplicateLink']/@tw-cat-id").getall()
        for url,id in zip(category_urls,category_id):
            item={}
            item['link']=url
            item['id']=id
            self.collection.insert_one(item)

            logging.info(url)

if __name__=='__main__':
    category=Category()
    category.start()

