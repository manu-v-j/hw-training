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
            stock_number=item.get('stock_number','')
            upc=item.get('upc','')
            product_number=item.get('product_number','')
            part_number=item.get('part_number','')
            images=item.get('images','')
            brand=item.get('brand','')
            product_description=item.get('product_description','')
            pdp_url=item.get('pdp_url','')
            specifications=item.get('specifications',{})
            regulatory_data_sheet=item.get('regulatory_data_sheet','')
            other=item.get('other','')
            catalogs=item.get('catalogs','')
            brochures=item.get('brochures','')
            
            product_description=re.sub(r'\s+',' ',product_description)

            self.all_items.append({
                'product_name':product_name,
                'stock_number':stock_number,
                'upc':upc,
                'product_number':product_number,
                'part_number':part_number,
                'images':images,
                'brand':brand,
                'product_description':product_description,
                'pdp_url':pdp_url,
                'specifications':specifications,
                'regulatory_data_sheet':regulatory_data_sheet,
                'other':other,
                'catalogs':catalogs,
                'brochures':brochures
            })

            headers=['product_name','stock_number','upc','product_number','part_number','images','brand','product_description','pdp_url',
                     'specifications','regulatory_data_sheet','other','catalogs','brochures']

            with open('3m_20250923.csv', 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()

   
 
   
   