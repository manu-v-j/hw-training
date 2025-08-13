import requests
from parsel import Selector
from settings import headers
import json

class Crawler:
    def __init__(self):
        pass
    def start(self):
        page=1
        while True:
            category_url="https://www.equipmenttrader.com/Bucket-Truck/equipment-for-sale?category=Bucket%20Truck%7C644247024"
            min_price=0
            max_price=10000
            zip_code=23462
            params = f"&price={min_price}%3A{max_price}&zip={zip_code}&radius=10000"
            url = f"{category_url}{params}&page={page}"
            response=requests.get(url,headers=headers)
            sel=Selector(text=response.text)
            product_urls = sel.xpath('//article[@class="search-card tide-display-block tide-position-relative tide-cursor-pointer tide-underline-none tide-xy-hidden bg-white"]/a/@href').getall()
            if not product_urls:
                break
            for link in product_urls:
                full_url=f"https://www.equipmenttrader.com{link}"
                self.parse_item(full_url)
            page+=1

    def parse_item(self,url):
        response=requests.get(url,headers=headers)
        sel=Selector(response.text)
        script_text=sel.xpath("//script[@data-vue-selector='ad-data']/text()").get()
        data=json.loads(script_text)
        price=data.get('price','')
        description=data.get('description','')
        image_list=data.get('photos',[])
        for image in image_list:
            images=image.get('url','')
        location=data.get('location','')
        contact_info=data.get('formattedPhone','')
        print(contact_info)

if __name__=='__main__':
    crawler=Crawler()
    crawler.start()