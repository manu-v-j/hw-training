import requests
from parsel import Selector
from pymongo import MongoClient
from settings import headers, MONGO_URL, MONGO_DB, CATEGORY_COLLECTION, COLLECTION
import logging
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO)

class Crawler:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[COLLECTION]

    def start(self):
        count = 0
        for item in self.db[CATEGORY_COLLECTION].find():
            base_url = item.get('link')

            page_url = base_url
            seen = set()

            while True:
                print(f"Fetching: {page_url}")
                response = requests.get(page_url, headers=headers)
                sel = Selector(text=response.text)

                product_urls = sel.xpath(
                    "//a[contains(@class,'styled__ImageContainer-sc-1fweb41-0')]/@href").getall()

                if not product_urls:
                    break

                for p_url in product_urls:
                    full_url = urljoin("https://www.tesco.com", p_url)
                    if full_url not in seen:
                        seen.add(full_url)
                        logging.info(full_url)
                        count += 1
                        print(count)

                next_href = sel.xpath("//a[@aria-label='Next page']/@href").get()
                if next_href:
                    page_url = urljoin("https://www.tesco.com", next_href)
                else:
                    break


if __name__ == '__main__':
    crawler = Crawler()
    crawler.start()
