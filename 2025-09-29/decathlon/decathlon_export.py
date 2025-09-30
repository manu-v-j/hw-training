from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS
from pymongo import MongoClient
import csv,re


class Export:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.all_items = []

    def start(self):
        for item in self.db[COLLECTION_DETAILS].find():
            unique_id=item.get('unique_id','')
            product_name=item.get('product_name','')
            brand=item.get('brand','')
            selling_price=item.get('selling_price','')
            regular_price=item.get('regular_price','')
            currency=item.get('currency','')
            pdp_url=item.get('pdp_url','')
            product_description=item.get('product_description','')
            rating=item.get('rating','')
            review=item.get('review','')
            breadcrumb=item.get('breadcrumb','')
            color=item.get('color','')
            size=item.get('size','')
            promotion_description=item.get('promotion_description','')
            care_instructions=item.get('care_instructions','')
            material_composition=item.get('material_composition','')
            image_url=item.get('image_url','')

            selling_price = "{:.2f}".format(float(selling_price.strip()))
            regular_price = "{:.2f}".format(float(regular_price.strip()))       
            product_description=re.sub(r'\s+',' ',product_description)
            care_instructions=re.sub(r'\s+',' ',care_instructions)

            self.all_items.append({
                'unique_id':unique_id,
                'product_name':product_name,
                'brand':brand,
                'selling_price':selling_price,
                'regular_price':regular_price,
                'currency':currency,
                'pdp_url':pdp_url,
                'product_description':product_description,
                'rating':rating,
                'review':review,
                'breadcrumb':breadcrumb,
                'color':color,
                'size':size,
                'promotion_description':promotion_description,
                'care_instructions':care_instructions,
                'material_composition':material_composition,
                'image_url':image_url
            })

            headers=['unique_id','product_name','brand','selling_price','regular_price',
                    'currency','pdp_url','product_description','rating','review','breadcrumb','color','size',
                    'promotion_description','care_instructions','material_composition','image_url']

            with open('decathlon_20250930.csv', 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(self.all_items)


if __name__=='__main__':
    export=Export()
    export.start()

   
 
 
   
   