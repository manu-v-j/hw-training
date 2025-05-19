from settings import *  
from parsel import Selector
from playwright.sync_api import sync_playwright
from sothebysrealty_crawler import Crawler
import re
from pymongo import MongoClient


client=MongoClient("localhost",27017)
db=client["sothebysrealty"]
collection=db["agent"]

class Parser:

    def __init__(self):
        self.mongo=''

    def start(self):

        crawler=Crawler()
        agent_link=crawler.start(baseurl)
        for link in agent_link:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)

                context = browser.new_context(user_agent=Headers["User-Agent"])

                page = context.new_page()
                page.goto(link, timeout=60000)

                page.wait_for_timeout(5000) 

                response = page.content()
                self.parse_item(link,response)

    def parse_item(self,link,response):
                sel = Selector(text=response)
                # XPATH
                phone_xpath="//li[contains(@class,'agent-phone')]/a/span/text()"
                email_xpath="//div[contains(@class,'agent-email')]/a/text()"
                language_xpath="//h3[@class='agent__descrption']/text()"
                address_xpath="//div[contains(@class, 'office-address')]/p/text()"
                property_xpath="//div[contains(@class,'m-listing-item__title')]/a/@href"

                # EXTRACT
                phone=sel.xpath(phone_xpath).getall()
                email=sel.xpath(email_xpath).get()
                language=sel.xpath(language_xpath).get()
                address=sel.xpath(address_xpath).getall()
                property=sel.xpath(property_xpath).get()

                # CLEAN
                phone= [re.sub(r'[^+\d.\-\s]', '', num).strip() for num in phone_xpath]
                address=''.join([address.strip() for address in address])

                collection.insert_one({
                     'url':link,
                     'phone':phone,
                     'email':email,
                     'address':address,
                     'property':property
                })
                

if __name__ == "__main__":
    parser=Parser()
    parser.start()
