import requests
from parsel import Selector
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY,COLLECTION
import logging,json,re
from pymongo import MongoClient,errors
logging.basicConfig(level=logging.INFO)

class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]

    def start(self):
        for item in self.db[COLLECTION_CATEGORY].find():
            url=item.get('link')
            service_id=item.get('service_id')
            match = re.search(r"\d+", url)
            if match:
                key=match.group()
            page = 0
            while True:
                params = {
                    'currency': 'USD',
                    'serviceType': 'pickup',
                    'categoryKey': key,
                    'limit': '60',
                    'offset': str(page * 60),  
                    'sort': 'relevance',
                    'testVariant': 'A',
                    'servicePoint': service_id,
                }


                response = requests.get(
                    "https://api.aldi.us/v3/product-search",
                    params=params,
                    headers=headers
                )

                data = response.json()
                product_list = data.get("data", [])

                if not product_list: 
                    break

                for product in product_list:
                    sku = product.get("sku", "")
                    url_name = product.get("urlSlugText", "")
                    product_url = f"https://www.aldi.us/product/{url_name}-{sku}"
                    try:
                        self.collection.insert_one({'link':product_url})
                        logging.info(product_url)

                    except errors.DuplicateKeyError:
                        logging.info(f"Duplicate: {product_url}")
                      
                page += 1  


if __name__=='__main__':
    crawler=Crawler()
    crawler.start()