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
        self.collection.create_index('link',unique=True)

    def start(self):
        for item in self.db[COLLECTION_CATEGORY].find():
            base_url = item.get('link')
            page = 1
            while True:
                url = f"{base_url}&page={page}"
                response = requests.get(url, headers=headers, impersonate='chrome')
                sel = Selector(text=response.text)
                product_urls = sel.xpath("//a[contains(@class,'productDetailsLink')]/@href").getall()

                if not product_urls:
                    print("No more products. Stopping.")
                    break

                print(f"Scraping: {url}")

                for product in product_urls:
                    full_url = f"https://shop.rewe.de{product}"
                    try:
                        self.collection.insert_one({'link': full_url})
                        logging.info(full_url)
                    except:
                        logging.warning(f"Duplicate skipped: {full_url}")

                page += 1

if __name__=='__main__':
    crawler=Crawler()
    crawler.start()
