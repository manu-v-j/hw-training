import requests
from parsel import Selector
from settings import headers,MONGO_URI,MONGO_DB,COLLECTION,COLLECTION_DETAILS
from pymongo import MongoClient
import re
from hoogvliet_items import ProductItem
import logging
logging.basicConfig(level=logging.INFO)

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_DETAILS]

    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get('link')
            response=requests.get(url,headers=headers)
            self.parse_item(response,url)

    def parse_item(self,response,url):
        if response.status_code==200:
            sel=Selector(text=response.text)

            #XPATH
            product_name_xpath="//div[@class='product-info']//h1/text()"
            regular_price_xpath="//div[@class='price-display-container']//span//text()"
            grammage_quantity_raw_xpath="//div[@class='ratio-base-packing-unit']/span//text()"
            ingredients_xpath="//h3[contains(text(), 'Ingredi')]/ancestor::div[@class='accordion-item open']//div[@class='accordion-content']/p/text()"
            storage_instructions_xpath = "//h3[contains(text(), 'Bewaar en/of gebruiksadvies')]/ancestor::div[@class='accordion-item']//div[@class='accordion-content']/p/text()"
            country_of_origin_xpath="//h3[contains(text(), 'Land van herkomst:')]/ancestor::div[@class='accordion-item']//div[@class='accordion-content']/p/text()"
            distributor_address_xpath="//h3[contains(text(), 'Leverancier:')]/ancestor::div[@class='accordion-item']//div[@class='accordion-content']/p/text()"
            nutritions_rows_xpath="//div[@class='accordion-content nutritional-info']//tr"    
            image_url_xpath="//div[@class='product-image-container']/img/@src"
            breadcrumbs_raw_xpath="//li[contains(@class,'breadcrumbs-list')]//text()"
            
            #EXTRACT
            product_name=sel.xpath(product_name_xpath).get()
            regular_price=sel.xpath(regular_price_xpath).getall()
            currency='Euro'
            grammage_quantity_raw=sel.xpath(grammage_quantity_raw_xpath).get()
            ingredients=sel.xpath(ingredients_xpath).get()
            storage_instructions=sel.xpath(storage_instructions_xpath).get()
            country_of_origin=sel.xpath(country_of_origin_xpath).get()
            distributor_address=sel.xpath(distributor_address_xpath).get()
            nutritions_rows=sel.xpath(nutritions_rows_xpath)
            image_url=sel.xpath(image_url_xpath).get()
            breadcrumbs_raw=sel.xpath(breadcrumbs_raw_xpath).getall()

            #CLEAN
            if product_name:
                product_name=product_name.strip()

            regular_price = ''.join(regular_price)

            if country_of_origin:
                country_of_origin=country_of_origin.strip()

            grammage_quantity=''
            grammage_unit=''
            if grammage_quantity_raw:
                cleaned_text = re.sub(r'\bCa\.\s*', '', grammage_quantity_raw).strip()
                match = re.match(r'(\d+)\s*(\w+)', cleaned_text)
                if match:
                    grammage_quantity = match.group(1)
                    grammage_unit = match.group(2)
            if ingredients:
                ingredients = re.sub(r'\s+', ' ', ingredients).strip()
            nutritions={}
            for row in nutritions_rows:
                    label = row.xpath(".//td[1]/text()").get().strip()
                    value = row.xpath(".//td[2]/text()").get().strip()
                    nutritions[label]=value
            breadcrumbs = [item.strip() for item in breadcrumbs_raw if item.strip() and item.strip() != '/']

            item={}
            item['product_name']=product_name
            item['regular_price']=regular_price
            item['currency']=currency
            item['grammage_quantity']=grammage_quantity
            item['grammage_unit']=grammage_unit
            item['ingredients']=ingredients
            item['pdp_url']=url
            item['storage_instructions']=storage_instructions
            item['country_of_origin']=country_of_origin
            item['distributor_address']=distributor_address
            item['nutritions']=nutritions
            item['image_url']=image_url
            item['breadcrumbs']=breadcrumbs

            product_item=ProductItem(**item)
            product_item.save()


if __name__=='__main__':
    parser=Parser()
    parser.start()