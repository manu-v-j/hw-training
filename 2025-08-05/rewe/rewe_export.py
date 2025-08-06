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
            unique_id=item.get('unique_id')
            product_name=item.get('product_name')
            brand=item.get('brand')
            grammage_quantity=item.get('grammage_quantity')
            grammage_unit=item.get('grammage_unit')
            pdp_url=item.get('pdp_url')
            selling_price=item.get('selling_price')
            regular_price=item.get('regular_price')
            currency=item.get('currency')
            country_of_origin=item.get('country_of_origin')
            product_description=item.get('product_description')
            breadcrumb=item.get('breadcrumb')
            ingredients=item.get('ingredients')
            nutritions=item.get('nutritions')
            storage_instructions=item.get('storage_instructions')
            image_url=item.get('image_url')

            self.all_items.append({
                'unique_id':unique_id,
                'product_name':product_name,
                'brand':brand,
                'grammage_quantity':grammage_quantity,
                'grammage_unit':grammage_unit,
                'pdp_url':pdp_url,
                'selling_price':selling_price,
                'regular_price':regular_price,
                'currency':currency,
                'country_of_origin':country_of_origin,
                'product_description':product_description,
                'breadcrumb':breadcrumb,
                'ingredients':ingredients,
                'nutritions':nutritions,
                'storage_instructions':storage_instructions,
                'image_url':image_url
            })

            field_names=['unique_id','product_name','brand','grammage_quantity','grammage_unit','pdp_url','selling_price','regular_price',
                         'currency','country_of_origin','product_description','breadcrumb','ingredients','nutritions',
                         'storage_instructions','image_url']


        with open('rewe_20250806.csv', 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(self.all_items)


if __name__ == "__main__":
    Export().start()