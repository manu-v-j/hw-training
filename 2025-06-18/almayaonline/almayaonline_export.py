import csv
from settings import MONGO_URI,DB_NAME,COLLECTION_DETAILS
from pymongo import MongoClient

client=MongoClient(MONGO_URI)
db=client[DB_NAME]

class Export:
    def __init__(self):
        self.all_items=[]

    def start(self):
        for item in db[COLLECTION_DETAILS].find():
            url=item.get("url")
            product_name=item.get("product_name")
            grammage_quantity=item.get("grammage_quantity")
            grammage_unit=item.get("grammage_unit")
            product_decsription=item.get("product_decsription")
            currency=item.get("currency")
            regular_price=item.get("regular_price")
            image_url=item.get("image_url")

            self.all_items.append({
                'Url':url,
                'Product_name':product_name,
                'Grammage_quantity':grammage_quantity,
                'Grammage_unit':grammage_unit,
                'Product_decsription':product_decsription,
                'Currency':currency,
                'Regular_price':regular_price,
                'Image_url':image_url
            })

            fieldnames=['Url','Product_name','Grammage_quantity','Grammage_unit','Product_decsription','Currency','Regular_price','Image_url']
            with open("DataHut_20250618.csv","w",newline="") as csvfile:
                writer=csv.DictWriter(csvfile,fieldnames)
                writer.writeheader()
                writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()	