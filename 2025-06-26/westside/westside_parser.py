import requests
from parsel import Selector
from settings import headers,MONGO_URI,MONGO_DB,COLLECTION,COLLECTION_DETAILS
from pymongo import MongoClient
from westside_items import ProductItem
import re
import logging
logging.basicConfig(level=logging.INFO)

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_DETAILS]

    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get('link','')
            response=requests.get(url,headers=headers)
            if response.status_code==200:
                self.parse_item(response,url)

    def parse_item(self,response,url):
        sel=Selector(text=response.text)

        # XPATH
        product_name_xpath="//div[@class='product__title']/h1/text()"
        brand_xpath="//p[@class='product__text inline-richtext caption-with-letter-spacing']/text()"
        regular_price_raw_xpath="//span[@class='price-item price-item--regular']/text()"
        breadcrumb_xpath="//li[@class='breadcrumbs__item']/a/text()"
        color_xpath="//div[@class='tooltip']/text()"
        product_description_xpath="//div[@class='features_discription']/p/text()"
        country_of_origin_xpath="//div[@class='features' and b[text()='Country Of Origin:']]/text()[2]"
        instructions_xpath="//div[@class='features' and b[text()='Care Instruction:']]/text()[2]"
        material_composition_xpath="//div[@class='features' and b[text()='Fabric Composition:']]/text()[2]"
        size_xpath="//label[@class='product_clr_variant' and @id='pdp-variant']/text()"
        image_urls_xpath="//div[@class='product__media media media--transparent']/img/@src"
        fit_guide_xpath="//div[@class='features' and b[text()='Model Fit:']]/text()[2]"
        body_fit_xpath="//div[@class='features' and b[text()='Fit:']]/text()[2]"
        product_sku_xpath="//div[@class='features' and b[text()='SKU:']]/text()[2]"
        manufacturer_address_xpath="//div[@class='features' and b[text()='Manufactured and Marketed By:']]/p/text()"
        product_dimensions_xpath="//div[@class='features' and b[text()='Dimensions:']]/text()[2]"
        product_quantity_xpath="//div[@class='features' and b[text()='Net Quantity:']]/text()[2]"

        # EXTRACT
        product_name=sel.xpath(product_name_xpath).get()
        brand=sel.xpath(brand_xpath).get()
        regular_price_raw=sel.xpath(regular_price_raw_xpath).get()
        breadcrumb=sel.xpath(breadcrumb_xpath).getall()
        color=sel.xpath(color_xpath).getall()
        product_description=sel.xpath(product_description_xpath).get()
        country_of_origin=sel.xpath(country_of_origin_xpath).get()
        instructions=sel.xpath(instructions_xpath).get()
        material_composition=sel.xpath(material_composition_xpath).get()
        size=sel.xpath(size_xpath).getall()
        image_urls=sel.xpath(image_urls_xpath).getall()
        fit_guide=sel.xpath(fit_guide_xpath).get()
        body_fit=sel.xpath(body_fit_xpath).get()
        product_sku=sel.xpath(product_sku_xpath).get()
        manufacturer_address=sel.xpath(manufacturer_address_xpath).get()
        product_dimensions=sel.xpath(product_dimensions_xpath).get()
        product_quantity=sel.xpath(product_quantity_xpath).get()
        pdp_url=url

        # CLEAN
        if regular_price_raw:
            regular_price_raw=regular_price_raw.strip()

        regular_price=regular_price_raw.replace('₹','').strip()
        currency= re.search(r"[^\d\s.,]+", regular_price_raw).group()

        if country_of_origin:
            country_of_origin=country_of_origin.strip()

        if instructions:
            instructions=instructions.strip()

        if material_composition:
            material_composition=material_composition.strip()

        if fit_guide:
            fit_guide=fit_guide.strip()

        if body_fit:
            body_fit=body_fit.strip()

        if product_sku:
            product_sku=product_sku.strip()

        if product_dimensions:
            product_dimensions=product_dimensions.strip()

        if product_quantity:
            product_quantity=product_quantity.strip()

        item={}
        item['product_name']=product_name
        item['brand']=brand
        item['regular_price']=regular_price
        item['currency']=currency
        item['breadcrumb']=breadcrumb
        item['color']=color
        item['product_description']=product_description
        item['country_of_origin']=country_of_origin
        item['instructions']=instructions
        item['material_composition']=material_composition
        item['size']=size
        item['image_urls']=image_urls
        item['pdp_url']=pdp_url
        item['fit_guide']=fit_guide
        item['body_fit']=body_fit
        item['product_sku']=product_sku
        item['manufacturer_address']=manufacturer_address
        item['product_dimensions']=product_dimensions
        item['product_quantity']=product_quantity


        product_item=ProductItem(**item)
        product_item.save()
        logging.info(item)

if __name__=='__main__':
    parser=Parser()
    parser.start()