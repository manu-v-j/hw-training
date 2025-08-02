from curl_cffi import requests
from parsel import Selector
from settings import headers, base_url, MONGO_URL, MONGO_DB, COLLECTION
from pymongo.errors import DuplicateKeyError
from pymongo import MongoClient
import logging

logging.basicConfig(level=logging.INFO)

class Crawler:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[COLLECTION]
        self.collection.create_index('link', unique=True)

    def start(self, base_url):
        while base_url:
            response = requests.get(base_url, headers=headers)
            if response.status_code == 200:
                base_url = self.parse_item(response)  
            else:
                break

    def parse_item(self, response):
        sel = Selector(text=response.text)
        product_urls = sel.xpath("//div[@class='description-spacing']/a/@href").getall()

        for url in product_urls:
            try:
                full_url = f"https://www.macys.com{url}"
                logging.info(full_url)
                self.collection.insert_one({'link': full_url})
            except DuplicateKeyError:
                logging.warning(f"Duplicate link skipped: {full_url}")

      
        next_page = sel.xpath("//li[contains(@class,'chevron-next chevron-next')]/a/@href").get()
        if next_page:
            base_url=f"https://www.macys.com{next_page}"
            return base_url
        return None


if __name__ == '__main__':
    crawler = Crawler()
    crawler.start(base_url)
