import requests
from settings import MONGO_URI,MONGO_DB,COLLECTION,COLLEC_DETAIL,headers
from pymongo import MongoClient
from parsel import Selector
import json
import re
import logging
import html
logging.basicConfig(level=logging.INFO)

class Parser:

    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLEC_DETAIL]

    def start(self):
        for item in self.db[COLLECTION].find():
            url = item.get("link", "")
            product_id = url.split("ID=")[1].split("-")[0]

            payload={
                    "productId": f"{product_id}",
                   
                    }
            response=requests.get("https://www.walgreens.com/productapi/v1/products",params=payload)
            if response.status_code==200:
                 self.parse_item(response)

    def parse_item(self,response):
        data=response.json()
        product_name=data.get("productInfo",{}).get("title","")
        selling_price=data.get("priceInfo",{}).get("substitutionprice","")
        details_list=data.get("prodDetails",{}).get("section",[])
        product_description_raw=details_list[0].get("description", {}).get("productDesc", "")
        text = re.sub(r'<[^>]+>', '\n', product_description_raw)
        text = html.unescape(text)
        product_description = "\n".join(line.strip() for line in text.splitlines() if line.strip())
        grammage=data.get("productInfo",{}).get("sizeCount","")
        upc=data.get("inventory",{}).get("upc","")

        ingredients = [] 
        sections = data.get("prodDetails", {}).get("section", [])
        for section in sections:
            ingredient_info = section.get("ingredients", {}).get("ingredientGroups", [])
            for group in ingredient_info:
                for ingredient_type in group.get("ingredientTypes", []):
                    if ingredient_type.get("typeName", "").lower() == "active":
                        ingredients.extend(ingredient_type.get("ingredients", []))

        warning = ""       
        for section in sections:
            product_warning = section.get("warnings", {}).get("productWarning", "")
            if product_warning:
                text = re.sub(r'<[^>]+>', '\n', product_warning)
            text = html.unescape(text)
            warning = "\n".join(line.strip() for line in text.splitlines() if line.strip())

        product_sku=data.get("productInfo",{}).get("skuId","")
        brand=data.get("productInfo",{}).get("brandName","")
        for section in sections:
            rating=section.get("reviews",{}).get("overallRating","")
        review=section.get("reviews",{}).get("reviewCount","")

        image_url = []
        product_detail=data.get("productInfo", {}).get("filmStripUrl", [])

        for item in product_detail:
            for key, value in item.items():
                if key.startswith("largeImageUrl"):
                    image_url.append("https:" + value)            

        item={}
        item['Retailer_ID']=""
        item['Product_name']=product_name
        item['Product_description']=product_description
        item['Grammage']=grammage
        item['UPC']=upc
        item['Ingredients']=ingredients
        item['Warning']=warning
        item['Product_sku']=product_sku
        item['Brand']=brand
        item['Rating']=rating
        item['Review']=review
        item['Image_url']=image_url
        item['Retailer_URL']=""
        item['Selling_price']=selling_price
        logging.info(item)

        self.collection.insert_one(item)

if __name__=='__main__':
    parser=Parser()
    parser.start()