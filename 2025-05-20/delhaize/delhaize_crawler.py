from playwright.sync_api import sync_playwright
import time
from settings import *

class Crawler:
    def __init__(self):
        pass

    def start(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(
                proxy={"server": "http://57.129.81.201:8080"},  
            )
            context = browser.new_context(
                user_agent=headers.get("User-Agent"),
                extra_http_headers=headers,
            )
            page = context.new_page()
            page.goto(
                    "https://www.delhaize.be/nl/shop/Wijn-and-bubbels/c/v2WIN?q=%3Arelevance&sort=relevance",
                    timeout=60000,
                    wait_until="networkidle"
                )
            
        browser.close()     

if __name__ == "__main__":
    crawler = Crawler()
    crawler.start()
