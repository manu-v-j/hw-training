from settings import *
from parsel import Selector
import requests
from urllib.parse import urljoin
import re

class Crawler:

    def __init__(self):
        self.mongo=''

    
    def start(self,url):
        response=requests.get(url,headers=Headers)
        sel=Selector(response.text)
        products=sel.xpath("//article[@class='_63a946ba']")
        for product in products:
            product_url=product.xpath(".//div[@class='_70cdfb32']/a/@href").get()
            full_url=urljoin(url,product_url)
            print(full_url)
            price_text=product.xpath(".//div[@aria-label='Price']/span[1]/text()").get()
            match = re.match(r'^([A-Z]{3})\s([\d,]+)', price_text)
            if match:
                currency = match.group(1)  
                price = match.group(2)

            next_page=sel.xpath("//div[@title='Next']/ancestor::a/@href").get()
            if next_page:
                full_url=urljoin(url,next_page)
                self.start(full_url)
            else:
                break

    def parse_item(self,response,url):
        sel=Selector(response.text)
        products=sel.xpath("//article[@class='_63a946ba']")
        for product in products:
            product_url=product.xpath(".//div[@class='_70cdfb32']/a/@href").get()
            full_url=urljoin(url,product_url)
            print(full_url)
            price_text=product.xpath(".//div[@aria-label='Price']/span[1]/text()").get()
            match = re.match(r'^([A-Z]{3})\s([\d,]+)', price_text)
            if match:
                currency = match.group(1)  
                price = match.group(2)






if __name__=="__main__":
    crawler = Crawler()
    crawler.start(baseurl_rent)
    
