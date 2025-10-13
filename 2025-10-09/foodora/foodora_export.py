from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS
from pymongo import MongoClient
import csv,re

class Export:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.all_items=[]

    def start(self):
        for item in self.db[COLLECTION_DETAILS].find().limit(200):
            product_name=item.get('product_name','')
            selling_price=item.get('selling_price','')
            regular_price=item.get('regular_price','')
            currency=item.get('currency','')
            grammage_quantity=item.get('grammage_quantity','')
            grammage_unit=item.get('grammage_unit','')
            product_unique_key=item.get('product_unique_key','')
            product_description=item.get('product_description','')
            price_per_unit=item.get('price_per_unit')
            image_url=item.get('image_url','')

            product_description=re.sub(r'\s+',' ',product_description)
            selling_price = float(f"{float(selling_price):.2f}")    
            regular_price = float(f"{float(regular_price):.2f}")  
            grammage_quantity=grammage_quantity.replace(',','.')  


            self.all_items.append({
                'product_name':product_name,
                'selling_price':selling_price,
                'regular_price':regular_price,
                'currency':currency,
                'grammage_quantity':grammage_quantity,
                'grammage_unit':grammage_unit,
                'product_unique_key':product_unique_key,
                'product_description':product_description,
                'price_per_unit':price_per_unit,
                'image_url':image_url,

            })


            headers=['product_name','selling_price','regular_price','currency',
                    'grammage_quantity','grammage_unit','product_unique_key','product_description',
                    'price_per_unit','image_url']

            with open('foodora_20251013.csv', 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(self.all_items)


if __name__=='__main__':
    export=Export()
    export.start()
  
