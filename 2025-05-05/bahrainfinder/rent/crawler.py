import requests
from parsel import Selector
from urllib.parse import urljoin
from parser import parser


class Bahrainfinder:
    def __init__(self):
        self.url='https://bahrainfinder.bh/en/for-rent/'

    def crawler(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        }
        response=requests.get(self.url,headers=headers)
        selector=Selector(response.text)
        properties=selector.xpath(".//div[contains(@class,'item-wrap')]")
       
        for property in properties:
            property_link=property.xpath(".//div[@class='listing-thumb']/a/@href").get()
            pdp_response=requests.get(property_link,headers=headers)
            if pdp_response.status_code==200:
                parser(pdp_response.text)





obj=Bahrainfinder()
obj.crawler()

