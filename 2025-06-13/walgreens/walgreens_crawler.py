import requests
from parsel import Selector
from settings import MONGO_URI,MONGO_DB,COLLECTION
import re
import json
from pymongo import MongoClient

class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]

    def start(self):
        count=0        
        payload = {
                        "id": ["20003545", "360545"]
                }

        response=requests.post('https://www.walgreens.com/productsearch/v1/categories',json=payload)
        self.parse_item(response,count)
    
    def parse_item(self,response,count):
        data=response.json()
        category=data.get("categories",[])
        for item in category:
            category_url=item.get("url","")
            full_url=f"https://www.walgreens.com{category_url}"
            response=requests.get(full_url)
            sel=Selector(text=response.text)
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
                        print(url)
                        self.collection.insert_one({'link':url})
                        count+=1


if __name__=='__main__':
    crawler=Crawler()
    crawler.start()
