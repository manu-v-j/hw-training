import csv
from settings import MONGO_URI,MONGO_DB,COLLEC_DETAIL
from pymongo import MongoClient

client=MongoClient(MONGO_URI)
db=client[MONGO_DB]

class Export:
    def __init__(self):
        self.all_items=[]

    def start(self):
        for item in db[COLLEC_DETAIL].find():
            Retailer_ID=item.get("Retailer_ID")
            Product_name=item.get("Product_name")
            Product_description=item.get("Product_description")
            Grammage=item.get("Grammage")
            UPC=item.get("UPC")
            Ingredients=item.get("Ingredients")
            Warning=item.get("Warning")
            Product_sku=item.get("Product_sku")
            Brand=item.get("Brand")
            Rating=item.get("Rating")
            Review=item.get("Review")
            Image_url=item.get("Image_url")
            Retailer_URL=item.get("Retailer_URL")
            Selling_price=item.get("Selling_price")

            self.all_items.append({
                'Retailer_ID':Retailer_ID,
                'Product_name':Product_name,
                'Product_description':Product_description,
                'Grammage':Grammage,
                'UPC':UPC,
                'Ingredients':Ingredients,
                'Warning':Warning,
                'Product_sku':Product_sku,
                'Brand':Brand,
                'Rating':Rating,
                'Review':Review,
                'Image_url':Image_url,
                'Retailer_URL':Retailer_URL,
                'Selling_price':Selling_price
            })

            fieldnames=[
                'Retailer_ID','Product_name','Product_description','Grammage','UPC','Ingredients','Warning','Product_sku','Brand',
                'Rating','Review','Image_url','Retailer_URL','Selling_price'
            ]

            with open("DataHut_20250613.csv","w",newline="") as csvfile:
                writer=csv.DictWriter(csvfile,fieldnames)
                writer.writeheader()
                writer.writerows(self.all_items)

exporter=Export()
exporter.start()