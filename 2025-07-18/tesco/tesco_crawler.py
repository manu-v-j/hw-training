import requests
from parsel import Selector
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from settings import headers, MONGO_URL, MONGO_DB, CATEGORY_COLLECTION, COLLECTION
import logging
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO)

class Crawler:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[COLLECTION]
        self.collection.create_index('link',unique=True)
        self.count = 0

    def start(self):
        for item in self.db[CATEGORY_COLLECTION].find():
            base_url = item.get('link')
            page_url = base_url

            while page_url:
                logging.info(f"Fetching: {page_url}")
                response = requests.get(page_url, headers=headers)
                if response.status_code == 200:
                    page_url = self.parse_item(response)
                else:
                    break

    def parse_item(self, response):
        sel = Selector(text=response.text)
        product_urls = sel.xpath(
            "//a[contains(@class,'styled__Anchor-sc-1i711qa-0 gJVSxB ddsweb-link__anchor')]/@href | //a[@class='a59700_dUMb6G_imageContainer']/@href"
        ).getall()

        if not product_urls:
            return None

        for url in product_urls:
            try:
                full_url = urljoin("https://www.tesco.com", url)
                self.collection.insert_one({'link':full_url})
                logging.info(full_url)
                self.count += 1
                print(self.count)
            except DuplicateKeyError:
                logging.warning(f"Duplicate link skipped: {full_url}")

        next_href = sel.xpath("//a[@aria-label='Next page']/@href").get()
        if next_href:
            page_url=urljoin("https://www.tesco.com", next_href)
            return page_url
        else:
            return None


if __name__ == '__main__':
    crawler = Crawler()
    crawler.start()
