import requests 
from parsel import Selector
from settings import headers,base_url,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

class Category:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_CATEGORY]

    def start(self):
        response=requests.get(base_url,headers=headers,verify=False)
        sel=Selector(text=response.text)
        category_urls=sel.xpath("//article[contains(@class,'CategoryLeafstyles__Wrapper-sc-2bwko3-0')]/a/@href").getall()
        for category in category_urls:
            full_url=f'https://www.lego.com{category}'
            self.collection.insert_one({'link':full_url})

            logging.info(full_url)

if __name__=='__main__':
    category=Category()
    category.start()