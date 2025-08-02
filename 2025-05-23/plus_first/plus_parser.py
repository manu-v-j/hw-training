import requests
from settings import *
from pymongo import MongoClient
from urllib.parse import urljoin
import re

class Parser:

    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[DB_NAME]
        self.collection=self.db[COLLECTION__DETAIL]

    def start(self):  
        client=MongoClient(MONGO_URI)
        db=client[DB_NAME]
        collection=db[COLLECTION]

        for item in db[COLLECTION].find():
            url=item.get("link")
            sku=re.search(r"\d{6}",url).group()
            payload={
                
            "versionInfo": {
                "moduleVersion": "PuN3d6LB4faGdgG7sxfsDQ",
                "apiVersion": "11PE+Ajsou80jI7PsgrPjg"
            },
            "screenData":{
                "variables": {
                        "CartPromotionDeliveryDate": "2025-05-26",
                        "ChannelId": "",
                        "CheckoutId": "46877c68-4b0d-4816-ac21-c46d6ea4fd7f",
                        "LineItemQuantity": 0,
                        "Locale": "nl-NL",
                        "OneWelcomeUserId": "",
                        "OrderEditId": "",
                        "ProductName": "plus-chips-naturel-zak-250-g",
                        "SKU": sku,
                    }
                },
            "viewName": "MainFlow.ProductDetailsPage"  
            }
            
            response=requests.post(url_pdp,headers=headers,json=payload)
            if response.status_code==200:
                self.parse_item(response)

    def parse_item(self,response):
        data=response.json().get("data",{}).get("ProductOut",{})

        url=data.get("Overview").get("Slug")
        full_url=urljoin("https://www.plus.nl/product/plus-ribbelchips-naturel-zak-250-g-560636",url)

        name=data.get("Overview",{}).get("Name")
        price=data.get("Overview",{}).get("Price")

        breadcrumbs_list=data.get("Categories",{}).get("List",[])
        breadcrumbs=[item.get("Name") for item in breadcrumbs_list]

        nutrients={}
        nutrients_list=data.get("Nutrient",{}).get("Nutrients",{}).get("List",[])
        for item in nutrients_list:
            description=item.get("Description")
            value=item.get("QuantityContained",{}).get("Value")
            if description and value is not None:
                nutrients[description]=value

        promotion=data.get("Marketing",{}).get("Message")
        ingredients=data.get("Ingredients")
        images=data.get("Overview",{}).get("Image").get("URL")
        
        
        data={
            "url":full_url,
            "name":name,
            "price":price,
            "breadcrumbs":breadcrumbs,
            "nutrients":nutrients,
            "promotion":promotion,
            "ingredients":ingredients,
            "images":images
        }

        self.collection.insert_one(data)

if __name__=="__main__":
    parser=Parser()
    parser.start()