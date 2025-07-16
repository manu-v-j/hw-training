import requests
from parsel import Selector
from settings import headers,MONGO_URI,MONGO_DB,COLLECTION_CATEGORY,COLLECTION
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)
from pymongo.errors import DuplicateKeyError


class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]
        self.collection.create_index('link',unique=True)

    def  start(self):
        
        for item in self.db[COLLECTION_CATEGORY].find():
            url=item.get('link')
            id=item.get('id')
            print(id)
            page=1
            while True:
                url = 'https://navigator-group1.tweakwise.com/navigation/ed681b01'

                payload = {
                    "tn_q": "",
                    "tn_p": page,
                    "tn_ps": 16,
                    "tn_sort": "Relevantie",
                    "tn_profilekey": "fJLU4uH7kLxf4omMWx974frxbwC0qhWsY4FV8S0HluLIkg==",
                    "tn_cid": id,
                    "CatalogPermalink": "producten",
                    "CategoryPermalink": "aardappelen-groente-fruit",
                    "format": "json",
                    "tn_parameters": "ae-productorrecipe=product"
                }                
                response=requests.post(url,headers=headers,params=payload)
                has_item=self.parse_item(response)
                if not has_item:
                    break
                page+=1

    def parse_item(self,response):
        data = response.json()
        item_list=data.get('items',[])   
        if not item_list:
            return False
        for item in item_list:
            product_url=item.get('url','')
            try:
                self.collection.insert_one({'link':product_url})
                logging.info(product_url)

            except DuplicateKeyError:
                logging.debug(f"Duplicate skipped: {product_url}")
        return True
                
if __name__=='__main__':
    crawler=Crawler()
    crawler.start()