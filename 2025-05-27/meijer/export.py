import csv
from settings import MONGO_URI, DB_NAME, COLLECTION_DETAIL
from pymongo import MongoClient


client = MongoClient(MONGO_URI)
db = client[DB_NAME]



class Export:
    def __init__(self):
        self.all_items = []

    def start(self):
        for item in db[COLLECTION_DETAIL].find():
            unique_id = item.get("unique_id")
            product_name = item.get("product_name")
            grammage_quantity = item.get("grammage_quantity")
            grammage_unit = item.get("grammage_unit")  
            regular_price = item.get("regular_price")
            selling_price = item.get("selling_price")
            product_description = item.get("product_description")
            promotion_valid_upto = item.get("promotion_valid_upto")
            image_url = item.get("image_url")
            instock = item.get("instock")
            netcontent = item.get("netcontent")


            self.all_items.append({
                "unique_id": unique_id,
                "product_name": product_name,
                "grammage_quantity": grammage_quantity,
                "grammage_unit": grammage_unit,
                "regular_price": regular_price,
                "selling_price": selling_price,
                "product_description": product_description,
                "promotion_valid_upto": promotion_valid_upto,
                "image_url": image_url,
                "instock": instock,
                "netcontent":netcontent
            })

            fieldnames = [
                    "unique_id", "product_name", "grammage_quantity", "grammage_unit",
                    "regular_price", "selling_price", "product_description",
                    "promotion_valid_upto", "image_url", "instock", "netcontent"
                ]
            
            with open("result.csv", "w", encoding="utf-8", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.all_items)


exporter = Export()
exporter.start()
