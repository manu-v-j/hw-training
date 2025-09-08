import re
import json
from settings import headers,MONGO_URL,MONGO_DB,CATAEGORY_COLLECTION
from pymongo import MongoClient
from curl_cffi import requests
from parsel import Selector
import logging
logging.basicConfig(level=logging.INFO)

class Category:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[CATAEGORY_COLLECTION]

    def bypass_akamai(self,session, url, headers):
        r = session.get(url, headers=headers, impersonate="chrome")
        
        if "bm-verify" not in r.text:
            return r  
        
        
        token = re.search(r'"bm-verify":\s*"([^"]+)"', r.text)
        token = token.group(1) if token else None
        
        i_match = re.search(r"var i = (\d+);", r.text)
        concat_match = re.search(r'Number\("(\d+)" \+ "(\d+)"\)', r.text)
        
        if not (token and i_match and concat_match):
            raise RuntimeError("Could not parse Akamai challenge")
        
        i = int(i_match.group(1))
        concat_val = concat_match.group(1) + concat_match.group(2)
        pow_val = i + int(concat_val)
        
        payload = {"bm-verify": token, "pow": pow_val}
        
        verify_url = url.split("/", 3)[:3]
        verify_url = "/".join(verify_url) + "/_sec/verify?provider=interstitial"

        vr = session.post(verify_url, headers=headers, data=json.dumps(payload), impersonate="chrome")
        
        
        r2 = session.get(url, headers=headers, impersonate="chrome")
        return r2

    def start(self):
        with requests.Session() as s:
            url = "https://www.zara.com/ae"
            response = self.bypass_akamai(s, url, headers)
            if response.status_code==200:
                self.parse_item(response)
    def parse_item(self,response):
        sel=Selector(text=response.text)
        category_urls=sel.xpath("//li[contains(@class,'layout-categories-category') and contains(@data-layout,'products-category-view')]/a/@href").getall()
        for url in category_urls:
            self.collection.insert_one({'link':url})
            logging.info(url)
if __name__=='__main__':
    category=Category()
    category.start()