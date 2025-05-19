from playwright.sync_api import sync_playwright
from parsel import Selector
from urllib.parse import urljoin
from settings import *
import logging

class Crawler:

    def __init__(self):
        pass
    def start(self,url):
        agent_links = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(user_agent=headers)
            page=context.new_page()
            try:
                page.goto(url, timeout=60000, wait_until="domcontentloaded")
                page.wait_for_selector(".site-roster-card-image-link", timeout=20000)

                content = page.content()
                selector = Selector(text=content)

                agent_links = [
                    urljoin(url, link)
                    for link in selector.xpath("//a[@class='site-roster-card-image-link']/@href").getall()
                ]
            except Exception as e:
                print(f"[Error] {e}")
            finally:
                browser.close()

        return agent_links


if __name__ == "__main__":
    crawler=Crawler()
    result = crawler.start("https://www.alliebeth.com/roster/Agents/0")
    print(result)

