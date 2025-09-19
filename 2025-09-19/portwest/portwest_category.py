import requests
from parsel import Selector
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY
from pymongo import MongoClient,errors
import logging
logging.basicConfig(level=logging.INFO)

class Category:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_CATEGORY]
        self.collection.create_index("id", unique=True)
        self.collection.create_index("link", unique=True)

    def start(self):
        response = requests.get('https://www.portwest.com/market/', headers=headers)
        if response.status_code==200:
            self.parse_item(response)
    
    def parse_item(self,response):
        sel=Selector(text=response.text)
        category_urls=sel.xpath("//div[@class='menu-title']/a/@href").getall()
        for url in category_urls:
            try:
                id=url.split('X',1)[1]
                category_id="X" + id
                item={}
                item['id']=category_id
                item['link']=url
                self.collection.insert_one(item)
                
            except errors.DuplicateKeyError:
                logging.info(f"Duplicate: {id}")   

            
            logging.info(item)

if __name__=='__main__':
    category=Category()
    category.start()
