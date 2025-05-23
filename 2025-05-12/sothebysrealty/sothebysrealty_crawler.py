from playwright.sync_api import sync_playwright
from parsel import Selector
from settings import *
from urllib.parse import urljoin
from pymongo import MongoClient

class Crawler:

    def __init__(self):
        self.clint=MongoClient(MONGO_URI)
        self.db=self.clint[DB_NAME]
        self.collection=self.db[COLLECTION]
    def start(self, url):

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(user_agent=headers["User-Agent"])  
            page = context.new_page()
            page_count=0

            while url and page_count<11:
                page.goto(url, timeout=60000)

                for _ in range(5):
                    page.evaluate("window.scrollBy(0, window.innerHeight)")
                    page.wait_for_timeout(10000)

                response = page.content()
                url,links=self.parse_item(response, url)
                self.collection.insert_many([{"link": link} for link in links])
               
                page_count+=1

            browser.close()

    def parse_item(self, response, url):
        sel = Selector(text=response)
        links = sel.xpath("//div[@class='m-agent-item-results__card']/a/@href").getall()
        links=[urljoin(url, link) for link in links]

        next_page = sel.xpath("//a[@class='pagination-item' and @aria-label='Next']/@href").get()
        url = urljoin(url, next_page) if next_page else None

        return url,links
    
         

if __name__ == "__main__":
    crawler = Crawler()
    result = crawler.start(baseurl)  
    

# from curl_cffi import requests  
# from parsel import Selector

# baseurl = "https://www.sothebysrealty.com/eng/associates/int"


# headers = {
#     "accept": "*/*",
#     "accept-encoding": "gzip, deflate, br, zstd",
#     "accept-language": "en-US,en;q=0.9",
#     "referer": "https://www.sothebysrealty.com/eng/associates/int",
#     "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
#     "sec-ch-ua-mobile": "?1",
#     "sec-ch-ua-platform": '"Android"',
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
# }

# cookies = {
#     "LanguagePreference": "eng",
#     "_gcl_au": "1.1.294586184.1747023417",
#     "_ga": "GA1.1.389935457.1747023417",
#     "_fbp": "fb.1.1747023420697.994819225374127257",
#     "notice_preferences": "2:",
#     "notice_gdpr_prefs": "0,1,2:",
#     "cmapi_gtm_bl": "",
#     "cmapi_cookie_privacy": "permit 1,2,3",
#     "LastLocationGetter": '{"data":{"SeoPart":"/int"}}',
#     "notice_behavior": "implied,us",
#     "ASP.NET_SessionId": "posgb1hsdpel1olvoyn4ldkn",
#     "userLocation": "nld",
#     "userLocationName": "Netherlands",
#     "_ga_07J12X0FK6": "GS2.1.s1747902307$o26$g0$t1747902307$j60$l0$h0$dVeWZWkrgHOE8p3k2lQrzlOt0s45lRc9-bA",
#     "aws-waf-token": "9e743767-d51f-4ed0-ae4f-58a9d7373872:BgoAmmo6JzlQAAAA:4PxBCunVgBTp27yV0Vdr72XC8VBKihAgW3RNsD9mcGg6e1eQw6EE0+SqAZpR9Lr/fbo/miQFMWIRJ8t4yb6qe0dQDjVm+DAgt3cUbYNVe+7bz+k5hON0XRT5Hwp+Y3tgBTZ7q56b2z09Mh7fApde4xNW+jpmJQCImjH8luhT0bT/ffrA2jkAy+9P03YMRjedjdBjX0E="
# }

# import json
# response = requests.get(baseurl, headers=headers, cookies=cookies, impersonate="chrome")

# if response.status_code == 200:
#     with open('result.json', 'w', encoding='utf-8') as f:
#         json.dump({"html": response.text}, f, indent=2)   
# else:
#     print(f"Request failed with status code {response.status_code}")
