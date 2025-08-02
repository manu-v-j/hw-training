import requests
from parsel import Selector
from settings import headers,MONGO_URI,DB_NAME,CATEGORY,url
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

class Category:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[DB_NAME]
        self.collection=self.db[CATEGORY]

    def start(self):
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            self.parse_item(response)
        
    def parse_item(self,response):
        sel=Selector(text=response.text)
        category_url=sel.xpath("//li[@class='all-categories']/ul/li/a/@href").getall()
        for category in category_url:
            full_url=f"https://www.almayaonline.com{category}"

            item={}
            item['link']=full_url
            logging.info(item)
            self.collection.insert_one(item)


if __name__=='__main__':
    category=Category()
    category.start()
