import requests
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY,COLLECTION
import json,re
from pymongo import MongoClient,errors
import logging
logging.basicConfig(level=logging.INFO)


class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]
        self.collection.create_index("id", unique=True)
        self.collection.create_index("link", unique=True)


    def start(self):
        for item in self.db[COLLECTION_CATEGORY].find():
            id=item.get('id','')
            print(id)
            params = {
                'languageId': '-1',
                'showProducts': 'false',
                'priceFilter': 'true',
                'appId': '1',
            }
            response = requests.get(
                f'https://www.stradivarius.com/itxrest/3/catalog/store/55009581/50331096/category/{id}/product',
                params=params,
                headers=headers,
            )
            response.raise_for_status()
            data = response.json()

            element_list = data.get('gridElements', [])
            all_pids = []
            for item in element_list:
                product_ids = item.get('ccIds', [])
                all_pids.extend(product_ids)

            for pid in all_pids:
                params = {
                    'languageId': '-1',
                    'categoryId': '1390584',
                    'productIds': str(pid),   
                    'appId': '1',
                }

                response = requests.get(
                    'https://www.stradivarius.com/itxrest/3/catalog/store/55009581/50331096/productsArray',
                    params=params,
                    headers=headers,
                )
                response.raise_for_status()
                data = response.json()

                product_list = data.get('products', [])
                for product in product_list:
                    summary_list = product.get('bundleProductSummaries', [])
                    for item in summary_list:
                        url = item.get('productUrl', '').lstrip('/')
                        if url:
                            try:
                                full_url = f"https://www.stradivarius.com/ae/{url}"
                                item={}
                                item['id']=pid
                                item['link']=full_url
                                self.collection.insert_one(item)    
                                print(item)   
                            except errors.DuplicateKeyError:
                                logging.info(f"Duplicate: {pid}")               


if __name__=='__main__':
    crawler=Crawler()
    crawler.start()

