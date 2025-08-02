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
            url=item.get('link')
            while url:
                response=requests.get(url,headers=headers,verify=False)
                if response.status_code==200:
                    url=self.parse_item(response)
                    if not url:
                        break
    def parse_item(self,response):
        sel=Selector(text=response.text)
        product_urls=sel.xpath("//a[contains(@class,'ProductImage_productLink__G_6o_')]/@href").getall()
        for product in product_urls:
            try:
                full_url=f'https://www.lego.com{product}'
                self.collection.insert_one({'link':full_url})
                
            except errors.DuplicateKeyError:
                logging.info(f"Duplicate: {full_url}")
            logging.info(full_url)     

        next_page=sel.xpath("//a[contains(@class,'Paginationstyles__NextLink-sc-npbsev-10 kgXhfG')]/@href").get()
        if next_page:
            url=f'https://www.lego.com{next_page}'
            return url
        else:
            return None


if __name__=='__main__':
    carwler=Crawler()
    carwler.start()