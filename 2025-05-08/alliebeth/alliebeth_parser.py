
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

client = MongoClient("mongodb://localhost:27017/")
db = client["alliebeth_agents"]          
collection = db["agents"]  

def parser(url):
   
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")  
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)

        name_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='site-info-contact']/h2"))
        )
        phone_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='site-info-contact']/p[2]/a"))
        )
        address_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='site-info-contact']/p[last()]"))
        )
        elements = driver.find_elements(By.XPATH, '//article[@class="int-prop"]/a')
        hrefs = [el.get_attribute('href') for el in elements]

        # about_elems = WebDriverWait(driver, 10).until(
        # EC.presence_of_all_elements_located((By.XPATH, "//div[@class='site-about-column']/div/p"))
        # )
        # about = ' '.join([elem.text.strip() for elem in about_elems])
        
        name = name_elem.text.strip()
        phone = phone_elem.text.strip()
        address = address_elem.text.strip().replace('\n', ', ')

        print("Name:", name)
        print("Phone:", phone)
        print("Address:", address)
        print("Details links:", hrefs)
        

        collection.insert_one({
            "name": name,
            "phone": phone,
            "address": address,
            "details_links": hrefs,
            "profile_url": url
        })

    except Exception as e:
        print(f"[ERROR] Failed on {url}: {e}")
    finally:
        driver.quit()

    return None
