from playwright.sync_api import sync_playwright
from settings import *

class Crawler:
    def __init__(self):
        pass
    def start(self,url):
        detail_urls = []  

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
                        detail_urls.append(full_url)  
                        
                except Exception as e:
                    print(f"Failed to get href for link {i}: {e}")

            browser.close()
        
        return detail_urls 

if __name__ == "__main__":
    crawler=Crawler()
    url=crawler.start(baseurl)
    print(url)