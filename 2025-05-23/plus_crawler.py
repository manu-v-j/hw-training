import requests
from settings import *
import json
from pymongo import MongoClient

class Crawler:

    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[DB_NAME]
        self.collection=self.db[COLLECTION]

    def start(self,url):
        num = 1

        while num < 43:
            payload = {
                "versionInfo": {
                    "moduleVersion": "PuN3d6LB4faGdgG7sxfsDQ",
                    "apiVersion": "bYh0SIb+kuEKWPesnQKP1A"
                },
                "screenData": {
                    "variables": {
                        "AppliedFiltersList": {
                            "List": [],
                            "EmptyListItem": {
                                "Name": "",
                                "Quantity": "0",
                                "URL": ""
                            }
                        },
                        "CategorySlug": "kaas",
                        "CheckoutId": "46877c68-4b0d-4816-ac21-c46d6ea4fd7f",
                        "LocalCategoryID": 0,
                        "LocalCategoryName": "",
                        "LocalCategoryParentId": 0,
                        "LocalCategoryTitle": "",
                        "Monitoring_FlowTypeId": 3,
                        "OneWelcomeUserId": "",
                        "OrderEditId": "",
                        "PageNumber": num
                    }
                },
                "viewName": "MainFlow.ProductListPage"
            }

            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 200:
                self.parse_item(response)

            num += 1

    def parse_item(self,response):
        data = response.json()
        product_list = data.get('data', {}).get('ProductList', {}).get("List", [])

        base_url = "https://www.plus.nl/product/" 
        for item in product_list:
            url = item.get("PLP_Str", {}).get("Slug")
            if url:
                full_url = base_url + url
                self.collection.insert_one({'link':full_url})
           

if __name__=="__main__":
    crawler=Crawler()
    crawler.start(url)