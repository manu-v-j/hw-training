from curl_cffi import requests
from parsel import Selector
from settings import headers,MONGO_DB,MONGO_URL,COLLECTION,COLLECTION_CATEGORY
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]

    def start(self):
        for item in self.db[COLLECTION_CATEGORY].find():
            url = item.get('link')
            while url:
                response = requests.get(url, headers=headers,impersonate='chrome')  
                
                if response.status_code == 200:
                    sel = Selector(text=response.text)
                    
                    product_urls = sel.xpath("//a[contains(@class,'productDetailsLink')]/@href").getall()
                    for product in product_urls:
                        full_url = f'https://shop.rewe.de{product}'
                        # print(full_url)
                    
                next_page = sel.xpath("//a[contains(@class,'plr-pagination__arrow--enabled')]/@href").get()
                if next_page:
                    url = f'https://shop.rewe.de{next_page}'
                else:
                    break
              

if __name__=='__main__':
    crawler=Crawler()
    crawler.start()
