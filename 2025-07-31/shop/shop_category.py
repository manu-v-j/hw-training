from curl_cffi import requests
from parsel import Selector
from settings import headers,base_url,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY
from pymongo import MongoClient
import re
import logging
logging.basicConfig(level=logging.INFO)

class Category:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_CATEGORY]

    def start(self):
        response=requests.get(base_url,headers=headers,impersonate='chrome')
        if response.status_code==200:
            self.parse_item(response)

    def parse_item(self,response):
        sel=Selector(text=response.text)
        urls = re.findall(r"piShopUrl\('(.*?)'\)", response.text)
        urls=urls[0:22]
        for url in urls:
            full_url=f'https://shop.rewe.de{url}'
            self.collection.insert_one({'link':full_url})

            logging.info(full_url)

if __name__=='__main__':
    category=Category()
    category.start()