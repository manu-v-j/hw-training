from settings import MONGO_URL, MONGO_DB, COLLECTION_DETAILS
from pymongo import MongoClient
import csv

class Export:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.all_items = []

    def start(self):
        for item in self.db[COLLECTION_DETAILS].find():
            unique_id = item.get('unique_id')
            competitor_name = item.get('competitor_name')
            product_name = item.get('product_name')  
            brand = item.get('brand')
            selling_price = item.get('selling_price')
            regular_price = item.get('regular_price')
            percentage_discount = item.get('percentage_discount')
            pdp_url = item.get('pdp_url')
            features = item.get('features')
            color = item.get('color')
            product_description = item.get('product_description')
            availability = item.get('availability')
            image = item.get('image')

            self.all_items.append({
                'unique_id': unique_id,
                'competitor_name': competitor_name,
                'product_name': product_name,
                'brand': brand,
                'selling_price': selling_price,
                'regular_price': regular_price,
                'percentage_discount': percentage_discount,
                'pdp_url': pdp_url,
                'features': features,
                'color': color,
                'product_description': product_description,
                'availability': availability,
                'image': image
            })

        field_names = [
            'unique_id', 'competitor_name', 'product_name', 'brand', 'selling_price',
            'regular_price', 'percentage_discount', 'pdp_url', 'features', 'color',
            'product_description', 'availability', 'image'
        ]

        with open('lego_20250730.csv', 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(self.all_items)


if __name__ == "__main__":
    Export().start()