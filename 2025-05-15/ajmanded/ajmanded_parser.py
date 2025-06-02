from curl_cffi import requests
from parsel import Selector
import logging
from pymongo import MongoClient
from settings import *

class Parser:

    def __init__(self):
        self.client=MongoClient("localhost",27017)
        self.db=self.client[DB_NAME]
        self.collection=self.db[COLLEC_DETAIL]
        
    def start(self):
        for item in self.db[COLLECTION].find():     
            url=item.get("link")
            response =  requests.get(url,impersonate="chrome", timeout=60)
            if response.status_code == 200:
                self.parse_item(url,response)

    def parse_item(self,link,response):
        selector = Selector(response.text)

        # XPATH
        license_number_xpath = "//li[@class='res-item' and span[text()='License Number']]/text()"
        license_type_xpath = "//li[@class='res-item' and span[text()='License Type']]/text()"
        legal_form_xpath = "//li[@class='res-item' and span[text()='Legal Form']]/text()"
        arabic_trade_name_xpath =  "//li[@class='res-item' and span[text()='Arabic Trade Name']]/text()"
        english_trade_name_xpath = "//li[@class='res-item' and span[text()='English Trade Name']]/text()"
        license_start_date_xpath = "//li[@class='res-item' and span[text()='License Start Date']]/text()"
        license_expiry_date_xpath = "//li[@class='res-item' and span[text()='License Expiry Date']]/text()"
        activities_xpath = "//h5[text()='Activities']/following-sibling::ul[1]/li[@class='res-item']/text()"
        est_banning_status_xpath = "//li[@class='res-item' and span[text()='Establishment Banning Status']]/text()"
        est_banning_reason_xpath="//li[@class='res-item' and span[text()='Establishment Banning Reason']]/text()"
        area_xpath = "//li[@class='res-item' and span[text()='Area']]/text()"
        building_name_xpath="//li[@class='res-item' and span[text()='Building Name']]/text()"
        block_number_xpath="//li[@class='res-item' and span[text()='Block Number']]/text()"
        unit_type_xpath="//li[@class='res-item' and span[text()='Unit Type']]/text()"

        # EXTRACT
        license_number = selector.xpath(license_number_xpath).get()
        license_type = selector.xpath(license_type_xpath).get()
        legal_form = selector.xpath(legal_form_xpath).get()
        arabic_trade_name = selector.xpath(arabic_trade_name_xpath).get()
        english_trade_name = selector.xpath(english_trade_name_xpath).get()
        license_start_date = selector.xpath(license_start_date_xpath).get()
        license_expiry_date = selector.xpath(license_expiry_date_xpath).get()
        activities = selector.xpath(activities_xpath).getall()
        est_banning_status = selector.xpath(est_banning_status_xpath).get()
        area = selector.xpath(area_xpath).get()
        est_banning_reason=selector.xpath(est_banning_reason_xpath).get()
        building_name=selector.xpath(building_name_xpath).get()
        block_number=selector.xpath(block_number_xpath).get()
        unit_type=selector.xpath(unit_type_xpath).get()

        item={}
               
        item["real_estate_link"]=link
        item["license_number"]=license_number
        item["license_type"]=license_type
        item["legal_form"]=legal_form
        item["arabic_trade_name"]=arabic_trade_name
        item["english_trade_name"]=english_trade_name
        item["license_start_date"]=license_start_date
        item["license_expiry_date"]=license_expiry_date
        item["activities"]=activities
        item["est_banning_status"]=est_banning_status
        item["area"]=area
        item["est_banning_reason"]=est_banning_reason
        item["building_name"]=building_name
        item["block_number"]=block_number
        item["unit_type"]=unit_type

        self.collection.insert_one(item)
                        
if __name__ == "__main__":
    parser=Parser()
    parser.start()
