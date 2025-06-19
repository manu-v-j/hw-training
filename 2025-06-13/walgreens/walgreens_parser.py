import requests
from settings import MONGO_URI,MONGO_DB,COLLECTION,COLLEC_DETAIL,headers
from pymongo import MongoClient
from parsel import Selector
import json
import re
import logging
logging.basicConfig(level=logging.INFO)

class Parser:

    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLEC_DETAIL]

    def start(self):
        # for item in self.db[COLLECTION].find():
            # url = item.get("link", "")
            url="https://www.walgreens.com/store/c/walgreens-neti-pot-kit/ID=prod6335256-product"
            product_id = url.split("ID=")[1].split("-")[0]
            logging.info(product_id)

            payload = {
                "passkey": "tpcm2y0z48bicyt0z3et5n2xf",
                "apiversion": "5.5",
                "displaycode": "2001-en_us",
                "resource.q0": "products",
                "filter.q0": f"id:eq:{product_id}",
            }

            response = requests.get("https://api.bazaarvoice.com/data/batch.json", params=payload)
            raw_text = response.text

            json_str = re.sub(r'^BV\._internal\.dataHandler0\((.*)\)$', r'\1', raw_text)
            json_obj = json.loads(json_str)

            response = requests.get(url, headers=headers)
            self.parse_item(response, json_obj)


    def parse_item(self,response,json_data):
            sel=Selector(text=response.text)
            script_list=sel.xpath(".//script[@type='application/ld+json']/text()").getall()

            script_one=script_list[0]
            script_two=script_list[1]

            data=json.loads(script_one)
            breadcrumb_list=json.loads(script_two)

            retailer_id = ""
            product_name = data.get("name","")
            grammage = data.get("weight","")
            ingredients = data.get("category",{}).get("activeIngredient","")
            warning = data.get("category",{}).get("warning","")
            result_list = json_data.get("BatchedResults", {}).get("q0", {}).get("Results", [])
            for item in result_list:
                 upc=item.get("UPCs",[])
                 product_description=item.get("Description","")
            item_list = breadcrumb_list.get("itemListElement",[])
            breadcrumb = [item.get("name", "") for item in breadcrumb_list.get("itemListElement", [])]
            product_sku = data.get("sku")
            brand = data.get("brand",{}).get("name","")
            rating = data.get("aggregateRating",{}).get("ratingValue","")
            review = data.get("aggregateRating",{}).get("reviewCount","")
            image_url = data.get("image",[])

            offers_list=data.get("offers",[])
            for item in offers_list:
                retailer_url=item.get("url","")
                selling_price=item.get("price","")

            item={}
            item['Retailer_ID']=retailer_id
            item['Product_name']=product_name
            item['Product_description']=product_description
            item['Grammage']=grammage
            item['UPC']=upc
            item['Ingredients']=ingredients
            item['Warning']=warning
            item['Breadcrumb']=breadcrumb
            item['Product_sku']=product_sku
            item['Brand']=brand
            item['Rating']=rating
            item['Review']=review
            item['Image_url']=image_url
            item['Retailer_URL']=retailer_url
            item['Selling_price']=selling_price
            print(item)

            # self.collection.insert_one(item)

if __name__=='__main__':
    parser=Parser()
    parser.start()