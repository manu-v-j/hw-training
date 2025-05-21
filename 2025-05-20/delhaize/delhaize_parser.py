from settings import MONGO_URI,DB_NAME,COLLECTION
from pymongo import MongoClient
import re
import requests

client=MongoClient(MONGO_URI)
db=client[DB_NAME]
for item in db[COLLECTION].find():
    url=item.get("url")
    match=re.findall("S\d+",url)
    product_code=match[0]
    product_api=f"https://www.delhaize.be/api/v1/?operationName=ProductDetails&variables=%7B%22productCode%22%3A%22{product_code}%22%2C%22lang%22%3A%22nl%22%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2218006c9fd3796b52136051c77d1c05b451b18ce72e6fdb191570da1de6d2089e%22%7D%7D"
    response=requests.get(product_api)
    if response.status_code==200:
        data=response.json()
        product_name=data.get("data", {}).get("productDetails", {}).get("name")
        price=data.get("data", {}).get("productDetails", {}).get("price",{}).get("unitPrice")
        currency=data.get("data", {}).get("productDetails", {}).get("price",{}).get("currencySymbol")
        producer_name=data.get("data", {}).get("productDetails", {}).get("wineProducer",{}).get("name","")
        producer_address = data.get("data", {}).get("productDetails", {}).get("wineProducer", {}).get("street", "none").strip()
        print(producer_name)



