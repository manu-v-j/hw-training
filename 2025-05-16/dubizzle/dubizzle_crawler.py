from settings import *  
from parsel import Selector
import requests
from urllib.parse import urljoin
import re

class Crawler:

    def __init__(self):
        self.mongo = ''  

    def start(self, url):
        product_links = []
        while url:
            print(f"Crawling: {url}")
            response = requests.get(url, headers=Headers)
            sel = Selector(response.text)
            products = sel.xpath("//article[@class='_63a946ba']")
            for product in products:
                product_url = product.xpath(".//div[@class='_70cdfb32']/a/@href").get()
                if product_url:
                    full_url = urljoin(url, product_url)
                    product_links.append(full_url)
                    self.parse_item(full_url)

            # Uncomment for pagination:
            # next_page = sel.xpath("//div[@title='Next']/ancestor::a/@href").get()
            # if next_page:
            #     url = urljoin(url, next_page)
            # else:
            #     break

            break  

        return product_links

    def parse_item(self, url):
        response = requests.get(url, headers=Headers)
        if response.status_code != 200:
            print(f"Failed to fetch product page: {url}")
            return

        sel = Selector(response.text)
        price_text = sel.xpath("//div[@aria-label='Price']/span[1]/text()").get()
        currency, price = None, None
        if price_text:
            match = re.match(r'^([A-Z]{3})\s([\d,]+)', price_text)
            if match:
                currency = match.group(1)
                price = match.group(2)

if __name__ == "__main__":
    crawler = Crawler()
    product_links = crawler.start(baseurl_rent)
    for link in product_links:
        print(link)
