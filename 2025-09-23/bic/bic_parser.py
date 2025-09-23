import requests
from parsel import Selector
from pymongo import MongoClient
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY,COLLECTION_DETAILS,COLLECTION_ERROR

class Parser:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.products=['https://eu.bic.com/en-gb/beauty/hybrid-flex',
                       'https://eu.bic.com/en-gb/beauty/click-soleil',
                       '']

    def start(self):
        for base_url in self.products:
            response = requests.get(base_url, headers=headers)
            print(response.status_code)
            if response.status_code==200:
                self.parse_item(response)

    def parse_item(self,response):
        sel=Selector(text=response.text)
        rows = sel.xpath("//div[@class='push']")
        for item in rows:
            product_name_row = item.xpath(".//div/h2//text()").getall()
            product_description_row = item.xpath(".//div/ul/li//text()").getall()

            product_name=''.join(product_name_row)
            product_description=' '.join(product_description_row)
            print(product_name)

if __name__=='__main__':
    parser=Parser()
    parser.start()