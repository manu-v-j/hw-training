from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS
from pymongo import MongoClient
import csv,re


class Export:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.all_items = []

    def start(self):
        for item in self.db[COLLECTION_DETAILS].find().limit(200):
            unique_id=item.get('unique_id','')
            product_name=item.get('product_name','')
            selling_price=item.get('selling_price','')
            regular_price=item.get('regular_price','')
            currency=item.get('currency','')
            rating=item.get('rating','')
            review=item.get('review','')
            pdp_url=item.get('pdp_url','')
            product_description=item.get('product_description','')
            size=item.get('size','')
            style=item.get('style','')
            material=item.get('material','')
            images=item.get('images','')

            selling_price = float(f"{float(selling_price):.2f}")
            regular_price = float(f"{float(regular_price):.2f}")    
            product_description=re.sub(r'\s+',' ',product_description)
            rating=rating.replace('0.0','')
            review=review.replace('0','')
            
            self.all_items.append({
                'unique_id':unique_id,
                'product_name':product_name,
                'selling_price':selling_price,
                'regular_price':regular_price,
                'currency':currency,
                'rating':rating,
                'review':review,
                'pdp_url':pdp_url,
                'product_description':product_description,
                'size':size,
                'style':style,
                'material':material,
                'images':images,
            })

            headers=['unique_id','product_name','selling_price','regular_price',
                    'currency','rating','review','pdp_url','product_description','size',
                    'style','material','images']

            with open('snitch_20251002.csv', 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(self.all_items)


if __name__=='__main__':
    export=Export()
    export.start()

   
 
 
   
   