import requests
from parsel import Selector
import logging
from settings import headers,MONGO_DB,MONGO_URI,COLLECTION
from pymongo import MongoClient
logging.basicConfig(level=logging.INFO)

class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]

    def start(self):
        page=1
        while True:
            url=f"https://www2.hm.com/en_in/women/shop-by-product/tops.html?productTypes=Top&page={page}"
            response=requests.get(url,headers=headers)
            if response.status_code==200:
                has_product=self.parse_item(response)
                if not has_product:
                   break
            page+=1
    def parse_item(self,response):
        sel=Selector(text=response.text)
        product_urls=sel.xpath("//div[@class='e4889e']/a/@href").getall()
        if not product_urls:
            return False
        for url in product_urls:
            item={}
            item['link']=url
            self.collection.insert_one(item)

        return True 
            

if __name__=='__main__':
    crawler=Crawler()
    crawler.start()