import cloudscraper
from parsel import Selector
agent_url=[]
from pymongo import MongoClient
import logging 
from
scraper = cloudscraper.create_scraper(browser={'browser': 'chrome', 'platform': 'windows', 'mobile': False})
url='https://www.firstweber.com/bio/sanelbajramovic'
response = scraper.get(url)
print(response.status_code)
sel=Selector(text=response.text)
title=''
office_name=''
full_name=sel.xpath("//p[@class='rng-agent-profile-contact-name']/text()").get()
name_list=full_name.split()
first_name, middle_name, last_name = "", "", ""
if len(name_list) == 3:
    first_name, middle_name, last_name = name_list
elif len(name_list) == 2:
    first_name, last_name = name_list
address_list=sel.xpath("//li[@class='rng-agent-profile-contact-address']//text()").getall()
city_state_zip = address_list[1].split()
city=city_state_zip[0]
state=city_state_zip[1]
zipcode=city_state_zip[2]
profile_url=''
languages="English"
description=sel.xpath("//div[@id='widget-text-1-preview-5503-5079655']//text()").getall()
website=sel.xpath("//li[@class='rng-agent-profile-contact-website']/a/@href").get()
email=sel.xpath("//li[@class='rng-agent-profile-contact-email']/a/@href").get()
image_url=sel.xpath("//img[@class='rng-agent-profile-photo']/@src").get()
agent_phone_numbers=sel.xpath("//li[@class='rng-agent-profile-contact-phone']//text()").getall()
office_phone_number=''
social={}
facebook=sel.xpath("//ul[@class='rng-agent-profile-contact']/li[@class='social-facebook']/a/@href").get()
social['facebook']=facebook
linkdin=sel.xpath("//ul[@class='rng-agent-profile-contact']/li[@class='social-linkedin']/a/@href").get()
social['linkdin']=linkdin
twitter=sel.xpath("//ul[@class='rng-agent-profile-contact']/li[@class='social-twitter']/a/@href").get()
social['twitter']=twitter
country="United States"
