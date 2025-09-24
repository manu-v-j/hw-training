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
            product_name=item.get('product_name','')
            selling_price=item.get('selling_price','')
            regular_price=item.get('regular_price','')
            currency=item.get('currency','')
            pdp_url=item.get('pdp_url','')
            product_description=item.get('product_description','')
            rating=item.get('rating','')
            review=item.get('review',{})
            promotion_description=item.get('promotion_description','')
            breadcrumb=item.get('breadcrumb','')
            images=item.get('images','')
            
            product_description=re.sub(r'\s+',' ',product_description)
            product_description = re.sub(r'[\u200b\u200c\u200d\u2060]', '', product_description)
            breadcrumb=re.sub(r'[\u200b\u200c\u200d\u2060]', '', breadcrumb)
            product_name=re.sub(r'[\u200b\u200c\u200d\u2060]', '', product_name)

            self.all_items.append({
                'product_name':product_name,
                'selling_price':selling_price,
                'regular_price':regular_price,
                'currency':currency,
                'pdp_url':pdp_url,
                'product_description':product_description,
                'rating':rating,
                'review':review,
                'promotion_description':promotion_description,
                'breadcrumb':breadcrumb,
                'images':images,
            })

            headers=['product_name','selling_price','regular_price','currency','pdp_url','product_description','rating',
                     'review','promotion_description','breadcrumb','images']

            with open('lorespresso_20250924.csv', 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(self.all_items)


if __name__=='__main__':
    export=Export()
    export.start()

   
 
 
   
   