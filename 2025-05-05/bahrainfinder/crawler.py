import requests
from parsel import Selector
from urllib.parse import urljoin
from parser import parser
from time import sleep
import random
import json

class Bahrainfinder:

    def __init__(self):
        self.base_url = 'https://bahrainfinder.bh/en/sale/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        }

    def crawler(self, url, output_filename):
        page_count = 1
        all_data = []
        
        while url and page_count <= 10:
            print(f"Crawling page {page_count}: {url}")
            try:
                response = requests.get(url, headers=self.headers, timeout=10)
                selector = Selector(text=response.text)
                properties = selector.xpath("//div[contains(@class,'item-wrap')]")
                for property in properties:
                    property_link = property.xpath(".//div[contains(@class,'listing-thumb')]/a/@href").get()
                    if property_link:
                        full_url = urljoin(self.base_url, property_link)
                        pdp_response = requests.get(full_url, headers=self.headers, timeout=10)
                        if pdp_response.status_code == 200:
                            all_data.append(parser(pdp_response.text))

                next_page = selector.xpath("//a[@class='page-link' and @aria-label='Next']/@href").get()
                if next_page:
                    url = urljoin(self.base_url, next_page)
                    page_count += 1
                else:
                    url = None

                sleep(random.uniform(1, 3))  

            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                url = None

        self.save_data_to_json(all_data, output_filename)

    def save_data_to_json(self, all_data, filename):
        with open(filename, 'w') as f:
            json.dump(all_data, f, indent=4)

obj1 = Bahrainfinder()
obj2 = Bahrainfinder()

obj1.crawler('https://bahrainfinder.bh/en/sale/', 'for_sale.json')

obj2.crawler('https://bahrainfinder.bh/en/for-rent/', 'for_rent.json')
