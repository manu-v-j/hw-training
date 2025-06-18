import requests
from parsel import Selector
from settings import *
from pymongo import MongoClient

class Crawler:

    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[DB_NAME]
        self.collection=self.db[COLLECTION]

    def start(self):
        
        while True:
            response = requests.get(BASE_URL, headers=headers)
            next_url=self.parse_item(response,BASE_URL)
            BASE_URL=next_url            

    def parse_item(self,response):
        sel = Selector(text=response.text)

        product_urls = sel.xpath("//a[contains(@class, 'grid-product__link')]/@href").getall()
        for product_url in product_urls:
            full_url = f"https://noragardner.com{product_url}"
            
            self.collection.insert_one({'link':full_url})
            

        pagination = sel.xpath("//link[@rel='next']/@href").get()
        if pagination:
            next_page=f"https://noragardner.com{pagination}"
            return next_page
            
        
        else:
            return False
    

crawler=Crawler()
crawler.start()