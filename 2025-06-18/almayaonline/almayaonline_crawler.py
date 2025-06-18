import requests
from parsel import Selector
import re
from pymongo import MongoClient
from settings import base_url,headers

class Crawler:
    def __init__(self):
        pass

    def start(self):
        while True:
            response=requests.get(base_url,headers=headers)
            if response.status_code==200:
                self.parse_item(response)

    def parse_item(self,response):
            sel=Selector(text=response.text)
            product_urls=sel.xpath("//h2[@class='product-title']/a/@href").getall()
            for product in product_urls:
                url=f"https://www.almayaonline.com{product}"
                print(url)
                count+=1
                print(count)
            next_page=sel.xpath("//li[@class='next-page']/a/@href").get()
            if next_page:
                url=next_page
            else:
                break