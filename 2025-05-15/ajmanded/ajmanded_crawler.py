from playwright.sync_api import sync_playwright
from settings import *
from pymongo import MongoClient

class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[DB_NAME]
        self.collection=self.db[COLLECTION]
    def start(self,url):

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=100)
            page = browser.new_page()
            page.goto(url)
            page.wait_for_selector(".selectize-control")

            page.click(".selectize-control")
            page.click("div[data-value='N']")

            page.wait_for_selector("#LicenseTradeName", state="visible")
            page.fill("#LicenseTradeName", "realestate")

            print("Please solve the CAPTCHA manually in the browser.")
            input("Press ENTER after solving CAPTCHA...")

            page.click("button[type='submit']")      
            page.wait_for_url("**/TradeLicense/Search**", timeout=15000)
            print(f"Navigated to: {page.url}")     

            view_links = page.locator("//a[contains(@class, 'btn-view')]")
            count = view_links.count()
            print(f"Found {count} detail links")

            for i in range(count):
                link = view_links.nth(i)
                try:
                    href = link.get_attribute("href")
                    if href:
                        full_url = f"https://eservices.ajmanded.ae{href}"
                        self.collection.insert_one({"link":full_url})
                        
                except Exception as e:
                    print(f"Failed to get href for link {i}: {e}")

            browser.close()
        
         

if __name__ == "__main__":
    crawler=Crawler()
    url=crawler.start(baseurl)
    print(url)