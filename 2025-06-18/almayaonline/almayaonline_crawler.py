import requests
from parsel import Selector
from pymongo import MongoClient
from settings import headers,MONGO_URI,DB_NAME,CATEGORY,COLLECTION
import logging
logging.basicConfig(level=logging.INFO)

class Crawler:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DB_NAME]
        self.collection=self.db[COLLECTION]

    def start(self):
        for item in self.db[CATEGORY].find():
            base_url=item.get('link')
            while True:
                response=requests.get(base_url,headers=headers)
                if response.status_code==200:
                    next_page=self.parse_item(response)
                    if not next_page:
                        break
                    base_url=next_page

    def parse_item(self,response):
            sel=Selector(text=response.text)
            product_urls=sel.xpath("//h2[@class='product-title']/a/@href").getall()
            for product in product_urls:
                full_url=f"https://www.almayaonline.com{product}"
                item={}
                item['link']=full_url
                self.collection.insert_one(item)
                logging.info(full_url)

            next_page=sel.xpath("//li[@class='next-page']/a/@href").get()
            if next_page:
                return next_page

            else:
                return False
            
if __name__=='__main__':
    crawler=Crawler()
    crawler.start()