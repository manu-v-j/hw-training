import requests
from settings import MONGO_URI,MONGO_DB,COLLECTION,COLLEC_DETAIL,headers
from pymongo import MongoClient
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
            # url="https://www.walgreens.com/store/c/walgreens-neti-pot-kit/ID=prod6335256-product"
            product_id = url.split("ID=")[1].split("-")[0]

            payload={
                    "productId": f"{product_id}",
                   
                    }
            response=requests.get("https://www.walgreens.com/productapi/v1/products",params=payload,headers=headers)
            if response.status_code==200:
                 self.parse_item(response)

    def parse_item(self,response):
        data=response.json()
        title=data.get("productInfo",{}).get("title","")
        grammage=data.get("productInfo",{}).get("sizeCount","")
        product_name=','.join([title,grammage])
        selling_price=data.get("priceInfo",{}).get("substitutionprice","")
        details_list=data.get("prodDetails",{}).get("section",[])
        product_description_raw=details_list[0].get("description", {}).get("productDesc", "")
        text = re.sub(r'<[^>]+>', '\n', product_description_raw)
        text = html.unescape(text)
        product_description = "\n".join(line.strip() for line in text.splitlines() if line.strip())
        upc=data.get("inventory",{}).get("upc","")

        ingredients = ""
        sections = data.get("prodDetails", {}).get("section", [])
        for section in sections:
            ingredient_info = section.get("ingredients", {}).get("ingredientGroups", [])
            for group in ingredient_info:
                for ingredient_type in group.get("ingredientTypes", []):
                    if ingredient_type.get("typeName", "").lower() == "active":
                        ingredients_list=ingredient_type.get("ingredients", [])
                        ingredients=','.join(ingredients_list)

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
        item['retailer_id']=""
        item['product_name']=product_name
        item['product_description']=product_description
        item['grammage']=grammage
        item['upc']=upc
        item['ingredients']=ingredients
        item['warning']=warning
        item['product_sku']=product_sku
        item['brand']=brand
        item['rating']=rating
        item['review']=review
        item['image_url']=image_url
        item['retailer_URL']=""
        item['selling_price']=selling_price
        logging.info(ingredients)

        self.collection.insert_one(item)

if __name__=='__main__':
    parser=Parser()
    parser.start()