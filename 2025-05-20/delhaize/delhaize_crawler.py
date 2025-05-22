import requests
from settings import *
from pymongo import MongoClient

class Crawler:
    
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[DB_NAME]
        self.collection=self.db[COLLECTION]

    def start(self):
        num = 0
        max_pages = 11

        while num < max_pages:
            url = f"https://www.delhaize.be/api/v1/?operationName=GetCategoryProductSearch&variables=%7B%22lang%22%3A%22nl%22%2C%22searchQuery%22%3A%22%3Arelevance%22%2C%22sort%22%3A%22relevance%22%2C%22category%22%3A%22v2WIN%22%2C%22pageNumber%22%3A{num}%2C%22pageSize%22%3A20%2C%22filterFlag%22%3Atrue%2C%22fields%22%3A%22PRODUCT_TILE%22%2C%22plainChildCategories%22%3Atrue%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%224a9b385fdead25bb28350f1968ff36b8c44cf2def250653c8c81cbd3ece02e18%22%7D%7D"

            response = requests.get(url)
            if response.status_code == 200:
                self.parse_item(response)

            num += 1

    def parse_item(self,response):
        data = response.json()
        products = data.get("data", {}).get("categoryProductSearch", {}).get("products", [])
        for product in products:
            product_url = product.get("url")
            if product_url:
                full_url = 'https://www.delhaize.be' + product_url

                self.collection.insert_one({"url":full_url})

        return True  

if __name__ == "__main__":
    crawler=Crawler()
    crawler.start()