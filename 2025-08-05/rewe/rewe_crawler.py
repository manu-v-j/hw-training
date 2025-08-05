from curl_cffi import requests
from settings import headers,base_url,MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_CATEGORY
from parsel import Selector
from pymongo import MongoClient,errors
import logging
logging.basicConfig(level=logging.INFO)

class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]
        self.collection.create_index('link', unique=True)

    def start(self):
         for item in self.db[COLLECTION_CATEGORY].find():
            base_url = item.get('link')
            page = 1
            while True:
                url = f"{base_url}&page={page}"
                response = requests.get(base_url, headers=headers, impersonate='chrome')
                if response.status_code == 200:
                    has_item = self.parse_item(response)
                    if not has_item:
                        break
                page+=1
        
    def parse_item(self,response):
        sel=Selector(text=response.text)
        product_urls=sel.xpath("//a[contains(@class,'productDetailsLink')]/@href").getall()
        if not product_urls:
            return False
        
        for link in product_urls:
            try:
                full_url=f'https://shop.rewe.de{link}'
                self.collection.insert_one({'link':full_url})
                
            except errors.DuplicateKeyError:
                logging.info(f"Duplicate: {full_url}")


            logging.info(full_url)

if __name__=='__main__':
    crawler=Crawler()
    crawler.start()
