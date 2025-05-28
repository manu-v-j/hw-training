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
        page = 1
        while page:
            payload = {
                "c": "ciojs-client-2.64.2",
                "key": "key_GdYuTcnduTUtsZd6",
                "i": "e14167cf-a719-4007-9eb3-eda086d4084f",
                "s": 3,
                "us": "web",
                "page": page,
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
                "_dt": 1748333663952
            }

            response = requests.get(url, headers=headers, json=payload)
            if response.status_code == 200:
                self.parse_item(response)
                
                   

            page += 1

    def parse_item(self, response):
        
        data = response.json()
        result_list = data.get("response", {}).get("results", [])

        
        for item in result_list:
            id = item.get("data", {}).get("id")
            summary = item.get("data", {}).get("summary", "")
            name = unicodedata.normalize('NFKD', summary)
            name = re.sub(r'[^\w\s-]', '', name)
            name = re.sub(r'[\s_]+', '-', name).lower()
            full_url = f"https://www.meijer.com/shopping/product/{name}/{id}.html"
            print(full_url)
            # self.collection.insert_one({"link": full_url})
            
        return True
        

if __name__ == "__main__":
    crawler = Crawler()
    crawler.start()
