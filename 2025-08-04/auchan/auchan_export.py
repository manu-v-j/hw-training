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
            unique_id = item.get('unique_id')
            product_name = item.get('product_name')  
            regular_price = item.get('regular_price')
            selling_price = item.get('selling_price')
            percentage_discount = item.get('percentage_discount')
            breadcrumb=item.get('breadcrumb')
            pdp_url = item.get('pdp_url')
            uom=item.get('uom')

            self.all_items.append({
                'unique_id': unique_id,
                'product_name': product_name,
                'regular_price': regular_price,
                'selling_price': selling_price,
                'percentage_discount': percentage_discount,
                'breadcrumb': breadcrumb,
                'pdp_url': pdp_url,
                'uom': uom
            })


            field_names = ['unique_id','product_name','regular_price','selling_price','percentage_discount','breadcrumb',
                           'pdp_url','uom']
            
            with open('auchan20250805.csv', 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()