from curl_cffi import requests
from parsel import Selector
from settings import headers,url,MONGO_DB,MONGO_URI,CATEGORY_COLLECTION
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

class Category:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[CATEGORY_COLLECTION]

    def start(self,url):
        try:
            response = requests.get(url, headers=headers)
            sel = Selector(text=response.text)

            product_links = sel.xpath("//a[@class='sui-top-0 sui-left-0 sui-absolute sui-size-full sui-z-10']/@href").getall()
            if product_links:
                print(url)  
                self.collection.insert_one({'link':url})               

            subcategories = [
                href for href in sel.xpath("//li[contains(@class, 'side-navigation__li')]//a/@href").getall()
                if "Appliances-Kitchen-Appliance-Packages" not in href
            ]
            subcategories = [f"https://www.homedepot.com{sub}" if sub.startswith('/') else sub for sub in subcategories]

            for sub_url in subcategories:
                self.start(sub_url)

        except Exception as e:
            print(f"Error on {url}: {e}")

  
if __name__=='__main__':
    category=Category()
    category.start(url)

