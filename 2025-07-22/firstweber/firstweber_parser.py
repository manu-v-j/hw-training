import cloudscraper
from parsel import Selector
from pymongo import MongoClient
from settings import MONGO_URI,MONGO_DB,COLLECTION,COLLECTION_DETAILS
import logging 
import json

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.data=[]
        

    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get('link')
            scraper = cloudscraper.create_scraper(browser={'browser': 'chrome', 'platform': 'windows', 'mobile': False})
            response = scraper.get(url)
            print(response.status_code)
            sel=Selector(text=response.text)
            title='sales_agent'
            office_name=''
            full_name=sel.xpath("//p[@class='rng-agent-profile-contact-name']/text()").get(default='').strip()
            name_list=full_name.split()
            if name_list:
                first_name, middle_name, last_name = "", "", ""
                if len(name_list) == 3:
                    first_name, middle_name, last_name = name_list
                elif len(name_list) == 2:
                    first_name, last_name = name_list
            address_list=sel.xpath("//li[@class='rng-agent-profile-contact-address']//text()").getall()
            if address_list:
                city_state_zip = address_list[1].split()
                city=city_state_zip[0]
                state=city_state_zip[1]
                zipcode=city_state_zip[2]
            profile_url=''
            languages="English"
            description = sel.xpath("//main[@class='rng-agent-profile-content']//p//text() | //main[@class='rng-agent-profile-content']/div/text() | //main[@class='rng-agent-profile-content']/div//text()").getall()
            website=sel.xpath("//li[@class='rng-agent-profile-contact-website']/a/@href").get()
            email=sel.xpath("//li[@class='rng-agent-profile-contact-email']/a/@href").get()
            image_url=sel.xpath("//img[@class='rng-agent-profile-photo']/@src").get()
            agent_phone_numbers=sel.xpath("//li[@class='rng-agent-profile-contact-phone']//text()").getall()
            agent_phone_numbers = ", ".join([
                phone.strip() for phone in agent_phone_numbers if phone.strip()])            
            office_phone_number=''
            social = {
                    'facebook': sel.xpath("//ul[@class='rng-agent-profile-contact']/li[@class='social-facebook']/a/@href").get(),
                    'linkedin': sel.xpath("//ul[@class='rng-agent-profile-contact']/li[@class='social-linkedin']/a/@href").get(),
                    'twitter': sel.xpath("//ul[@class='rng-agent-profile-contact']/li[@class='social-twitter']/a/@href").get()
            }
            country="United States"

            agent_data = {
                'title':title,
                'office_name':'',
                'full_name': full_name,
                'first_name': first_name,
                'middle_name': middle_name,
                'last_name': last_name,
                'address': ' '.join(address_list).strip(),
                'city': city,
                'state': state,
                'zipcode': zipcode,
                'profile_url':url,
                'languages':'English',
                'description': ' '.join(description).strip(),
                'website': website,
                'email': email,
                'image_url': image_url,
                'agent_phone_numbers': agent_phone_numbers,
                'office_phone_number':office_phone_number,
                'social': social,
                'country': "United States",
                'profile_url': url
            }
            self.data.append(agent_data)
            with open('agents_data.json', 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            print(description)

if __name__=='__main__':
    parser=Parser()
    parser.start()
