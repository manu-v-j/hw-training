from settings import MONGO_URI, DB_NAME, COLLECTION, COLLEC_DETAIL
from pymongo import MongoClient
import re
import requests


class Parser:
    def __init__(self):
        pass

    def start(self):
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLEC_DETAIL]

        for item in db[COLLECTION].find():
            url = item.get("url")
            match = re.findall("S\\d+", url)
            if not match:
                continue
            product_code = match[0]
            product_api = f"https://www.delhaize.be/api/v1/?operationName=ProductDetails&variables=%7B%22productCode%22%3A%22{product_code}%22%2C%22lang%22%3A%22nl%22%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2218006c9fd3796b52136051c77d1c05b451b18ce72e6fdb191570da1de6d2089e%22%7D%7D"

            response = requests.get(product_api)
            if response.status_code == 200:
                self.parse_item(response, collection)

    def parse_item(self, response, collection):
        
        data = response.json().get("data", {})
        product_details = data.get("productDetails", {})

        product_name = product_details.get("name")

        price_info = product_details.get("price", {})
        price = price_info.get("unitPrice")
        currency = price_info.get("currencySymbol")

        wine_producer = product_details.get("wineProducer","")
        producer_name = ""
        producer_address = ""
        producer_name = wine_producer.get("name","") if wine_producer else ""
        producer_address = wine_producer.get("street","").strip()  if wine_producer else ""

        grape_variety = ""
        attributes = product_details.get("mobileClassificationAttributes", [])
        for attr in attributes:
            grape_variety = attr.get("value", "")
                

        url = product_details.get("url", "")
        if url:
            url = "" + url
        images = [img.get("url","") for img in product_details.get("galleryImages", [])]

        item={}
      
        item["product_name"]= product_name
        item["price"]= price
        item["currency"]= currency
        item["producer_name"]=producer_name
        item["producer_address"]=producer_address
        item["grape_variety"]= grape_variety
        item["product_url"]= url
        item["images"]=images
    
        collection.insert_one(item)

if __name__ == "__main__":
    parser=Parser()
    parser.start()
