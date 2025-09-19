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
            size=item.get('size','')
            colour=item.get('colour','')
            product_description=item.get('product_description')
            features=item.get('features','')
            material=item.get('material','')
            pdp_url=item.get('pdp_url','')
            images=item.get('images','')
            datasheets=item.get('datasheets','')
            declaration_conformity_eu=item.get('declaration_conformity_eu','')
            declaration_conformity_uk=item.get('declaration_conformity_uk','')
            sizing_chart=item.get('sizing_chart','')

            features=re.sub(r'\s+',' ',features)
            material=re.sub(r'\s+',' ',material)

            self.all_items.append({
                'product_name':product_name,
                'size':size,
                'colour':colour,
                'product_description':product_description,
                'features':features,
                'material':material,
                'pdp_url':pdp_url,
                'images':images,
                'datasheets':datasheets,
                'declaration_conformity_eu':declaration_conformity_eu,
                'declaration_conformity_uk':declaration_conformity_uk,
                'sizing_chart':sizing_chart
            })

            headers=['product_name','size','colour','product_description','features','material','pdp_url','images','datasheets','declaration_conformity_eu','declaration_conformity_uk','sizing_chart']

            with open('portwest_20250919.csv', 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()

    
           