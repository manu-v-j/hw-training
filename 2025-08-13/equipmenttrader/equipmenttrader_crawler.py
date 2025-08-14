import requests
from parsel import Selector
from settings import headers
import json,re

class Crawler:
    def __init__(self):
        pass
    def start(self):
        category_url="https://www.equipmenttrader.com/Bucket-Truck/equipment-for-sale?category=Bucket%20Truck%7C644247024"
        min_price=1
        max_price=10000
        zip_code=23462
        
        while True:
            params = f"&price={min_price}%3A{max_price}&zip={zip_code}&radius=10000"
            url = f"{category_url}{params}&page=1"
            response=requests.get(url,headers=headers)
            sel=Selector(text=response.text)
            count=sel.xpath('//span[@class="inventory-count bold"]/text()').get()   
            count = int(count.replace(",", ""))
            count=int(count)
            print(f"{min_price}={max_price}  count : {count}")
            if count == 0:
                print("No more products available. Stopping.")
                break

            if count<=380:
                page=1

                while page<=10:
                    page_url=f"{category_url}{params}&page={page}"
                    response=requests.get(page_url,headers=headers)
                    content=self.product_item(response)
                    if not content:
                        break
                    page_no += 1

                min_price = max_price
                max_price += 10000

            else:
                max_price = (min_price + max_price) // 2

    def product_item(self,response):
        sel=Selector(text=response.text)
        product_urls = sel.xpath('//article[@class="search-card tide-display-block tide-position-relative tide-cursor-pointer tide-underline-none tide-xy-hidden bg-white"]/a/@href').getall()
        if not product_urls:
             return False
        for link in product_urls:
            full_url=f"https://www.equipmenttrader.com{link}"
            self.parse_item(full_url)
                 

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
        specification_list=sel.xpath("//h2[contains(text(),'Detailed Specifications')]/following-sibling:: div/ul/li")
        specification={}
        for item in specification_list:
            key=item.xpath(".//div/h3/span[1]/text()").get()
            value=item.xpath(".//div/h3/span[2]/text()").get()
            specification[key]=value

if __name__=='__main__':
    crawler=Crawler()
    crawler.start()