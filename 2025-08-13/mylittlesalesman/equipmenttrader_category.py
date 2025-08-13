import requests
from settings import headers,base_url,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY
from parsel import Selector
import logging
from pymongo import MongoClient
logging.basicConfig(level=logging.INFO)

class Category:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_CATEGORY]

    def start(self):
        response=requests.get(base_url,headers=headers)
        sel=Selector(text=response.text)
        category_urls=sel.xpath("//span[contains(text(),'For Rent') or contains(text(),'For Sale')]/following-sibling::div//li/a/@href").getall()
        for link in category_urls:
            full_url=f"https://www.mylittlesalesman.com{link}"
            self.collection.insert_one({'link':full_url})

if __name__=='__main__':
    category=Category()
    category.start()