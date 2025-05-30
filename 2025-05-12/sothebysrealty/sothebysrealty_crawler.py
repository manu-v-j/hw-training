from curl_cffi import requests  
from parsel import Selector
from pymongo import MongoClient
from urllib.parse import urljoin
from settings import *
import json


class Crawler:
    def __init__(self):
        self.clint=MongoClient(MONGO_URI)
        self.db=self.clint[DB_NAME]
        self.collection=self.db[COLLECTION]
        
    def start(self, baseurl):
        url=baseurl
        while url:
            response = requests.get(url, headers=headers, cookies=cookies, impersonate="chrome")
            if response.status_code != 200:
                print(f"Failed to fetch {url} - status code {response.status_code}")
                break
            next_url=self.parse_item(response)
            url=next_url
    def parse_item(self, response):    
        sel = Selector(response.text)
        content = sel.xpath('//script[@id="__NEXT_DATA__" and @type="application/json"]/text()').get()

        content_json = json.loads(content)
        modules = content_json.get("props", {}).get("pageProps", {}).get("initialState", {}).get("PageStore", {}).get("modules", [])
        
        for module in modules:
            if module.get("moduleName") == "agentitem":
                agent_data = module.get("legacyData", {}).get("result", {}).get("agent", [])
                agent_list = agent_data if isinstance(agent_data, list) else [agent_data]
                
                for agent_attrs in agent_list:
                    canonical_data = agent_attrs.get("canonicalurldata", {})
                    items = canonical_data.get("item", [])
                    if items:
                        item = items[0]
                        url = item.get("_attributes", {}).get("url")
                        if url:
                            self.collection.insert_one({"link": url} )

    
        next_page = sel.xpath('//a[@class="pagination-item" and @aria-label="Next"]/@href').get()
        if next_page:
            return urljoin(baseurl, next_page)
        return None


if __name__ == "__main__":
    crawler = Crawler()
    result = crawler.start(baseurl)  