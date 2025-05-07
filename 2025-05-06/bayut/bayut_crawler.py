import requests
from parsel import Selector
from urllib.parse import urljoin
from bayut_parser import parser
from settings import headers,baseurl
import json


class Bayut:
    def crawler(self,url,file_name):
        page_count=1
        all_data=[]
        while url and page_count<=10:
            print(f"Crawling page {page_count}: {url}")
            response=requests.get(url,headers=headers)
            selector=Selector(response.text)
            links = selector.xpath("//div[@class='dde89f38']/a[@class='d40f2294']/@href").getall()
            links=set(links)
            for link in links:
                if link:
                    full_url=urljoin(baseurl,link)
                    all_data.append(parser(full_url,headers))
            next_page=selector.xpath("//a[@class='_95dd93c1' and @title='Next']/@href").get()
            if next_page:
                url=urljoin(baseurl,next_page)
                page_count+=1  

            else:
                None
            self.save_to_json(all_data,file_name)

    def save_to_json(self, all_data, filename):
        with open(filename,'w') as f:
            json.dump(all_data,f,indent=4)

            
            

obj1=Bayut()
obj2=Bayut()
obj1.crawler('https://www.bayut.com/for-sale/apartments/dubai/','sale.json')
obj2.crawler('https://www.bayut.com/to-rent/apartments/dubai/','rent.json')