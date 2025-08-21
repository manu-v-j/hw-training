from settings import MONGO_URL, MONGO_DB, COLLECTION_DETAILS
from pymongo import MongoClient
import csv

class Export:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.all_items = []

    def start(self):
        for item in self.db[COLLECTION_DETAILS].find():
            prices=item.get('prices')
            product_id=item.get('product_id')
            product_description=item.get('product_description')
            color=item.get('color')
            department=item.get('department')
            sub_department=item.get('sub_department')
            product_type=item.get('product_type')

            self.all_items.append({
                'prices':prices,
                'product_id':product_id,
                'product_description':product_description,
                'color':color,
                'department':department,
                'sub_department':sub_department,
                'product_type':product_type
            })

            headers=['prices','product_id','product_description','color','department','sub_department','product_type']

            with open('zara_20250821.csv', 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()
