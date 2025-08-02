from parsel import Selector
from settings import *
from pymongo import MongoClient

import cloudscraper

class Crawler:
  def __init__(self):
    self.client=MongoClient(MONGO_URI)
    self.db=self.client[DB_NAME]
    self.collection=self.db[COLLECTION]

  def start(self,baseurl):
    scraper = cloudscraper.create_scraper()  
    response = scraper.get(baseurl)
    if response.status_code==200:
      self.parse_item(response)

  def parse_item(self,response):
    sel=Selector(text=response.text)
    urls=sel.xpath("//a[@class='site-roster-card-image-link']/@href").getall()
    for url in urls:
      full_url=f"https://www.alliebeth.com{url}"
      self.collection.insert_one({"link":full_url})            


if __name__=="__main__":
  crawler=Crawler()
  crawler.start(baseurl)
