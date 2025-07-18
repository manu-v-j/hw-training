from settings import MONGO_URI,MONGO_DB,COLLECTION_DETAILS
from pymongo import MongoClient
import csv

client=MongoClient(MONGO_URI)
db=client[MONGO_DB]

class Export:
    def __init__(self):
        self.all_items=[]

    def start(self):
        for item in db[COLLECTION_DETAILS].find():
            product_name=item.get('product_name')
            regular_price=item.get('regular_price')
            currency=item.get('currency')
            product_description=item.get('product_description')
            pdp_url=item.get('pdp_url')
            size=item.get('size')
            clothing_length=item.get('clothing_length')
            clothing_fit=item.get('clothing_fit')
            style=item.get('style')
            neck_style=item.get('neck_style')
            country_of_origin=item.get('country_of_origin')
            manufacturer_address=item.get('manufacturer_address')
            importer_address=item.get('importer_address')
            material_composition=item.get('material_composition')
            material=item.get('material')
            care_instructions=item.get('care_instructions')
            image_url=item.get('image_url')
            color=item.get('color')
            relative_color=item.get('relative_color')
            breadcrumbs=item.get('breadcrumbs')


            self.all_items.append({
                'Product_name':product_name,
                'Regular_price':regular_price,
                'Currency':currency,
                'Product_description':product_description,
                'Pdp_url':pdp_url,
                'Size':size,
                'Clothing_length':clothing_length,
                'Clothing_fit':clothing_fit,
                'Style':style,
                'Neck_style':neck_style,
                'Country_of_origin':country_of_origin,
                'Manufacturer_address':manufacturer_address,
                'Importer_address':importer_address,
                'Material_composition':material_composition,
                'Material':material,
                'Care_instructions':care_instructions,
                'Image_url':image_url,
                'Color':color,
                'Relative_color':relative_color,
                'Breadcrumbs':breadcrumbs

            })

            fieldnames=[
                'Product_name','Regular_price','Currency','Product_description','Pdp_url','Size','Clothing_length','Clothing_fit','Style',
                'Neck_style','Country_of_origin','Manufacturer_address','Importer_address','Material_composition','Material','Care_instructions','Image_url',
                'Color','Relative_color','Breadcrumbs'
            ]

            with open('hm_20250630.csv','w',newline='') as csv_file:
                writer=csv.DictWriter(csv_file,fieldnames)
                writer.writeheader()
                writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()