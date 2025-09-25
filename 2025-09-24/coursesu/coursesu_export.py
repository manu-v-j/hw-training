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
            unique_id=item.get('unique_id','')
            grammage_quantity=item.get('grammage_quantity','')
            grammage_unit=item.get('grammage_unit','')
            pdp_url=item.get('pdp_url','')
            rating=item.get('rating','')
            review=item.get('review','')
            netweight=item.get('netweight','')
            country_of_origin=item.get('country_of_origin','')
            breadcrumb=item.get('breadcrumb','')
            legal_name=item.get('legal_name','')
            ingredients=item.get('ingredients','')
            storage_instructions=item.get('storage_instructions','')
            image_url=item.get('image_url','')
            
            image_url=','.join(image_url)
            match = re.search(r"([\d.]+)/5", rating)
            if match:
                rating = round(float(match.group(1)), 1)  

            match_review = re.search(r"\d+", str(review))
            if match_review:
                review =match_review.group()
            review=review.replace('Voir l’avis','')
            grammage_quantity=grammage_quantity.replace(',','.')
            netweight=netweight.replace(',','.')

            self.all_items.append({
                'product_name':product_name,
                'unique_id':unique_id,
                'grammage_quantity':grammage_quantity,
                'grammage_unit':grammage_unit,
                'pdp_url':pdp_url,
                'rating':rating,
                'review':review,
                'netweight':netweight,
                'country_of_origin':country_of_origin,
                'breadcrumb':breadcrumb,
                'legal_name':legal_name,
                'ingredients':ingredients,
                'storage_instructions':storage_instructions,
                'image_url':image_url

            })

            headers=['product_name','unique_id','grammage_quantity','grammage_unit','pdp_url','rating',
                     'review','netweight','country_of_origin','breadcrumb','legal_name','ingredients','storage_instructions',
                     'image_url']

            with open('coursesu_20250925.csv', 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(self.all_items)


if __name__=='__main__':
    export=Export()
    export.start()