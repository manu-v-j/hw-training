import requests
from settings import headers, MONGO_URL, MONGO_DB, COLLECTION, COLLECTION_INPUT,COLLECTION_FAILED
from parsel import Selector
from pymongo import MongoClient,errors
import logging
from fuzzywuzzy import fuzz

logging.basicConfig(level=logging.INFO)

class Crawler:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[COLLECTION]
        self.collection.create_index('link',unique=True)
        self.collection_failed=self.db[COLLECTION_FAILED]

    def start(self):
        for item in self.db[COLLECTION_INPUT].find():
            part_number = item.get('PART_NUMBER', '')
            product_title = item.get('PRODUCT_TITLE', '')
            base_url = f"https://www.oreillyauto.com/search?q={part_number}"
            print(base_url)
            response = requests.get(base_url, headers=headers)
            if response.status_code == 200:
                self.parse_item(response, part_number, product_title)

    def parse_item(self, response, part_number, product_title):
        sel = Selector(text=response.text)
        product_names = sel.xpath("//h2[contains(@class,'product__name')]/text()").getall()
        product_links = sel.xpath("//a[contains(@class,'product__link')]/@href").getall()

        if not product_links:
            self.collection_failed.insert_one({'part':part_number})
            return

        matched = False
        for url in product_links:
            part = url.split('/')[-1].split('?')[0]
            # Check if the part number matches the input exactly
            if part == part_number:
                try:
                    full_url=f"https://www.oreillyauto.com{url}"
                    self.collection.insert_one({'link':full_url})
                    matched = True
                except errors.DuplicateKeyError:
                    logging.info(f"Duplicate: {url}")


            else:
                for name in product_names:
                    # To check if the name exists in product_title in both conditions
                    if (name in product_title) or (product_title in name):
                        try:
                            full_url=f"https://www.oreillyauto.com{url}"
                            self.collection.insert_one({'link':full_url})
                            matched = True
                        except errors.DuplicateKeyError:
                                logging.info(f"Duplicate: {url}")


                    else:
                    # To calculate the fuzzy ratio, if the ratio is greater than 70, get the URL
                        similarity = fuzz.ratio(product_title, name)
                        if similarity > 70:
                            try:
                                full_url=f"https://www.oreillyauto.com{url}"
                                self.collection.insert_one({'link':full_url})
                                matched = True
                            except errors.DuplicateKeyError:
                                logging.info(f"Duplicate: {url}")

        if not matched :
            self.collection_failed.insert_one({'part':part_number})


if __name__=='__main__':
    crawler=Crawler()
    crawler.start()