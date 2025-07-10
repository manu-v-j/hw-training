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
            Product_name=item.get('product_name')
            Regular_price=item.get('regular_price')
            Currency=item.get('currency')
            Size=item.get('size')
            Color=item.get('color')
            Pdp_url=item.get('pdp_url')
            Material=item.get('material')
            Pattern=item.get('pattern')
            Length=item.get('length')
            Neck_style=item.get('neck_style')
            Clothing_fit=item.get('clothing_fit')
            Product_description=item.get('product_description')
            Care_instructions=item.get('care_instructions')
            Image_url=item.get('image_url')
    
            self.all_items.append({
                'Product_name':Product_name,
                'Regular_price':Regular_price,
                'Currency':Currency,
                'Size':Size,
                'Color':Color,
                'Pdp_url':Pdp_url,
                'Material':Material,
                'Pattern':Pattern,
                'Length':Length,
                'Neck_style':Neck_style,
                'Clothing_fit':Clothing_fit,
                'Product_description':Product_description,
                'Care_instructions':Care_instructions,
                'Image_url':Image_url
            })

            field_names=['Product_name','Regular_price','Currency','Size','Color','Pdp_url','Material','Pattern','Length','Neck_style',
                         'Clothing_fit','Product_description','Care_instructions','Image_url']
            

            with open('Datahut_20250710.csv','w',newline='') as csv_file:
              writer=csv.DictWriter(csv_file,field_names)
              writer.writeheader()
              writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()