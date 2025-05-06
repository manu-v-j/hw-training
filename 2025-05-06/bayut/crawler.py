import requests
from parsel import Selector
from urllib.parse import urljoin
from parser import parser

class Bayut:
    def __init__(self):
        self.baseurl='https://www.bayut.com/for-sale/apartments/dubai/'
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        }

    def crawler(self,url):
        page_count=1
        all_data=[]
        while url and page_count<2:
            response=requests.get(url,headers=self.headers)
            selector=Selector(response.text)
            links = selector.xpath("//div[@class='dde89f38']/a[@class='d40f2294']/@href").getall()
            links=set(links)
            for link in links:
                if link:
                    full_url=urljoin(self.baseurl,link)
                    parser(full_url,self.headers)

obj=Bayut()
obj.crawler('https://www.bayut.com/for-sale/apartments/dubai/')