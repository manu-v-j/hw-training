
from playwright.sync_api import sync_playwright

def parser(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        try:
            page.goto(url, timeout=30000)
            page.wait_for_timeout(5000) 

        
            name_xpath = "//div[@class='site-info-contact']/h2"
            phone_xpath = "//div[@class='site-info-contact']/p[2]/a"

       
            name = page.locator(f"xpath={name_xpath}").text_content(timeout=10000)
            phone = page.locator(f"xpath={phone_xpath}").text_content(timeout=10000)

            print("Name:", name.strip())
            print("Phone:", phone.strip())

        except Exception as e:
            print(f"[ERROR] Failed on {url}: {e}")
        finally:
            browser.close()
    return None

