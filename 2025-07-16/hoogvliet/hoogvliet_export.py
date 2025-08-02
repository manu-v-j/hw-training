from settings import MONGO_URI,MONGO_DB,COLLECTION_DETAILS
from pymongo import MongoClient
import csv

class Export:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.all_items=[]

    def start(self):
        for item in self.db[COLLECTION_DETAILS].find():
            product_name=item.get('product_name')
            regular_price=item.get('regular_price')
            currency=item.get('currency')
            grammage_quantity=item.get('grammage_quantity')
            grammage_unit=item.get('grammage_unit')
            ingredients=item.get('ingredients')
            pdp_url=item.get('pdp_url')
            storage_instructions=item.get('storage_instructions')
            country_of_origin=item.get('country_of_origin')
            nutritions=item.get('nutritions')
            image_url=item.get('image_url')
            breadcrumbs=item.get('breadcrumbs')


            self.all_items.append({
                'Product_name':product_name,
                'Regular_price':regular_price,
                'Currency':currency,
                'Grammage_quantity':grammage_quantity,
                'Grammage_unit':grammage_unit,
                'Ingredients':ingredients,
                'Pdp_url':pdp_url,
                'Storage_instructions':storage_instructions,
                'Country_of_origin':country_of_origin,
                'Nutritions':nutritions,
                'Image_url':image_url,
                'Breadcrumbs':breadcrumbs
            })

            field_names=['Product_name','Regular_price','Currency','Grammage_quantity','Grammage_unit','Ingredients','Pdp_url','Storage_instructions','Country_of_origin',
                        'Nutritions','Image_url','Breadcrumbs']
            
            with open('hoogvilet_20250717.csv','w') as csv_file:
                writer=csv.DictWriter(csv_file,field_names)
                writer.writeheader()
                writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()