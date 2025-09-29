from curl_cffi import requests
from parsel import Selector
import logging
from pymongo import MongoClient,errors
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY,COLLECTION

logging.basicConfig(level=logging.INFO)

class Crawler:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]
        self.collection.create_index('link',unique=True)

    def start(self):
        for item in self.db[COLLECTION_CATEGORY].find():
            base_url=item.get('link','')
            count=0
            while True:
                params = {
                    'from': str(count),
                    'size': '40',
                }
                response=requests.get(base_url,params=params,headers=headers,impersonate='chrome')
                print(base_url)
                if response.status_code==200:
                    has_item=self.parse_item(response)
                    if not has_item:
                        break

                count+=40
                print(count)
    def parse_item(self,response):
        sel=Selector(text=response.text)
        product_urls=sel.xpath("//div[contains(@class,'product-card-details__item')]/h2/a/@href").getall()

        if not product_urls:
            return False

        for url in product_urls:
            try:
                full_url=f"https://www.decathlon.de{url}"
                self.collection.insert_one({'link':full_url})

            except errors.DuplicateKeyError:
                logging.info(f"Duplicate: {full_url}")

        
        return True

if __name__=='__main__':
    crawler=Crawler()
    crawler.start()