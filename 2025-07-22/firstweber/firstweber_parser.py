from curl_cffi import requests
from parsel import Selector
from pymongo import MongoClient
from settings import MONGO_URI,MONGO_DB,COLLECTION,COLLECTION_DETAILS,headers
import logging 
import re
import json

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.all_agents=[]

    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get('link')
            # scraper = cloudscraper.create_scraper(browser={'browser': 'chrome', 'platform': 'windows', 'mobile': False})
            response = requests.get(url,impersonate='chrome')
            print(response.status_code)
            sel=Selector(text=response.text)
            title=sel.xpath("//p[small[text()='Designations']]/text()").get()
            office_name=''
            full_name=sel.xpath("//p[@class='rng-agent-profile-contact-name']/text()").get(default='').strip()
            name_list=full_name.split()
            first_name, middle_name, last_name = "", "", ""
            if name_list:
                if len(name_list) == 3:
                    first_name, middle_name, last_name = name_list
                elif len(name_list) == 2:
                    first_name, last_name = name_list

            address_list=sel.xpath("//li[@class='rng-agent-profile-contact-address']//text()").getall()
            if address_list:
                city_state_zip = address_list[1]
                print(city_state_zip)
                match = re.match(r"(.+?)\s+([A-Z]{2})\s+(\d{5})$", city_state_zip)
                if match:
                    city = match.group(1)
                    state = match.group(2)
                    zipcode = match.group(3)
                else:
                    city = state = zipcode = ""

            languages=sel.xpath("//p[@class='rng-agent-profile-languages']/text()").get() or""
            description = sel.xpath("//main[@class='rng-agent-profile-content']/div//text()").getall()
            description=' '.join([des.strip() for des in description if des.strip()])
            website=sel.xpath("//li[@class='rng-agent-profile-contact-website']/a/@href").get() or ""
            email=""
            image_url=sel.xpath("//img[@class='rng-agent-profile-photo']/@src").get() or ""
            agent_phone_numbers=sel.xpath("//li[@class='rng-agent-profile-contact-phone']//text()").getall()
            agent_phone_numbers = ", ".join([
                phone.strip() for phone in agent_phone_numbers if phone.strip()])            
            office_phone_number=''
            social = {
                    'facebook': sel.xpath("//ul[@class='rng-agent-profile-contact']/li[@class='social-facebook']/a/@href").get() or "",
                    'linkedin': sel.xpath("//ul[@class='rng-agent-profile-contact']/li[@class='social-linkedin']/a/@href").get() or "",
                    'twitter': sel.xpath("//ul[@class='rng-agent-profile-contact']/li[@class='social-twitter']/a/@href").get() or ""
            }
            country="United States"

            agent_data = {
                'title':title,
                'office_name':'',
                'first_name': first_name,
                'middle_name': middle_name,
                'last_name': last_name,
                'address': ' '.join(address_list).strip(),
                'city': city,
                'state': state,
                'zipcode': zipcode,
                'profile_url':url,
                'languages':languages,
                'description': description,
                'website': website,
                'email': email,
                'image_url': image_url,
                'agent_phone_numbers': agent_phone_numbers,
                'office_phone_number':office_phone_number,
                'social': social,
                'country': "United States",
                'profile_url': url
            }
            
            self.all_agents.append(agent_data)

            with open('agents_data.json', 'a', encoding='utf-8') as f:
                f.write(json.dumps(agent_data, ensure_ascii=False) + '\n')
            print(zipcode)


if __name__=='__main__':
    parser=Parser()
    parser.start()
