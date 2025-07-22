# import cloudscraper
from curl_cffi import requests
import json
from parsel import Selector
from pymongo import MongoClient
from settings import MONGO_URI,MONGO_DB,COLLECTION,headers
from pymongo.errors import DuplicateKeyError
import logging
logging.basicConfig(level=logging.INFO)
class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]
        self.collection.create_index('link',unique=True)

    def start(self):
        url = 'https://www.firstweber.com/CMS/CmsRoster/RosterSearchResults?layoutID=1126&pageSize=10&pageNumber=0&sortBy=firstname'
        # scraper = cloudscraper.create_scraper(browser={'browser': 'chrome', 'platform': 'windows', 'mobile': False})
        # response = scraper.get(url,headers=headers)
        response=requests.get(url,headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            self.parse_item(response,scraper)
    def parse_item(self,response,scraper):
        data = response.json() 
        data = json.loads(data) 
        html_data = data.get("Html", "")
        sel = Selector(text=html_data)
        agent_links=sel.xpath("//article[@class='rng-agent-roster-agent-card js-sort-item']/a/@href").getall()
        agent_links=set(agent_links)
        for url in agent_links:
            full_url=f"https://www.firstweber.com{url}"
            print(full_url)
            response = scraper.get(full_url)
            sel=Selector(text=response.text)
            agent_link=sel.xpath("//article[@class='rng-agent-roster-agent-card js-sort-item']/a/@href").getall()
            for url in agent_link:
                try:
                    full_url=f"https://www.firstweber.com{url}"
                    # self.collection.insert_one({'link':full_url})
                    # print(full_url)
                except DuplicateKeyError:
                    logging.debug(f"Duplicate skipped: {full_url}")

    

if __name__=='__main__':
    crawler=Crawler()
    crawler.start()