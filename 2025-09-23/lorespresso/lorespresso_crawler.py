import requests
import logging
from parsel import Selector
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
            base_url=item.get('link')
            response = requests.get(base_url, headers=headers)

            if response.status_code==200:
                self.parse_item(response)

    def parse_item(self,response):
        sel=Selector(text=response.text)
        product_range=sel.xpath("//div[@class='MuiBox-root mui-style-1wcjc1k']//a/@href").getall()
        for category_url in product_range:
            page = 1
            while True:
                full_url = f"https://www.lorespresso.com/{category_url}/page/{page}"
                response = requests.get(full_url, headers=headers)
                print(full_url)
                if response.status_code == 200:
                    selector = Selector(text=response.text)
                    product_urls = selector.xpath("//div[contains(@class, 'ProductListItem-titleContainer')]//a/@href").getall()

                    if not product_urls:
                        break

                    for product in product_urls:
                        try:
                            product_url = f"https://www.lorespresso.com/{product}"
                            self.collection.insert_one({'link':product_url})

                            logging.info(product_url)
                        except errors.DuplicateKeyError:
                            logging.info(f"Duplicate: {full_url}")
                else:
                    break  
                page += 1

if __name__=='__main__':
    crawler=Crawler()
    crawler.start()
