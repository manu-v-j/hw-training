import requests
from parsel import Selector
from settings import *
import re
from pymongo import MongoClient


class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[DB_NAME]
        self.collecton=self.db[COLLECTION_DETAIL]

    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get('link')
            response=requests.get(url,headers=headers)
            self.parse_item(response,url)

    def parse_item(self,response,url):
        sel=Selector(text=response.text)

        unique_id=sel.xpath("//td[@class='col data' and @data-td='EAN']//text()").get()
        product_name=sel.xpath("//span[@class='base']//text()").get()
        brand=sel.xpath("//td[@class='col data' and @data-td='Merk']//text()").get()
        pdp_url=url
        match_quantity= re.search(r'(\d+(?:[\.,]\d+)?(?:\s*[xX×]\s*\d+)?)', product_name)
        grammage_quantity=match_quantity.group() if match_quantity else None
        match_unit=re.search(r'\b(kg|g|ml|l)\b', product_name)
        grammage_unit = match_unit.group() if match_unit else None
        instock=sel.xpath("//span[@class='in-stock-text']//text()").get()
        regular_price=sel.xpath("//span[@class='price']//text()").get()
        currency=sel.xpath("//span[@class='price-per_unit']//text()").get()
        currency=(re.search(r'€', currency)).group()if currency else None
        breadcrumb=sel.xpath("//div[@class='breadcrumbs']//li//span[@itemprop='name']//text()").getall()
        description_list=sel.xpath("//div[@class='product attribute description']/div//text()").getall()
        description = ' '.join([x.strip() for x in description_list if x.strip()])
        material_composition=sel.xpath("//td[@class='col data' and @data-td='Samenstelling']//text()").get()
        nutritional_information=sel.xpath("//td[@class='col data' and @data-td='Analyse']//text()").get()
        feeding_recommendation=sel.xpath("//td[@class='col data' and @data-td='Aanbeveling']//text()").get()
        reviews=sel.xpath("//span[@class='counter']//text()").get()

        item={}
        item['unique_id']=unique_id
        item['product_name']=product_name
        item['brand']=brand
        item['pdp_url']=pdp_url
        item['grammage_quantity']=grammage_quantity
        item['grammage_unit']=grammage_unit
        item['instock']=instock
        item['regular_price']=regular_price
        item['currency']=currency
        item['breadcrumb']=breadcrumb
        item['description']=description
        item['material_composition']=material_composition
        item['nutritional_information']=nutritional_information
        item['feeding_recommendation']=feeding_recommendation
        item['reviews']=reviews

        self.collecton.insert_one(item)


if __name__=='__main__':
    parser=Parser()
    parser.start()