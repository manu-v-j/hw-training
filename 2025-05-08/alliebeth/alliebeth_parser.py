from alliebeth_crawler import Crawler
from settings import *
from parsel import Selector
import cloudscraper
from pymongo import MongoClient

client=MongoClient("localhost",27017)
db=client["alliebeth"]
collection=db["agent"]

class Parser:

    def __init__(self):
        pass

    def start(self,baseurl):
        crawler = Crawler()
        agent_links = crawler.start(baseurl)

       
        for link in agent_links:
            scraper = cloudscraper.create_scraper()  
            url = link
            response = scraper.get(url)
            if response:
                self.parse_item(response,url)

    def parse_item(self,response,url):           
        sel=Selector(response.text)

        # XPATH
        name_xpath="//div[@class='site-info-contact']/h2/text()"
        phone_xpath="//div[@class='site-info-contact']/p[2]/a/text()"
        address_xpath="//div[@class='site-info-contact']/p[last()]//text()"
        about_xpath="//div[@class='site-about-column']/div/p/text()"

        # EXTRACT
        url=url
        name=sel.xpath(name_xpath).get()
        phone=sel.xpath(phone_xpath).get()
        address=sel.xpath(address_xpath).getall()
        about=sel.xpath(about_xpath).getall()

        # CLEAN
        address = " ".join([t.strip() for t in address if t.strip()])
        about = "".join([t.strip() for t in about if t.strip()])

        collection.insert_one({
            'url':url,
            'name':name,
            'phone':phone,
            'address':address,
            'about':about,
        })


if __name__ == "__main__":
    parser=Parser()
    parser.start(baseurl)


