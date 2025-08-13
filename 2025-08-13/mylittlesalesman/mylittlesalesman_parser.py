import requests
from parsel import Selector
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_DETAILS
import re,csv,os
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_DETAILS]
    def start(self):
        for item in self.db[COLLECTION].find().limit(200):
            url=item.get('link')
            print(url)
            response=requests.get(url,headers=headers)
            if response.status_code==200:
                self.parse_item(response)

    def parse_item(self,response):
        sel=Selector(text=response.text)
        price=''
        price_raw=sel.xpath("//span[@class='b text-darkred']/text()").get()
        if price_raw:
            price = re.sub(r"[^\d.]", "", price_raw)  
            if price:
                price = "{:.2f}".format(float(price))

        description=sel.xpath("//h2[contains(text(),'Product Description')]/following-sibling::div/text()").getall()
        description=','.join([item for item in description if item.strip()]) if description else ''

        specification_raw=sel.xpath("//h2[contains(text(),'Product Specifications')]/following-sibling:: table//tr")
        specification={}
        for row in specification_raw:
            key=row.xpath("./th/text()").get()
            value=row.xpath("./td//text()").get()
            value = value if value else ''
            specification[key]=value

        images=sel.xpath("//a[@data-fancybox='gallery']/@href").getall()
        location=sel.xpath("//h2[@class='h6 pb0']/text()").get()
        contact_info=sel.xpath("//a[@id='ctl00_ctl00_mc_mc_hypPhone']/@data-mls-tel").get()
        
        item={}
        item['price']=price
        item['description']=description
        item['specification']=specification
        item['images']=images
        item['location']=location
        item['contact_info']=contact_info

        csv_file = "mylittlesalesman_20250813.csv"
        file_exists = os.path.isfile(csv_file)
        with open(csv_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=item.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(item)

if __name__=='__main__':
    parser=Parser()
    parser.start()

