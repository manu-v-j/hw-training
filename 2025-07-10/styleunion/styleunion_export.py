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
            size=item.get('size')
            color=item.get('color')
            pdp_url=item.get('pdp_url')
            material=item.get('material')
            pattern=item.get('pattern')
            length=item.get('length')
            neck_style=item.get('neck_style')
            clothing_fit=item.get('clothing_fit')
            product_description=item.get('product_description')
            care_instructions=item.get('care_instructions')
            image_url=item.get('image_url')
            product_sku=item.get('product_sku')
            self.all_items.append({
                'Product_name':product_name,
                'Regular_price':regular_price,
                'Currency':currency,
                'Size':size,
                'Color':color,
                'Pdp_url':pdp_url,
                'Material':material,
                'Pattern':pattern,
                'Length':length,
                'Neck_style':neck_style,
                'Clothing_fit':clothing_fit,
                'Product_description':product_description,
                'Care_instructions':care_instructions,
                'Image_url':image_url,
                'Product_sku':product_sku
            })

            field_names=['Product_name','Regular_price','Currency','Size','Color','Pdp_url','Material','Pattern','Length','Neck_style',
                         'Clothing_fit','Product_description','Care_instructions','Image_url']
            

            with open('styleunion_20250710.csv','w',newline='') as csv_file:
              writer=csv.DictWriter(csv_file,field_names)
              writer.writeheader()
              writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()