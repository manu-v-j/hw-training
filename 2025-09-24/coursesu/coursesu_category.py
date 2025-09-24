import requests
from parsel import Selector
from settings import headers,base_url,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY
from pymongo import MongoClient

class Category:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_CATEGORY]

    def start(self):
        response=requests.get(base_url,headers=headers)
        
        if response.status_code==200:
            self.parse_item(response)

    def parse_item(self,response):
        sel=Selector(text=response.text)
        category_urls=sel.xpath("//a[@class='ab-prehome-category-link']/@href").getall()
        for url in category_urls:
            self.collection.insert_one({'link':url})
            print(url)

if __name__=='__main__':
    category=Category()
    category.start()

