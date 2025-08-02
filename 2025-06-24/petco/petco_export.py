import csv
from settings import MONGO_URI,MONGO_DB,COLLECTION_DETAILS
from pymongo import MongoClient

client=MongoClient(MONGO_URI)
db=client[MONGO_DB]

class Export:
    def __init__(self):
        self.all_items=[]

    def start(self):
        for item in db[COLLECTION_DETAILS].find():
            product_name=item.get("product_name")
            brand=item.get("brand")
            selling_price=item.get("selling_price")
            currency=item.get("currency")
            product_sku=item.get("product_sku")
            size=item.get("size")
            pdp_url=item.get("pdp_url")
            product_description=item.get("product_description")
            breadcrumb=item.get("breadcrumb")
            rating=item.get("rating")
            review=item.get("review")
            image_url=item.get("image_url")
            nutritions=item.get("nutritions")
            ingredients=item.get("ingredients")

            self.all_items.append({
                'Product_name':product_name,
                'Brand':brand,
                'Selling_price':selling_price,
                'Currency':currency,
                'Product_sku':product_sku,
                'Size':size,
                'Pdp_url':pdp_url,
                'Product_description':product_description,
                'Breadcrumb':breadcrumb,
                'Rating':rating,
                'Review':review,
                'Image_url':image_url,
                'Nutritions':nutritions,
                'Ingredients':ingredients
                
            })
            fieldnames=[
                'Product_name','Brand','Selling_price','Currency','Product_sku','Size','Pdp_url','Product_description','Breadcrumb',
                'Rating','Review','Image_url','Nutritions','Ingredients'
            ]
            with open("DataHut_20250624.csv","w",newline="") as csvfile:
                writer=csv.DictWriter(csvfile,fieldnames)
                writer.writeheader()
                writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()