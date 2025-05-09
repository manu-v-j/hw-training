

from parsel import Selector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin
from webdriver_manager.chrome import ChromeDriverManager
from alliebeth_parser import parser 


def crawler(url):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")  
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

    # Setup driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "site-roster-card-image-link"))
        )

        selector = Selector(text=driver.page_source)
        agent_links = selector.xpath("//a[@class='site-roster-card-image-link']/@href").getall()

        return [urljoin(url, link) for link in agent_links]

    finally:
        driver.quit()


if __name__ == "__main__":
    result = crawler("https://www.alliebeth.com/roster/Agents/0")
    for link in result:
        parser(link)

