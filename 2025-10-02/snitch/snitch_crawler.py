import requests
from parsel import Selector
import logging
from pymongo import MongoClient,errors
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION

logging.basicConfig(level=logging.INFO)

class Crawler:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]
        self.collection.create_index('link',unique=True)

    def start(self):
        page=1
        while True:
            params = {
                'page': str(page),
                'limit': '100',
                '0': '[object Object]',
                'product_type': 'Shirts',
            }

            response = requests.get('https://mxemjhp3rt.ap-south-1.awsapprunner.com/products/plp/v2', params=params, headers=headers)
            data=response.json()
            product_list=data.get('data',{}).get('products',[])
            if not product_list:
                break
            for item in product_list:
                id=item.get('shopify_product_id','')
                handle=item.get('handle','')
                try:
                    full_url=f"https://www.snitch.com/men-shirts/{handle}/{id}/buy"
                    self.collection.insert_one({'link':full_url})
                    logging.info(full_url)

                except errors.DuplicateKeyError:
                    logging.info(f"Duplicate: {full_url}")


            page+=1

if __name__=='__main__':
    crawler=Crawler()
    crawler.start()