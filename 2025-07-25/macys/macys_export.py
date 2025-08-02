from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS
from pymongo import MongoClient
import csv

class Export:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.all_items=[]

    def start(self):
        for item in self.db[COLLECTION_DETAILS].find():
            product_id=item.get('product_id')
            product_name=item.get('product_name')
            brand=item.get('brand')
            regular_price=item.get('regular_price')
            selling_price=item.get('selling_price')
            promotion_description=item.get('promotion_description')
            currency=item.get('currency')
            pdp_url=item.get('pdp_url')
            breadcrumb=item.get('breadcrumb')
            product_description=item.get('product_description')
            color=item.get('color')
            size=item.get('size')
            rating=item.get('rating')
            review=item.get('review')
            features=item.get('features')
            material_care_instruction=item.get('material_care_instruction')
            availability=item.get('availability')
            image_url=item.get('image_url')

            self.all_items.append({
                'Product_id':product_id,
                'Product_name':product_name,
                'Brand':brand,
                'Regular_price':regular_price,
                'Selling_price':selling_price,
                'Promotion_description':promotion_description,
                'Currency':currency,
                'Pdp_url':pdp_url,
                'Breadcrumb':breadcrumb,
                'Product_description':product_description,
                'Color':color,
                'Size':size,
                'Rating':rating,
                'Review':review,
                'Features':features,
                'Material_Care_instruction':material_care_instruction,
                'Availability':availability,
                'Image_url':image_url
            })

            field_names=['Product_id','Product_name','Brand','Regular_price','Selling_price','Promotion_description','Currency','Pdp_url','Breadcrumb',
                         'Product_description','Color','Size','Rating','Review','Features','Material_Care_instruction','Availability','Image_url']
            
            with open('macys_20250725.csv','w') as csv_file:
                writer=csv.DictWriter(csv_file,field_names)
                writer.writeheader()
                writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()