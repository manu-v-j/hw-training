from settings import headers,MONGO_URL,MONGO_DB,CATAEGORY_COLLECTION,SUBCATEGORY_COLLECTION
import requests
from parsel import Selector
from pymongo import MongoClient
import re,json
import logging

class Subcategory:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[SUBCATEGORY_COLLECTION]
    def start(self):
        for item in self.db[CATAEGORY_COLLECTION].find():
            url=item.get('link')
            response=requests.get(url,headers=headers)
            sel=Selector(text=response.text)
            script_text=sel.xpath("//script[contains(text(), 'window._ost.childCategories')]/text()").get()

            match = re.search(r"window\._ost\.childCategories\s*=\s*(\[.*?\]);", script_text, re.S)
            if match:
                data_str = match.group(1)
                data = json.loads(data_str.replace("'", '"'))  
                category_list = [item.get('url', '') for item in data]
                for item in category_list:
                    full_url=f'https://www.oreillyauto.com{item}'
                    print(full_url)

if __name__=='__main__':
    subcategory=Subcategory()
    subcategory.start()