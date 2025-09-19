import requests
from parsel import Selector
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY,COLLECTION
from pymongo import MongoClient,errors
import logging
logging.basicConfig(level=logging.INFO)

class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]
        self.collection.create_index('link',unique=True)

    def start(self):
        for item in self.db[COLLECTION_CATEGORY].find():
            id=item.get('id')
         
            count=0
            while True:
                base_url=f'https://www.portwest.com/products/load_more_category_products/{id}/{count}'
                response = requests.get(base_url,headers=headers)
                has_item=self.parse_item(response)
                if not has_item:
                    break

                count+=12
    def parse_item(self,response):
        sel=Selector(text=response.text)
        product_urls=sel.xpath("//h2[@class='product-title']/a/@href").getall()
        if not product_urls:
            return False
        for url in product_urls:
            try:
                full_url=f"https://www.portwest.com{url}"
                self.collection.insert_one({'link':full_url})
                logging.info(full_url)

            except errors.DuplicateKeyError:
                logging.info(f"Duplicate: {full_url}")   

        return True
    
if __name__=='__main__':
    crawler=Crawler()
    crawler.start()