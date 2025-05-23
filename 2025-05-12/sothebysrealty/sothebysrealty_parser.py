
from settings import *
import requests
from parsel import Selector
import re
from pymongo import MongoClient

class Parser:

    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DB_NAME]
        self.collection = self.db[COLLEC_DETAIL]



    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get("link")
            print(url)
            response = requests.get(url, headers=headers, cookies=cookies)
            self.parse_item(response,url)

    def parse_item(self, response,link):
        sel = Selector(text=response.text)  


        # XPATH
        name_xpath="//h1[@class='Hero__agent-name']/text()"
        phone_xpath="//li[contains(@class,'agent-phone')]/a/span/text()"
        email_xpath="//div[contains(@class,'agent-email')]/a/text()"
        language_xpath="//h3[@class='agent__descrption']/text()"
        address_xpath="//div[contains(@class, 'office-address')]/p/text()"
        property_xpath="//div[contains(@class,'m-listing-item__title')]/a/@href"

        # # EXTRACT
        name=sel.xpath(name_xpath).get()
        phone=sel.xpath(phone_xpath).getall()
        email=sel.xpath(email_xpath).get()
        language=sel.xpath(language_xpath).get()
        address=sel.xpath(address_xpath).getall()
        properties=sel.xpath(property_xpath).get()

        # # CLEAN
        phone= [re.sub(r'[^+\d.\-\s]', '', num).strip() for num in phone]
        address=''.join([address.strip() for address in address])

        self.collection.insert_one({
            'name':name,
            'url':link,
            'phone':phone,
            'email':email,
            'language':language,
            'address':address,
            'properties':properties
            })
                

if __name__ == "__main__":
    parser=Parser()
    parser.start()