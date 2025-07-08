import requests
from parsel import Selector
from urllib.parse import urljoin
from bayut_parser import parser
from settings import headers,baseurl
import json


# class Bayut:
#     def crawler(self,url,file_name):
#         page_count=1
#         all_data=[]
#         while url :
#             print(f"Crawling page {page_count}: {url}")
#             response=requests.get("https://www.bayut.com/for-sale/apartments/dubai/",headers=headers)
#             selector=Selector(response.text)
#             list_location=selector.xpath("//a[@class='b4c99d06']/@href").getall() 
#             for link in list_location:
#                 url=urljoin(baseurl,link)
#                 print(url)

#             links = selector.xpath("//div[@class='dde89f38']/a[@class='d40f2294']/@href").getall()
#             links=set(links)
#             for link in links:
#                 if link:
#                     full_url=urljoin(baseurl,link)
#                     all_data.append(parser(full_url,headers))
#             next_page=selector.xpath("//a[@class='_95dd93c1' and @title='Next']/@href").get()
#             if next_page:
#                 url=urljoin(baseurl,next_page)
#                 page_count+=1  

            # else:
            #     None
            # self.save_to_json(all_data,file_name)

    # def save_to_json(self, all_data, filename):
    #     with open(filename,'w') as f:
    #         json.dump(all_data,f,indent=4)

            
            

# obj1=Bayut()
# obj2=Bayut()
# obj1.crawler('https://www.bayut.com/for-sale/apartments/dubai/','sale.json')
# obj2.crawler('https://www.bayut.com/to-rent/apartments/dubai/','rent.json')


# response = requests.get("https://www.bayut.com/for-sale/apartments/dubai/", headers=headers)
# selector = Selector(response.text)
# area_links = selector.xpath("//a[@class='f2067243 fontCompensation e48ccca4']/@href").getall()

# # Loop through each area
# count=0
# for area_link in area_links:
#     url = urljoin(baseurl, area_link)

#     while url:
#         print(f"Scraping: {url}")
#         response = requests.get(url, headers=headers)
#         selector = Selector(response.text)

#         # Get property links on this page
#         property_links = selector.xpath("//div[@class='dde89f38']/a/@href").getall()
#         property_links=set(property_links)
#         for link in property_links:
#             full_url = urljoin(baseurl, link)
#             count+=1
#             print(count)
#             print(full_url)

#         # Check for the next page
#         next_page = selector.xpath("//a[@class='_95dd93c1' and @title='Next']/@href").get()
#         if next_page:
#             url = urljoin(baseurl, next_page)
#         else:
#             break


price_list=["https://www.bayut.com/for-sale/apartments/dubai/?price_max=10000000","https://www.bayut.com/for-sale/apartments/dubai/?price_min=10000000&price_max=30000000",
            "https://www.bayut.com/for-sale/apartments/dubai/?price_min=3000000&price_max=10000000"]
for url in price_list:

    while True:
        print(url)
        response=requests.get(url,headers=headers)
        selector=Selector(response.text)
        list_location=selector.xpath("//a[@class='d40f2294']/@href").getall() 
        list_location=set(list_location)
        for link in list_location:
            url=urljoin(baseurl,link)
            print(url)
        next_page = selector.xpath("//a[@class='_95dd93c1' and @title='Next']/@href").get()
        if next_page:
            url = urljoin(baseurl, next_page)
        else:
            break