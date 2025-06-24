from parsel import Selector
from settings import MONGO_URI,MONGO_DB,COLLECTION
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

class Crawler:

    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]

    def start(self):
        with open('/home/user/Hashwave/2025-06-24/petco/plp.html', 'r') as f:
            html = f.read()
            self.parse_item(html)
    
    def parse_item(self,html):
        sel = Selector(text=html)
        product_urls=sel.xpath("//h2[@class='ProductTile-styled__ProductTitle-sc-3aa49169-1 hYjpyg']/a/@href").getall()
        for url in product_urls:
            items={}
            items['link']=url
            self.collection.insert_one(items)
            logging.info(items)



if __name__=="__main__":
    crawler=Crawler()
    crawler.start()