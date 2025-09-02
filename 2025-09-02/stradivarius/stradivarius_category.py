import requests
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY
import json,re
from pymongo import MongoClient,errors

class Category:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_CATEGORY]
        self.collection.create_index('id', unique=True)

    def start(self):
        params = {
            'languageId': '-1',
            'typeCatalog': '1',
            'appId': '1',
        }

        response = requests.get(
            'https://www.stradivarius.com/itxrest/2/catalog/store/55009581/50331096/category',
            params=params,
            headers=headers,
        )
        self.parse_item(response)

    def parse_item(self,response):
        data = response.json()
       
        data_str = json.dumps(data)

        view_category_ids = re.findall(r'"viewCategoryId":\s*(\d+)', data_str)
        category_url_params= re.findall(r'"categoryUrlParam"\s*:\s*"([^"]+)"', data_str)


        category_ids = [int(x) for x in view_category_ids if int(x) != 0]
        category_url_params = [int(x) for x in category_url_params if x.strip()]


        for id in category_ids:
            try:
                self.collection.insert_one({'id':id})
            except errors.DuplicateKeyError:
                pass
        for url in category_url_params:
            try:
                self.collection.insert_one({'id': url})
            
            except errors.DuplicateKeyError:
                pass

if __name__=='__main__':
    category=Category()
    category.start()





