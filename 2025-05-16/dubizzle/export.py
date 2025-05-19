import logging
import json
from settings import MONGO_URI, DB_NAME, COLLECTION
from pymongo import MongoClient


client = MongoClient(MONGO_URI)
db = client[DB_NAME]



class Export:
    def __init__(self):
        self.all_items = []

    def start(self):
        for item in db[COLLECTION].find():
            url = item.get("url")
            price = item.get("price")
            currency = item.get("currency")
            bedroom = item.get("bedroom")  
            bathroom = item.get("bathroom")
            area = item.get("area")
            location = item.get("location")
            breadcrumb = item.get("breadcrumb")
            description = item.get("description")
            images = item.get("images")

            self.all_items.append({
                "url": url,
                "price": price,
                "currency": currency,
                "bedroom": bedroom,
                "bathroom": bathroom,
                "area": area,
                "location": location,
                "breadcrumb": breadcrumb,
                "description": description,
                "images": images
            })

        with open("result.json","w", encoding="utf-8") as file:
            json.dump(self.all_items, file, ensure_ascii=False, indent=4)


exporter = Export()
exporter.start()
