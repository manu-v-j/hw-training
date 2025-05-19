import requests
from parsel import Selector
from dubizzle_crawler import Crawler
from settings import *
import re
from time import sleep
import random


from pymongo import MongoClient
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION]

class Parser:

    def __init__(self):
        pass

    def start(self):
        crawler=Crawler()
        links=crawler.start(baseurl_rent)
        for link in links:
            response=requests.get(link,headers=Headers)
            wait_time = random.uniform(2, 5)
            sleep(wait_time)
            self.parse_item(link,response)

    def parse_item(self,link,response):
            sel=Selector(response.text)

            # XPATH
            price_text_xpath = "//div[@aria-label='Price']/span[1]/text()"
            location_xpath="//span[@class='a1c1940e'  and @aria-label='Location']/text()"
            bathroom_xpath="//div[span[1][text()='Bathrooms']]/span[2]/text()"
            bedroom_xpath="//div[span[1][text()='Bedrooms']]/span[2]/text()"
            area_xpath="//div[span[1][text()='Area (m²)']]/span[2]/text()"
            description_xapth="//div[@aria-label='Description']//div[@class='_472bfbef']//span/text()"
            breadcrumb_xpath="//a[@class='_013e7f4b']/text()"
            image_xpath="//picture[@class='a659dd2e']/img/@src"

            # EXTRACT
            url=link
            price_text=sel.xpath(price_text_xpath).get()
            location=sel.xpath(location_xpath).get()
            bathroom=sel.xpath(bathroom_xpath).get()
            bedroom=sel.xpath(bedroom_xpath).get()
            area=sel.xpath(area_xpath).get()
            description=sel.xpath(description_xapth).get()
            breadcrumb=sel.xpath(breadcrumb_xpath).getall()
            images=sel.xpath(image_xpath).getall()

            # CLEAN
            currency, price = None, None
            if price_text:
                match = re.match(r'^([A-Z]{3})\s([\d,]+)', price_text)
                if match:
                    currency = match.group(1)
                    price = match.group(2)

            # ITEM YIELD
            
            collection.insert_one({
                
                "url": url,
                "price": price,
                "currency": currency,
                "location": location,
                "bathroom": bathroom,
                "bedroom": bedroom,
                "area": area,
                "description": description,
                "breadcrumb":breadcrumb,
                "images": images
            })

            

if __name__ == "__main__":
    parser=Parser()
    parser.start()