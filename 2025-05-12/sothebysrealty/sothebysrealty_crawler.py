from parsel import Selector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin
from webdriver_manager.chrome import ChromeDriverManager
from sothebysrealty_parser import parser
from settings import *


def crawler(url):
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)

    driver.get(url)
    while True:
        WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"m-agent-item-results__card"))
        )
        selector=Selector(text=driver.page_source)
        agent_links=selector.xpath("//div[@class='m-agent-item-results__card-details']/a/@href").getall()
        agents=[urljoin(url,link) for link in agent_links] 
        for agent in agents:
            parser(agent)

        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@class='pagination-item' and @title='Next']"))
            )
            driver.execute_script("arguments[0].click();", next_button)
        except:
            break




obj=crawler(baseurl)