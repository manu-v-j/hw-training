import requests
from parsel import Selector
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION,category_list
from pymongo import MongoClient, errors
import logging
logging.basicConfig(level=logging.INFO)
url='https://www.mylittlesalesman.com/trucks-for-sale-i2c0f0m0?ptid=1'


class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]
        self.collection.create_index('link',unique=True)

    def start(self):
        for url in category_list:
            while url:
                response=requests.get(url,headers=headers)
                if response.status_code==200:
                    url=self.parse_item(response)
                    if not url:
                        break
                    
    def parse_item(self,response):
        sel=Selector(text=response.text)
        product_urls=sel.xpath("//div[@class='col-12 col-xl-3 c5g pri']/a/@href").getall()
        for product in product_urls:
            try:
                full_url=f'https://www.mylittlesalesman.com{product}'
                self.collection.insert_one({'link':full_url})
                logging.info(full_url)

            except errors.DuplicateKeyError:
                logging.info(f"Duplicate: {full_url}")

        next_page=sel.xpath("//li[@class='page-item pagination-next']/a/@href").get()
        if next_page:
            url=f'https://www.mylittlesalesman.com{next_page}'
            return url
        
if __name__=='__main__':
    crawler=Crawler()
    crawler.start()