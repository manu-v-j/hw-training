import requests
from parsel import Selector
from settings import headers,base_url

class Category:
    def __init__(self):
        pass

    def start(self):
        response=requests.get(base_url,headers=headers)
        sel=Selector(text=response.text)
        category_urls=sel.xpath("//a[@class='itemName']/@href").getall()
        for cat in category_urls:
            full_url=f"https://www.equipmenttrader.com{cat}"
            print(full_url)

if __name__=='__main__':
    category=Category()
    category.start()
        