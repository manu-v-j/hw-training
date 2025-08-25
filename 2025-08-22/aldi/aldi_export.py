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
            product_id=item.get('product_id','')
            product_name=item.get('product_name','')
            brand=item.get('brand','')
            grammage_quantity=item.get('grammage_quantity','')
            grammage_unit=item.get('grammage_unit','')
            pdp_url=item.get('pdp_url','')
            selling_price=item.get('selling_price','')
            regular_price=item.get('regular_price','')   
            currency=item.get('currency','')
            country_of_origin=item.get('country_of_origin','')
            breadcrumb=item.get('breadcrumb','')
            product_description=item.get('product_description','')
            image_url=item.get('image_url','')

            product_name = product_name.strip().strip().replace("  ", " ")
            product_description = re.sub(r'<br\s*/?>', ' ', product_description, flags=re.IGNORECASE).strip()
            product_description = re.sub(r'\s+', ' ', product_description).strip()
            if not image_url:
                image_url = ''

            country_of_origin = re.sub(r'\s*(and\s+)?Imported', '', country_of_origin, flags=re.IGNORECASE).strip()
            try:
                regular_price = f"{float(regular_price):.2f}" if regular_price else ""
            except:
                regular_price = ""

            try:
                selling_price = f"{float(selling_price):.2f}" if selling_price else ""
            except:
                selling_price = ""

            self.all_items.append({
                'product_id':product_id,
                'product_name':product_name,
                'brand':brand,
                'grammage_quantity':grammage_quantity,
                'grammage_unit':grammage_unit,
                'pdp_url':pdp_url,
                'selling_price':selling_price,
                'regular_price':regular_price,
                'currency':currency,
                'country_of_origin':country_of_origin,
                'breadcrumb':breadcrumb,
                'product_description':product_description,
                'image_url':image_url
            })

        headers=['product_id','product_name','brand','grammage_quantity','grammage_unit',
                 'pdp_url','selling_price','regular_price','currency','country_of_origin',
                 'breadcrumb','product_description','image_url']

        with open('aldi_20250825.csv', 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()
