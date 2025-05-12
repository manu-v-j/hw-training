from parsel import Selector
from selenium import webdriver
from urllib.parse import urljoin
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
import re

client=MongoClient("localhost",27017)
db=client["sothebysrealty_agents"]
collection=db["agent"]

def parser(url):
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)

    try:
        driver.get(url)
        page_url=url
        agent_name =WebDriverWait(driver,5).until(EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(@class, 'Hero__agent-name')]")
        )).text
        phone_ele=driver.find_elements(By.XPATH,"//li[contains(@class,'agent-phone')]/a/span")
        phone_numbers = [el.text for el in phone_ele]
        cleaned_numbers = [re.sub(r'[^+\d.\-\s]', '', num).strip() for num in phone_numbers]
        phone = ','.join(cleaned_numbers)
        email=driver.find_element(By.XPATH,"//div[contains(@class,'agent-email')]/a").text
        try:
            language = driver.find_element(By.XPATH, "//h3[@class='agent__descrption']").text.strip()
        except:
            language = None        
        address_ele=driver.find_elements(By.XPATH,"//div[contains(@class, 'office-address')]/p")
        address=''.join([address.text for address in address_ele])
        properties=driver.find_elements(By.XPATH,"//div[contains(@class,'m-listing-item__title')]/a")
        property_hrefs=[link.get_attribute('href') for link in properties]
        
        print(agent_name,phone,email,address,property_hrefs)

        collection.insert_one({
                "Page_url":page_url,
                "Agent_name":agent_name,
                "Phone":phone,
                "Email":email,
                "Language":language,
                "Address":address,
                "Properties":property_hrefs
            
                                            
        })

    except Exception as e:
        print(f"[ERROR] Failed on {url}: {e}")

    finally:
        driver.quit()


