from curl_cffi import requests
from parsel import Selector
from pymongo import MongoClient
from settings import headers,base_url,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY

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
        category_urls=sel.xpath("//a[contains(@class,'horizontal-menu-link--secondary')]/@href").getall()
        for url in category_urls:
            full_url=f"https://www.decathlon.de{url}"

            self.collection.insert_one({'link':full_url})

if __name__=='__main__':
    category=Category()
    category.start()