from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS
from pymongo import MongoClient
import csv


class Export:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client=self.db[MONGO_DB]
        self.all_items=[]
    
    def start(self):
        for item in self.db[COLLECTION_DETAILS].find():
            price=item.get('price')
            description=item.get('description')
            specifications=item.get('specifications')
            images=item.get('images')
            location=item.get('location')
            contact_info=item.get('contact_info')

            self.all_items.append({
                'Price':price,
                'Description':description,
                'Specifications':specifications,
                'Images':images,
                'Location':location,
                'Contact_info':contact_info

            })

            field_names=['Price','Description','Specifications','Images','Location','Contact_info']

            with open('mylittlesalesman_20250729.csv','w') as csv_file:
                writer=csv.DictWriter(csv_file,field_names)
                writer.writeheader()
                writer.writerows(self.all_items)
