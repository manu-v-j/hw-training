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

    def start(self):
        response=requests.get(base_url,headers=headers)
        if response.status_code==200:
            self.parse_item(response)

    def parse_item(self,response):
        sel=Selector(text=response.text)
        category_links=sel.xpath("//a[@class='dropdown__menulink js-menu-link-inside-dropdown']/@href").getall()
        for link in category_links:
            category_link=f"https://styleunion.in{link}"
            logging.info(category_link)
            item={}
            item['link']=category_link
            
            self.collection.insert_one(item)

if __name__=='__main__':
    category=Category()
    category.start()