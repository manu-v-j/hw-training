from parsel import Selector
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright
from sothebysrealty_parser import parser
import time
from settings import *


def crawler(url):
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto(url)
        time.sleep(10)

        while True:
            page.wait_for_selector(".m-agent-item-results__card") 
            selector=Selector(text=page.content())
            agent_links = selector.xpath("//div[@class='m-agent-item-results__card-details']/a/@href").getall()
            agents = [urljoin(url, link) for link in agent_links]
            print(agents)
            # for agent in agents:
            #     parser(agent,page)
            try:
                next_button=page.query_selector("a.pagination-item[title='Next']")
                if next_button and next_button.is_enabled():
                    next_button.click()
                    time.sleep(5)
                else:
                    break
            except:
                break

        browser.close()


crawler(baseurl)
