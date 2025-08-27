from settings import MONGO_URL, MONGO_DB, COLLECTION_DETAILS
from pymongo import MongoClient
import csv,re

class Export:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.all_items = []

    def start(self):
        for item in self.db[COLLECTION_DETAILS].find():
            product_name=item.get('product_name')
            product_description=item.get('product_description')
            upc=item.get('upc')
            brand=item.get('brand')
            selling_price=item.get('selling_price')
            regular_price=item.get('regular_price')
            currency=item.get('currency')
            pdp_url=item.get('pdp_url')
            warranty=item.get('warranty')
            breadcrumb=item.get('breadcrumb')
            image_url=item.get('image_url')
            match_reason=item.get('match_reason')

            product_description=re.sub(r"\\'", "", product_description)

            self.all_items.append({
                'product_name':product_name,
                'product_description':product_description,
                'upc':upc,
                'brand':brand,
                'selling_price':selling_price,
                'regular_price':regular_price,
                'currency':currency,
                'pdp_url':pdp_url,
                'warranty':warranty,
                'breadcrumb':breadcrumb,
                'image_url':image_url,
                'match_reason':match_reason
            })

            headers=['product_name','product_description','upc','brand','selling_price','regular_price','currency',
                     'pdp_url','warranty','breadcrumb','image_url','match_reason']
            
            with open('oreillyauto_20250827.csv', 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers,delimiter='|')
                writer.writeheader()
                writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()