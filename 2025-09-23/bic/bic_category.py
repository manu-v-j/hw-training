import requests
from parsel import Selector
from pymongo import MongoClient
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY

class Category:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_CATEGORY]

    def start(self):
        response=requests.get('https://eu.bic.com/en-gb',headers=headers)
        if response.status_code==200:
            self.parse_item(response)

    def parse_item(self,response):
        sel=Selector(text=response.text)
        product_urls=sel.xpath("//div[@class='final-links']/a/@href").getall()
        for url in product_urls:
            full_url=f"https://eu.bic.com{url}"

            self.collection.insert_one({'link':full_url})
if __name__=='__main__':
    category=Category()
    category.start()