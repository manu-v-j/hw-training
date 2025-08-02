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
            currency=item.get('currency')
            country_of_origin=item.get('country_of_origin')
            product_description=item.get('product_description')
            breadcrumb=item.get('breadcrumb')
            ingredients=item.get('ingredients')
            nutritions=item.get('nutritions')
            storage_instructions=item.get('storage_instructions')
            image_url=item.get('image_url')

            self.all_items.append({
                'Unique_id':unique_id,
                'Product_name':product_name,
                'Brand':brand,
                'Grammage_quantity':grammage_quantity,
                'Grammage_unit':grammage_unit,
                'Pdp_url':pdp_url,
                'Selling_price':selling_price,
                'Currency':currency,
                'Country_of_origin':country_of_origin,
                'Product_description':product_description,
                'Breadcrumb':breadcrumb,
                'Ingredients':ingredients,
                'Nutritions':nutritions,
                'Storage_instructions':storage_instructions,
                'Image_url':image_url
            })

            field_names=['Unique_id','Product_name','Brand','Grammage_quantity','Grammage_unit','Pdp_url','Selling_price',
                         'Currency','Country_of_origin','Product_description','Breadcrumb','Ingredients','Nutritions',
                         'Storage_instructions','Image_url']
            
            with open('shop_20250801.csv', 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(self.all_items)


if __name__ == "__main__":
    Export().start()