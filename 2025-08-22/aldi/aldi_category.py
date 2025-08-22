import requests
from parsel import Selector
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY
from pymongo import MongoClient
import logging,json
logging.basicConfig(level=logging.INFO)

class Category:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_CATEGORY]

    def start(self):
        response = requests.get('https://api.aldi.us/v2/service-points?addressZipcode=60113&serviceType=pickup&includeNearbyServicePoints=true', headers=headers)
        data_json=json.loads(response.text)
        store_id = data_json.get('data',[])[0].get('id','')
        response=requests.get(f'https://api.aldi.us/v2/product-category-tree?serviceType=pickup&servicePoint={store_id}',headers=headers)
        category_json=json.loads(response.text)
        category_list=category_json.get('data',[])
        for item in category_list:
            key=item.get('key','')
            name=item.get('urlSlugText','')
            category_url=f"https://www.aldi.us/products/{name}/{key}"
            self.collection.insert_one({'link':category_url,'service_id':store_id})

if __name__=='__main__':
    category=Category()
    category.start()
