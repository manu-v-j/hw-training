import csv
from settings import MONGO_URI,DB_NAME,COLLECTION_DETAIL
from pymongo import MongoClient

client=MongoClient(MONGO_URI)
db=client[DB_NAME]

class Export:
    def __init__(self):
        self.all_items=[]

    def start(self):
        for item in db[COLLECTION_DETAIL].find():
            url=item.get("url")
            product_name=item.get("product_name")
            sales_price=item.get("sales_price")
            product_sku=item.get("product_sku")
            brand=item.get("brand")
            total_number_of_reviews=item.get("total_number_of_reviews")
            star_rating=item.get("star_rating")
            review_title=item.get("review_title")
            review_text=item.get("review_text")

            self.all_items.append({
                'url':url,
                'product_name':product_name,
                'sales_price':sales_price,
                'product_sku':product_sku,
                'brand':brand,
                'total_number_of_reviews':total_number_of_reviews,
                'star_rating':star_rating,
                'review_title':review_title,
                'review_text':review_text
            })

            fieldnames=[
                "url","product_name","sales_price","product_sku","brand","total_number_of_reviews","star_rating",
                "review_title","review_text"
            ]

            with open("result.csv","w",encoding="utf-8",newline="") as csvfile:
                writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.all_items)

exporter = Export()
exporter.start()
