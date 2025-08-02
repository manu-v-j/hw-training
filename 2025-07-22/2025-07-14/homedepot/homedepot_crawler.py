import requests
from parsel import Selector
import logging
from settings import headers,CATEGORY_COLLECTION,MONGO_URI,MONGO_DB,COLLECTION
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
logging.basicConfig(level=logging.INFO)
from pymongo.errors import DuplicateKeyError


class Crawler:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[COLLECTION]
        self.collection.create_index("link", unique=True)

        self.count = 0

    def start(self):
        for item in self.db[CATEGORY_COLLECTION].find():
            url_base = item.get('link')
            page = 0
            while True:
                url = f'{url_base}?Nao={page}'
                logging.info(url)
                response = requests.get(url, headers=headers)
                has_item = self.parse_item(response)
                if not has_item:
                    break
                page += 24

    def parse_item(self, response):
        sel = Selector(text=response.text)
        product_urls = sel.xpath("//a[@class='sui-top-0 sui-left-0 sui-absolute sui-size-full sui-z-10']/@href").getall()
        if not product_urls:
            print("No more products found.")
            return False

        for product in product_urls:
            full_url = f"https://www.homedepot.com{product}"
            try:
                self.count += 1
                logging.info(f"{self.count} {full_url}")
                self.collection.insert_one({'link':full_url})
            except DuplicateKeyError:
                logging.info(f"Duplicate link skipped: {full_url}")
                continue
        return True

if __name__ == '__main__':
    crawler = Crawler()
    crawler.start()