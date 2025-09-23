import requests
import re
import logging
from parsel import Selector
from pymongo import MongoClient
from json import loads
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_DETAILS,COLLECTION_ERROR
from item_3m import Product_Item
logging.basicConfig(level=logging.INFO)
class Parser:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_DETAILS]
        self.collection_error=self.db[COLLECTION_ERROR]

    def start(self):
        for item in self.db[COLLECTION].find().limit(300):
            base_url=item.get('link')
            id=item.get('id')
            response=requests.get(base_url,headers=headers)
            if response.status_code==200:
                self.parse_item(response,base_url,id)
            else:
                self.collection_error.insert_one({'link':base_url})
    
    def parse_item(self,response,base_url,id):
        sel=Selector(text=response.text)

        #XAPTH
        SCRIPT_XPATH="//script[starts-with(text(), 'window.__INITIAL_DATA')]/text()"
        BREADCRUMB_XPATH="//ol[@class='MMM--breadcrumbs-list']//span/text()"
        DESCRIPTION_XPATH="//div[@class='sps2-pdp_details--upper_details']//text()"

        #EXTRACT
        script_text = sel.xpath(SCRIPT_XPATH).get()
        json_text = re.sub(r'^window\.__INITIAL_DATA\s*=\s*', '', script_text).strip()
        data = loads(json_text)
        product_name=data.get('productDetails',{}).get('name','')
        stock_number=data.get('productDetails',{}).get('stockNumber','')
        upc=data.get('productDetails',{}).get('upc','')
        product_number=data.get('productDetails',{}).get('productNumber','')
        part_number=data.get('productDetails',{}).get('partNumber','')
        images=data.get('productDetails',{}).get('imageUrl','')

        brand=''
        classification_list=data.get('classificationAttributes',[])
        for item in classification_list:
            if item.get('label', '') == 'Brands':
                brand = item.get('values', [])
                brand=''.join(brand)

        specifications={}
        for item in classification_list:
            key=item.get('label','')
            value_raw=item.get('values','')
            value=','.join(value_raw)
            specifications[key]=value

        breadcrumb_list=sel.xpath(BREADCRUMB_XPATH).getall()
        description_raw = sel.xpath(DESCRIPTION_XPATH).getall()

        breadcrumb = ' > '.join(breadcrumb_list)
        product_description = ' '.join([item.strip() for item in description_raw if item.strip()])
        
        #regualatory data sheet
        params = {
            'size': '4',
            'start': '0',
            'contentType': 'rds',
        }

        response = requests.get(
            f'https://www.3m.com/snaps2/api/pdp/moreResources/https/www.3m.com/3M/en_US{id}',
            params=params,
            headers=headers,
        )
        data_one=response.json()
        regulatory_data_sheet=''
        regulatory=data_one.get('resources',[])
        if regulatory:
            regulatory_data_sheet = [
                item.get('originalUrl', '') for item in regulatory
            ]
        regulatory_data_sheet=','.join(regulatory_data_sheet)

        #oher doc
        params = {
            'size': '4',
            'start': '0',
            'contentType': 'Other',
        }

        response = requests.get(
            f'https://www.3m.com/snaps2/api/pdp/moreResources/https/www.3m.com/3M/en_US{id}',
            params=params,
            headers=headers,
        )

        data_two=response.json()
        other=''
        other_list=data_two.get('resources',[])
        if other_list:
            other = [
                item.get('originalUrl', '') for item in other_list
            ]
        other=','.join(other)

        #catalogs doc
        params = {
            'size': '4',
            'start': '0',
            'contentType': 'catalogs',
        }

        response = requests.get(
            f'https://www.3m.com/snaps2/api/pdp/moreResources/https/www.3m.com/3M/en_US{id}',
            params=params,
            headers=headers,
        )
        data_three=response.json()
        catalogs=''
        catalog_list=data_three.get('resources',[])
        if catalog_list:
            catalogs = [
                item.get('originalUrl', '') for item in catalog_list
            ]
        catalogs=','.join(catalogs)

        #safety doc
        params = {
            'size': '4',
            'start': '0',
            'contentType': 'safety_inserts',
        }

        response = requests.get(
            f'https://www.3m.com/snaps2/api/pdp/moreResources/https/www.3m.com/3M/en_US{id}',
            params=params,
            headers=headers,
        )
        data_four=response.json()
        safety_insert=''
        safety_list=data_four.get('resources',[])
        if safety_list:
            safety_insert = [
                item.get('originalUrl', '') for item in safety_list
            ]
        safety_insert=','.join(safety_insert)

        #brochures doc
        params = {
            'size': '4',
            'start': '0',
            'contentType': 'brochures',
        }

        response = requests.get(
            f'https://www.3m.com/snaps2/api/pdp/moreResources/https/www.3m.com/3M/en_US{id}',
            params=params,
            headers=headers,
        )
        data_five=response.json()
        brochures=''
        brochures_list=data_five.get('resources',[])
        if brochures_list:
            brochures = [
                item.get('originalUrl', '') for item in brochures_list
            ]
        brochures=','.join(brochures)

        item={}
        item['product_name']=product_name
        item['stock_number']=stock_number
        item['upc']=upc
        item['product_number']=product_number
        item['part_number']=part_number
        item['images']=images
        item['brand']=brand
        item['product_description']=product_description
        item['pdp_url']=base_url
        item['breadcrumb']=breadcrumb
        item['specifications']=specifications
        item['regulatory_data_sheet']=regulatory_data_sheet
        item['other']=other
        item['catalogs']=catalogs
        item['brochures']=brochures

        product_item=Product_Item(**item)
        product_item.save()

        logging.info(item)


    
if __name__=='__main__':
    parser=Parser()
    parser.start()