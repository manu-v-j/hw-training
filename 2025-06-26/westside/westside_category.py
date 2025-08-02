import requests
from parsel import Selector
from settings import headers,url,MONGO_URI,MONGO_DB,COLLECTION_CATEGORY
from pymongo import MongoClient

class Category:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_CATEGORY]

    def start(self):
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            self.parse_item(response)

    def parse_item(self,response):
        sel=Selector(text=response.text)
        category_link=sel.xpath("//div[@class='MegaMenu-child-inner']/a/@href").getall()
        for url in category_link:
            if 'https://www.westside.com' not in url:
                fullurl=f"https://www.westside.com{url}"
            else:
                fullurl=url
            item={}
            item['link']=fullurl

            self.collection.insert_one(item)

if __name__=='__main__':
    category=Category()
    category.start()
