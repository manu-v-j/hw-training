from settings import MONGO_URI,MONGO_DB,COLLECTION_DETAILS
from pymongo import MongoClient
import csv

client=MongoClient(MONGO_URI)
db=client[MONGO_DB]

class Export:
    def __init__(self):
        self.all_items=[]

    def start(self):
        for item in db[COLLECTION_DETAILS].find():
            product_name=item.get('product_name')
            brand=item.get('brand')
            regular_price=item.get('regular_price')
            currency=item.get('currency')
            breadcrumb=item.get('breadcrumb')
            color=item.get('color')
            product_description=item.get('product_description')
            country_of_origin=item.get('country_of_origin')
            instructions=item.get('instructions')
            material_composition=item.get('material_composition')
            size=item.get('size')
            image_urls=item.get('image_urls')
            pdp_url=item.get('pdp_url')
            fit_guide=item.get('fit_guide')
            body_fit=item.get('body_fit')
            product_sku=item.get('product_sku')
            manufacturer_address=item.get('manufacturer_address')
            product_dimensions=item.get('product_dimensions')
            product_quantity=item.get('product_quantity')

            self.all_items.append({
                'product_name':product_name,
                'brand':brand,
                'regular_price':regular_price,
                'currency':currency,
                'breadcrumb':breadcrumb,
                'color':color,
                'product_description':product_description,
                'country_of_origin':country_of_origin,
                'instructions':instructions,
                'material_composition':material_composition,
                'size':size,
                'image_urls':image_urls,
                'pdp_url':pdp_url,
                'fit_guide':fit_guide,
                'body_fit':body_fit,
                'product_sku':product_sku,
                'manufacturer_address':manufacturer_address,
                'product_dimensions':product_dimensions,
                'product_quantity':product_quantity,

            })

            filednames=[
                'product_name','brand','regular_price','currency','breadcrumb','color','product_description','country_of_origin','instructions',
                'material_composition','size','image_urls','pdp_url','fit_guide','body_fit','product_sku','manufacturer_address','product_dimensions','product_quantity'
            ]

            with open("DataHut_20250627.csv","w",newline="") as csvfile:
                writer=csv.DictWriter(csvfile,filednames)
                writer.writeheader()
                writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()
