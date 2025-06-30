import requests
from parsel import Selector
import re
from settings import headers,MONGO_URI,MONGO_DB,COLLECTION,COLLECTION_ERROR
from pymongo import MongoClient
from hm_items import ProductItem
import logging
logging.basicConfig(level=logging.INFO)

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection_error=self.db[COLLECTION_ERROR]

    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get("link","")
            response=requests.get(url,headers=headers)
            if response.status_code==200:
                sel=Selector(text=response.text)
            else:
                self.collection_error.insert_one({'link':url})
            # XPATH
            product_name_xpath="//h1[@class='fe9348 bdb3fa d582fb']/text()"
            regular_price_raw_xpath="//span[@class='e70f50 d7cab8 d9ca8b']/text()"
            product_description_xpath="//p[@class='e95b5c f8c1e9 e2b79d']/text()"
            pdp_url=url
            size_xpath="//div[@class='ecc0f3']/dt[contains(text(), 'Size')]/following-sibling::dd/text()"
            clothing_length_xpath="//div[@class='ecc0f3']/dt[contains(text(), 'Length: ')]/following-sibling::dd/text()"
            clothing_fit_xpath="//div[@class='ecc0f3']/dt[contains(text(), 'Fit: ')]/following-sibling::dd/text()"
            style_xpath="//div[@class='ecc0f3']/dt[contains(text(), 'Style: ')]/following-sibling::dd/text()"
            neck_style_xpath="//div[@class='ecc0f3']/dt[contains(text(), 'Neckline: ')]/following-sibling::dd/text()"
            country_of_origin_xpath="//div[@class='ecc0f3']/dt[contains(text(), 'Neckline: ')]/following-sibling::dd/text()"
            manufacturer_address_xpath="//div[@class='ecc0f3']/dt[contains(text(), 'Manufactured by: ')]/following-sibling::dd/text()"
            importer_address_xpath="//div[@class='ecc0f3']/dt[contains(text(), 'Marketed or imported by: ')]/following-sibling::dd/text()"
            material_composition_xpath="//li[@class='d9d00c']/span/text()"
            material_xpath="//div[@class='ecc0f3']/dt[contains(text(), 'Material: ')]/following-sibling::dd/text()"
            care_instructions_xpath="//li[@class='e16073 fdbaf2']/text()"
            image_url_xpath="//div[@class='def5f0 fcc68c a33b36 f6e252']/span/img/@src"

            # EXTRACT
            product_name=sel.xpath(product_name_xpath).get()
            regular_price_raw=sel.xpath(regular_price_raw_xpath).get()
            product_description=sel.xpath(product_description_xpath).get()
            size=sel.xpath(size_xpath).getall()
            clothing_length=sel.xpath(clothing_length_xpath).get()
            clothing_fit=sel.xpath(clothing_fit_xpath).get()
            style=sel.xpath(style_xpath).get()
            neck_style=sel.xpath(neck_style_xpath).get()
            country_of_origin=sel.xpath(country_of_origin_xpath).get()
            manufacturer_address=sel.xpath(manufacturer_address_xpath).get()
            importer_address=sel.xpath(importer_address_xpath).get()
            material_composition=sel.xpath(material_composition_xpath).get()
            material=sel.xpath(material_xpath).get()
            care_instructions=sel.xpath(care_instructions_xpath).getall()
            image_url=sel.xpath(image_url_xpath).getall()

            # CLEAN
            regular_price=regular_price_raw.replace('Rs.','')
            if regular_price:
                regular_price=regular_price.strip()
            currency=re.search(r'Rs',regular_price_raw).group()

            item={}
            item['product_name']=product_name
            item['regular_price']=regular_price
            item['currency']=currency
            item['product_description']=product_description
            item['pdp_url']=pdp_url
            item['size']=size
            item['clothing_length']=clothing_length
            item['clothing_fit']=clothing_fit
            item['style']=style
            item['neck_style']=neck_style
            item['country_of_origin']=country_of_origin
            item['manufacturer_address']=manufacturer_address
            item['importer_address']=importer_address
            item['material_composition']=material_composition
            item['material']=material
            item['care_instructions']=care_instructions
            item['image_url']=image_url

            product_item=ProductItem(**item)
            product_item.save()

if __name__=='__main__':
    parser=Parser()
    parser.start()
