import requests
from parsel import Selector
from crawler import crawler
import json


class Lidlespider:
    def __init__(self):
        self.url = 'https://sortiment.lidl.ch/de/brot-backwaren#/'
        self.productdata = []

    def parser(self):
        response = requests.get(self.url)
        selector = Selector(response.text)
        products = selector.xpath("//div[@class='product-item-info']")

        for product in products:
            product_url = product.xpath(".//a/@href").get()
            if product_url:
                item = self.crawler(product_url)
                if item:
                    self.productdata.append(item)

        self.save_to_json()

    def crawler(self, url):
        data = crawler(url)
        if data:
            return data

    def save_to_json(self):
        with open('output.json', 'w', encoding='utf-8') as f:
            json.dump(self.productdata, f, ensure_ascii=False, indent=4)



spider = Lidlespider()
spider.parser()  
