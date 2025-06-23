import requests
from parsel import Selector
from settings import MONGO_URI,MONGO_DB,COLLECTION,headers
import re
import json
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]

    def start(self):
        payload = {
                        "id": ["20003545", "360545"]
                }

        response=requests.post('https://www.walgreens.com/productsearch/v1/categories',json=payload,headers=headers)
        self.parse_item(response)
    
    def parse_item(self,response):
        data=response.json()
        category=data.get("categories",[])
        for item in category:
            category_url=item.get("url","")
            full_url=f"https://www.walgreens.com{category_url}"
            response_product=requests.get(full_url,headers=headers)
            sel=Selector(text=response_product.text)
            script_content = sel.xpath('//script[contains(text(), "window.getInitialState")]/text()').get()

            if script_content:
                json_match = re.search(r'return\s*(\{.*})', script_content, re.DOTALL)
                match=json_match.group(1)
                if match.endswith('}'):
                    match=match[:-1]
                    data=json.loads(match)
                    result_list=data.get("searchResult",{}).get("productList",[]) 
                    for item in result_list:
                        product_url=item.get("productInfo",{}).get("productURL","")
                        url=f"https://www.walgreens.com{product_url}"
                        item={}
                        item['link']=url
                        # logging.info(item)
                        # self.collection.insert_one({'link':url})


if __name__=='__main__':
    crawler=Crawler()
    crawler.start()
