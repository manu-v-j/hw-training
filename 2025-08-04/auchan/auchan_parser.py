import requests
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION,cookies
import json
from pymongo import MongoClient
from auchan_items import Product_Item
import re
import logging
logging.basicConfig(level=logging.INFO)

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]

    def start(self):
        for item in self.db[COLLECTION].find().limit(200):
            pdp_url=item.get('link')
            sku=item.get('sku')
            url=f'https://auchan.hu/api/v2/products/sku/{sku}?category_id=5680&hl=hu'
            response=requests.get(url,headers=headers,cookies=cookies)
            if response.status_code==200:
                self.parse_item(response,pdp_url)

    def parse_item(self,response,pdp_url):
        data=response.json()
        unique_id=data.get('defaultVariant',{}).get('sku','')
        product_name=data.get('defaultVariant',{}).get('name','')
        regular_price= data.get('defaultVariant',{}).get('price',{}).get('net','')
        selling_price=data.get('defaultVariant',{}).get('price',{}).get('netDiscounted','')
        percentage_discount=data.get('defaultVariant',{}).get('price',{}).get('discountDisplayPercentage','')
        category_list=data.get('categories',[])

        #CLEAN
        selling_price = f"{float(selling_price):.2f}"
        regular_price=f"{float(regular_price):.2f}"
        breadcrumb=[]
        breadcrumb = '>'.join(['Főoldal', 'Online áruház'] + [category.get('name', '') for category in category_list] + [product_name])

       
        pattern = r'\d+(?:[.,]\d+)?\s*(ml|l|g|kg)'
        match = re.findall(pattern, product_name.lower())
        uom = match[-1] if match else ''

        item={}
        item['unique_id']=unique_id
        item['product_name']=product_name
        item['regular_price']=regular_price
        item['selling_price']=selling_price
        item['percentage_discount']=percentage_discount
        item['breadcrumb']=breadcrumb
        item['pdp_url']=pdp_url
        item['uom']=uom

        product_item=Product_Item(**item)
        product_item.save()
        logging.info(item)


if __name__=='__main__':
    parser=Parser()
    parser.start()