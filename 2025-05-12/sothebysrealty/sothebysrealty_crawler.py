from playwright.sync_api import sync_playwright
from parsel import Selector
from settings import *
from urllib.parse import urljoin

class Crawler:

    def __init__(self):
        pass
    def start(self, url):
        all_agent_links = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(user_agent=Headers["User-Agent"])  
            page = context.new_page()
            page_count=0

            while url and page_count<1:
                page.goto(url, timeout=60000)

                for _ in range(5):
                    page.evaluate("window.scrollBy(0, window.innerHeight)")
                    page.wait_for_timeout(10000)

                response = page.content()
                agent_links = self.parse_item(response, url)
                all_agent_links.extend(agent_links)

               
                sel = Selector(text=response)
                next_page = sel.xpath("//a[@class='pagination-item' and @aria-label='Next']/@href").get()
                url = urljoin(url, next_page) if next_page else None
                page_count+=1

            browser.close()
        return all_agent_links

    def parse_item(self, response, url):
        sel = Selector(text=response)
        links = sel.xpath("//div[@class='m-agent-item-results__card']/a/@href").getall()
        return [urljoin(url, link) for link in links]  



if __name__ == "__main__":
    crawler = Crawler()
    result = crawler.start(baseurl)  
    print(f"\nTotal agent links collected: {len(result)}")
    for link in result:
        print(link)
