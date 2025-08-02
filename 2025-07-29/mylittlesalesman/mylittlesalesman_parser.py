import requests
from parsel import Selector
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_ERROR
import re
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_ERROR]

    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get('link')
            response=requests.get(url,headers=headers)
            if response.status_code==200:
                self.parse_item(response)
            else:
                self.collection.insert_one({'link':url})
    def parse_item(self,response):
        sel=Selector(text=response.text)

        #XPATH
        PRICE_XPATH="//span[@class='b text-darkred']/text()"
        DESCRIPTION_XPATH="//h2[contains(text(),'Product Description')]/following-sibling::div/text()"
        SPECIFICATION_ROWS_XPATH="//h2[contains(text(),'Product Specifications')]/following-sibling:: table//tr"
        IMAGES_XPATH="//a[@data-fancybox='gallery']/@href"
        LOCATION_XPATH="//h2[@class='h6 pb0']/text()"
        CONTACT_INFO_XPATH="//a[@id='ctl00_ctl00_mc_mc_hypPhone']/@data-mls-tel"

        #EXTRACT
        price_raw=sel.xpath(PRICE_XPATH).get()
        description=sel.xpath(DESCRIPTION_XPATH).getall()   
        specifications_rows=sel.xpath(SPECIFICATION_ROWS_XPATH)
        specifications={}
        for row in specifications_rows:
            key = row.xpath("./th/text()").get()
            value = row.xpath("./td//text()").get()
            specifications[key]=value
        images=sel.xpath(IMAGES_XPATH).getall()
        location=sel.xpath(LOCATION_XPATH).get()
        contact_info=sel.xpath(CONTACT_INFO_XPATH).get()

        #CLEAN
        cleaned = re.sub(r"[^\d.,]", "", price_raw)  
        price = cleaned.replace(",", "")
        if price:
            price = "{:.2f}".format(float(price))
        description=''.join([item for item in description if item.strip()])


        item={}
        item['price']=price
        item['description']=description
        item['specifications']=specifications
        item['images']=images
        item['location']=location
        item['contact_info']=contact_info

        logging.info(description)

if __name__=='__main__':
    parser=Parser()
    parser.start()