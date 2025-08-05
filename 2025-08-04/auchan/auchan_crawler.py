from curl_cffi import requests
from settings import headers, MONGO_URL, MONGO_DB, COLLECTION
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

    def start(self):
        page = 1
        while True:
            url = "https://auchan.hu/api/v2/cache/products"
            params = {
                "page": page,
                "itemsPerPage": 12,
                "categoryId": 5669,
                "cacheSegmentationCode": "",
                "hl": "hu"
            }
            response = requests.get(url, headers=headers, params=params, impersonate='chrome')
            
            if response.status_code != 200:
                logging.error(f"Request failed with status code: {response.status_code}")
                break

            data = response.json()
            product_list = data.get('results', [])
            if not product_list:
                logging.info("No more products found. Exiting...")
                break

            for info in product_list:
                name = info.get('selectedVariant', {}).get('name', '')
                sku = info.get('selectedVariant', {}).get('sku', '')
                if name and sku:
                    slug = name.lower().replace(" ", "-").replace(",", "").replace(".", "")
                    product_url = f"https://auchan.hu/shop/{slug}.p-{sku}"
                    try:
                        self.collection.insert_one({'link': product_url,'sku':sku})
                        logging.info(f"Inserted: {product_url}")
                    except DuplicateKeyError:
                        logging.warning(f"Duplicate link skipped: {product_url}")

            page += 1


if __name__ == '__main__':
    crawler = Crawler()
    crawler.start()
