from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS
from pymongo import MongoClient
import csv,re

class Export:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.all_items=[]

    def start(self):
        for item in self.db[COLLECTION_DETAILS].find():
            product_name=item.get('product_name','')
            selling_price=item.get('selling_price','')
            regular_price=item.get('regular_price','')
            currency=item.get('currency','')
            pdp_url=item.get('pdp_url','')
            product_description=item.get('product_description','')
            percentage_discount=item.get('percentage_discount','')
            size=item.get('size','')
            color=item.get('color','')
            breadcrumb=item.get('breadcrumb','')
            manufacturer_address=item.get('manufacturer_address','')
            images=item.get('images','')

            product_description=re.sub(r'\s+',' ',product_description)

            self.all_items.append({
                'product_name':product_name,
                'selling_price':selling_price,
                'regular_price':regular_price,
                'currency':currency,
                'pdp_url':pdp_url,
                'product_description':product_description,
                'percentage_discount':percentage_discount,
                'size':size,
                'color':color,
                'breadcrumb':breadcrumb,
                'manufacturer_address':manufacturer_address,
                'images':images,
            })


            headers=['product_name','selling_price','regular_price','currency',
                    'pdp_url','product_description','percentage_discount','size',
                    'color','breadcrumb','manufacturer_address','images']

            with open('thehouseofrare_20251003.csv', 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(self.all_items)


if __name__=='__main__':
    export=Export()
    export.start()
  