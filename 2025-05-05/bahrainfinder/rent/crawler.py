import requests
from parsel import Selector
from urllib.parse import urljoin
from parser import parser


class Bahrainfinder:
    def __init__(self):
        self.url='https://bahrainfinder.bh/en/for-rent'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        }

    def crawler(self,max_page=10):
        for page in range(1,max_page+1):
            if page==1:
                url=self.url
            else:
                url=f"{self.url}/page/{page}/"
            response=requests.get(url,headers=self.headers)
            if response.status_code==200:
                self.parse_list_page(response.text)
               
    def parse_list_page(self,html_content):  
        selector=Selector(html_content)
        properties=selector.xpath(".//div[contains(@class,'item-wrap')]")
       
        for property in properties:
            property_link=property.xpath(".//div[@class='listing-thumb']/a/@href").get()
            pdp_response=requests.get(property_link,headers=self.headers)
            if pdp_response.status_code==200:
                parser(pdp_response.text)





obj=Bahrainfinder()
obj.crawler()

