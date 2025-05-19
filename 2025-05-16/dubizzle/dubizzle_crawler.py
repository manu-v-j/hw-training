from settings import *  
from parsel import Selector
import requests
from urllib.parse import urljoin

class Crawler:

    def __init__(self):
        pass

    def start(self, url):
        product_links = []
        page_count = 0
        while url and page_count < 2:
            print(f"Crawling: {url}")
            response = requests.get(url, headers=Headers)
            if response.status_code != 200:
                print(f"Failed to fetch page: {url}")
                break
            
            links, next_page_url = self.parse_item(url, response)
            product_links.extend(links)
            url = next_page_url
            page_count += 1

        return product_links

    def parse_item(self, url, response):
        sel = Selector(text=response.text)
        links_xpath = "//div[@class='_70cdfb32']/a/@href"
        links = sel.xpath(links_xpath).getall()
        full_links = [urljoin(url, link) for link in links]

        next_page = sel.xpath("//div[@title='Next']/ancestor::a/@href").get()
        next_page_url = urljoin(url, next_page) if next_page else None

        return full_links, next_page_url

if __name__ == "__main__":
    crawler = Crawler()
    product_links = crawler.start(baseurl_rent)
    for link in product_links:
        print(link)
