import requests
from settings import headers, MONGO_URL, MONGO_DB, COLLECTION, COLLECTION_INPUT, COLLECTION_FAILED
from parsel import Selector
from pymongo import MongoClient, errors
import logging
from fuzzywuzzy import fuzz

logging.basicConfig(level=logging.INFO)


class Crawler:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[COLLECTION]
        self.collection.create_index("link", unique=True)
        self.collection_failed = self.db[COLLECTION_FAILED]

    def start(self):
        count = 1
        for item in self.db[COLLECTION_INPUT].find():
            part_number = item.get("PART_NUMBER", "").strip()
            product_title = item.get("PRODUCT_TITLE", "").strip()


            base_url = f"https://www.oreillyauto.com/search?q={part_number}"
            logging.info(f"[{count}] Crawling: {base_url}")
        
            response = requests.get(base_url, headers=headers)
            if response.status_code == 200:
                self.parse_item(response, part_number, product_title)

            count += 1

    def parse_item(self, response, part_number, product_title):
        sel = Selector(text=response.text)
        product_links = sel.xpath("//a[contains(@class,'product__link')]/@href").getall()
        product_names = sel.xpath("//h2[contains(@class,'product__name')]/text()").getall()

        if not product_links:
            logging.warning(f"No product links found for part {part_number}")
            self.collection_failed.insert_one({"part": part_number, "reason": "no_links"})
            return

        matched = False
        for url, name in zip(product_links, product_names):
            part = url.split("/")[-1].split("?")[0].strip()
            full_url = f"https://www.oreillyauto.com{url}"

            #  Exact match on part number
            if part == part_number:
                matched = self.insert_link(full_url, part, name, product_title,matched="part") or matched
                continue

            # Title contains check
            elif (name in product_title) or (product_title in name):
                matched = self.insert_link(full_url, part, name, product_title,matched="text_contains") or matched
                continue

            #  Fuzzy matching 
            elif name and product_title:
                similarity = fuzz.ratio(product_title, name)
                if similarity > 70:
                    matched = (
                        self.insert_link(full_url, part, name, product_title,matched="fuzzy") or matched
                    )

        if not matched:
            logging.info(f"No match found for part {part_number}")
            self.collection_failed.insert_one({"part": part_number, "reason": "no_match"})

    def insert_link(self, full_url, part, product_name, product_title,matched):
        try:
            self.collection.insert_one(
                {
                    "link": full_url,
                    "part": part,
                    "product_name": product_name,
                    "product_title": product_title,
                    "matched":matched
                }
            )
            logging.info(f"Inserted: {full_url}")
            return True
        except errors.DuplicateKeyError:
            logging.info(f"Duplicate skipped: {full_url}")
            return False


if __name__ == "__main__":
    crawler = Crawler()
    crawler.start()
