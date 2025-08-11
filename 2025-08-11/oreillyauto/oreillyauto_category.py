import requests
from parsel import Selector
import re
import json
from settings import base_url,headers,MONGO_DB,MONGO_URL,CATAEGORY_COLLECTION
import logging
logging.basicConfig(level=logging.INFO)
from pymongo import MongoClient

class Category:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[CATAEGORY_COLLECTION]

    def start(self):
        response = requests.get(base_url, headers=headers)
        if response.status_code==200:
            self.parse_item(response)
    def parse_item(self,response):        
        sel=Selector(text=response.text)
        featured_url=sel.xpath("//div[@class='featured-categories_mobile-cat']/a/@href").get()
        url=f'https://www.oreillyauto.com{featured_url}'
        response=requests.get(url,headers=headers)
        selector=Selector(text=response.text)
        script_text = selector.xpath("//script[contains(text(), 'childCategories')]/text()").get()


        match = re.search(r"window\._ost\.childCategories\s*=\s*(\[.*?\]);", script_text, re.S)
        if match:
            data_str = match.group(1)
            data = json.loads(data_str.replace("'", '"'))  
            category_list = [item.get('url', '') for item in data]
            for item in category_list:
                full_url=f'https://www.oreillyauto.com{item}'
                self.collection.insert_one({'link':full_url})
                logging.info(full_url)

if __name__=='__main__':
    category=Category()
    category.start()
    
