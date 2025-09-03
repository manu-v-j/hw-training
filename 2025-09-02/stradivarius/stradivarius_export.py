from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS,file_name
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
            pdp_url=item.get('pdp_url')
            prices=item.get('prices')
            product_id=item.get('product_id')
            product_description=item.get('product_description')
            color=item.get('color')
            department=item.get('department')
            sub_department=item.get('sub_department')
            product_type=item.get('product_type')

            product_description = re.sub(r'<.*?>', ' ', product_description)
            product_description = re.sub(r'\s+', ' ', product_description).strip()
            prices = f"{prices:.2f}" 
            color = ",".join(color)


            self.all_items.append({
                'product_name':product_name,
                'pdp_url':pdp_url,
                'prices':prices,
                'product id':product_id,
                'product description':product_description,
                'color':color,
                'department':department,
                'sub department':sub_department,
                'product type':product_type
            })

            headers=['product_name','pdp_url','prices','product id','product description','color','department','sub department','product type']

            with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()