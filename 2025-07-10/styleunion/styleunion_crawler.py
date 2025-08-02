import requests
from parsel import Selector
from settings import headers,MONGO_URI,MONGO_DB,COLLECTION,COLLECTION_CATEGORY
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)
from pymongo.errors import DuplicateKeyError

class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]
        self.collection.create_index('link',unique=True)
        self.count = 0
        
    def start(self):    
        for item in self.db[COLLECTION_CATEGORY].find():
            url=item.get('link')
            page = 1

            while url:
                full_url=f"{url}?page={page}"
                logging.info(full_url)
                response = requests.get(full_url, headers=headers)
                if response.status_code==200:
                    has_item=self.parse_item(response)
                    if not has_item:
                        break
                page += 1

    def parse_item(self,response):
        sel = Selector(text=response.text)
        product_urls = sel.xpath("//div[@class='product-info']/a/@href").getall()

        if not product_urls:
            return False
        
        for product_url in product_urls:
            full_url = f"https://styleunion.in{product_url}"
            try:
                self.count += 1
                logging.info(self.count)
                logging.info(full_url)
                item={}
                item['link']=full_url
                self.collection.insert_one(item)
            except DuplicateKeyError:
                logging.debug(f"Duplicate skipped: {full_url}")

        

if __name__=='__main__':
    crawler=Crawler()
    crawler.start()