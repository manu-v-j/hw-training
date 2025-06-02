from settings import *  
from parsel import Selector
import requests
from urllib.parse import urljoin
from pymongo import MongoClient

class Crawler:

    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DB_NAME]
        self.collection = self.db[COLLECTION]

    def start(self, url):
        page_count = 0
        while True:
            print(f"Crawling: {url}")
            response = requests.get(url, headers=Headers)
            if response.status_code != 200:
                print(f"Failed to fetch page: {url}")
                break

            next_page_url = self.parse_item(url, response)
            if not next_page_url:
                break
            url = next_page_url
            page_count += 1

    def parse_item(self, base_url, response):
        sel = Selector(text=response.text)
        links_xpath = "//div[@class='_70cdfb32']/a/@href"
        links = sel.xpath(links_xpath).getall()

        full_urls = [urljoin(base_url, link) for link in links]

        for url in full_urls:
            self.collection.insert_one({"link": url})

        next_page = sel.xpath("//div[@title='Next']/ancestor::a/@href").get()
        next_page_url = urljoin(base_url, next_page) if next_page else None

        return next_page_url

if __name__ == "__main__":
    crawler = Crawler()
    crawler.start(baseurl_rent) 