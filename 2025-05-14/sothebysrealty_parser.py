from parsel import Selector
from playwright.sync_api import sync_playwright
import re
from urllib.parse import urljoin

def parser(url,page):
    page.goto(url,timeout=15000)
    
    page.wait_for_selector("h1.Hero__agent-name")
    content=page.content()
    selector=Selector(text=content)
    agent_name=selector.xpath("//h1[contains(@class, 'Hero__agent-name')]/text()").get()
    phone_numbers = selector.xpath("//li[contains(@class,'agent-phone')]/a/span/text()").getall()
    cleaned_numbers=[re.sub(r'[^+\d.\-\s]','',num).strip() for num in phone_numbers]
    phone=','.join(cleaned_numbers)
    email=selector.xpath("//div[contains(@class,'agent_email')]/a/text()").get()
    language=selector.xpath("//h3[@class='agent__descrption']/text()").get()
    language=language.strip()if language else None
    address_parts = selector.xpath("//div[contains(@class, 'office-address')]/p/text()").getall()
    address = ''.join([part.strip() for part in address_parts])
    property=selector.xpath("//div[contains(@class,'m-listing-item__title')]/a/@href").getall()
    

    print(agent_name, phone, email, address,property)


        
