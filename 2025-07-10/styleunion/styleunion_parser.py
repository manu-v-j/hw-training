import requests
from parsel import Selector
import re
from settings import headers,MONGO_URI,MONGO_DB,COLLECTION,COLLECTION_DETAILS
from pymongo import MongoClient
from styleunion_items import ProductItem
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
            if response.status_code==200:
                self.parse_item(response,url)

    def parse_item(self,response,url):
        sel=Selector(text=response.text)
        #XPATH
        product_name_xpath="//h1[@class='product__section-title product-title']/text()"
        regular_price_raw_xpath="//span[contains(@class, 'price-item')]/text()"    
        size_list_xpath="//label[@class='swatches__form--label']/text()"
        color_xpath="//span[@class='swatches__color-name']/text()"
        material_xpath="//div[@class='desc_inner acc__card active']//strong[text()='Fabric Type:']/following-sibling::text()"
        pattern_xpath="//div[@class='desc_inner acc__card active']//strong[text()='Pattern:']/following-sibling::text()"  
        length_xpath="//div[@class='desc_inner acc__card active']//strong[text()='Length:']/following-sibling::text()"    
        neck_style_xpath="//div[@class='desc_inner acc__card active']//strong[text()='Neck/Collar Type:']/following-sibling::text()"  
        clothing_fit_xpath="//div[@class='desc_inner acc__card active']//strong[text()='Fit:']/following-sibling::text()"
        product_description_xpath="//div[@class='acc__title'][h3[text()='Description']]/following-sibling::div[@class='acc__panel']//text()"
        care_instructions_xpath="//div[@class='acc__title'][h3[text()='Wash and Care']]/following-sibling::div[@class='acc__panel']//text()"
        image_url_xpath="//div[@class='box-ratio']/img/@src"
        product_sku_xpath="//span[@class='variant_sku']/text()"

        #EXTRACT
        product_name=sel.xpath(product_name_xpath).get()
        regular_price_raw=sel.xpath(regular_price_raw_xpath).get()
        size_list=sel.xpath(size_list_xpath).getall() 
        color=sel.xpath(color_xpath).getall()
        material=sel.xpath(material_xpath).get()
        pattern=sel.xpath(pattern_xpath).get()
        length=sel.xpath(length_xpath).get()
        neck_style=sel.xpath(neck_style_xpath).get()
        clothing_fit=sel.xpath(clothing_fit_xpath).get()
        product_description=sel.xpath(product_description_xpath).getall()
        care_instructions=sel.xpath(care_instructions_xpath).get()
        image_url=sel.xpath(image_url_xpath).getall()
        product_sku=sel.xpath(product_sku_xpath).get()
        currency='INR'

        #CLEAN
        if regular_price_raw:
            regular_price = regular_price_raw.replace('₹', '').strip()  
            regular_price = "{:.2f}".format(float(regular_price.replace(',', '')))

        size=[item.strip() for item in size_list if item.strip()]
        if material:
            material=material.strip()
        if pattern:
            pattern=pattern.strip()
        if length:
            length=length.strip()
        if neck_style:
            neck_style=neck_style.strip()
        if clothing_fit:
            clothing_fit=clothing_fit.strip()
        product_description = ' '.join(part.strip() for part in product_description if part.strip())
        if care_instructions:
            care_instructions=care_instructions.strip()
        image_url = ['https:' + url for url in image_url]

        item={}
        item['product_name']=product_name
        item['regular_price']=regular_price
        item['currency']=currency
        item['size']=size
        item['color']=color
        item['pdp_url']=url
        item['material']=material
        item['pattern']=pattern
        item['length']=length
        item['neck_style']=neck_style
        item['clothing_fit']=clothing_fit
        item['product_description']=product_description
        item['care_instructions']=care_instructions
        item['image_url']=image_url
        item['product_sku']=product_sku

        # product_item=ProductItem(**item)
        # product_item.save()

        logging.info(regular_price)

if  __name__=='__main__':
    parser=Parser()
    parser.start()