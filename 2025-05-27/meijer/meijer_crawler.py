import requests
from settings import url, headers, MONGO_URI, DB_NAME, COLLECTION
import unicodedata
from pymongo import MongoClient
import re
import logging
import json

logging.basicConfig(level=logging.INFO)

class Crawler:

    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DB_NAME]
        self.collection = self.db[COLLECTION]

    def start(self):
            page=1
            while page:
                url=f"https://ac.cnstrc.com/browse/group_id/L1-918?c=ciojs-client-2.64.2&key=key_GdYuTcnduTUtsZd6&i=e14167cf-a719-4007-9eb3-eda086d4084f&s=3&us=web&page={page}&num_results_per_page=52&filters%5BavailableInStores%5D=20&sort_by=relevance&sort_order=descending&fmt_options%5Bgroups_max_depth%5D=3&fmt_options%5Bgroups_start%5D=current&_dt=1748333663952"

                payload = {
                    "c": "ciojs-client-2.64.2",
                    "key": "key_GdYuTcnduTUtsZd6",
                    "i": "e14167cf-a719-4007-9eb3-eda086d4084f",
                    "s": 3,
                    "us": "web",
                    "page": 1,
                    "num_results_per_page": 52,
                    "filters": {
                        "availableInStores": 20
                    },
                    "sort_by": "relevance",
                    "sort_order": "descending",
                    "fmt_options": {
                        "groups_max_depth": 3,
                        "groups_start": "current"
                    },
                    "_dt": 1748448712246
                }

                response = requests.get(url, headers=headers, json=payload)
                if response.status_code == 200:
                    has_items=self.parse_item(response)
                    if not has_items:
                        break
                    
                page+=1

    def parse_item(self, response):
        
        data = response.json()
        result_list = data.get("response", {}).get("results", [])
        
        if not result_list:
            return False
        
        for item in result_list:
            id = item.get("data", {}).get("id")
            summary = item.get("data", {}).get("summary", "")
            name = unicodedata.normalize('NFKD', summary)
            name = re.sub(r'[^\w\s-]', '', name)
            name = re.sub(r'[\s_]+', '-', name).lower()
            full_url = f"https://www.meijer.com/shopping/product/{name}/{id}.html"
            self.collection.insert_one({"link": full_url})
            
        return True
        

if __name__ == "__main__":
    crawler = Crawler()
    crawler.start()
