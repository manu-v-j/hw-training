import requests
from parsel import Selector
from pymongo import MongoClient
from setttings import headers,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY

class Category:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_CATEGORY]

    def start(self):
        base_url="https://www.lorespresso.com/fr_fr"
        response=requests.get(base_url,headers=headers)
        if response.status_code==200:
            self.parse_item(response)

    def parse_item(self,response):
        sel=Selector(text=response.text)
        category_urls=sel.xpath("//div[@class='MuiBox-root mui-style-1kci5st']//a/@href").getall()
        for url in category_urls:
            full_url=f"https://www.lorespresso.com{url}"

            self.collection.insert_one({'link':full_url})

if __name__=='__main__':
    category=Category()
    category.start()
