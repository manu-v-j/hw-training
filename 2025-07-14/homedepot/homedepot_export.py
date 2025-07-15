from settings import MONGO_URI,MONGO_DB,DETAILS_COLLECTION
from pymongo import MongoClient
import csv

class Export:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.all_items=[]

    def start(self):
        for item in self.db[DETAILS_COLLECTION].find():
            Product_name=item.get('product_name')
            Selling_price=item.get('selling_price')
            Price_was=item.get('price_was')
            Currency=item.get('currency')
            Pdp_ur=item.get('pdp_url')
            Percentage_discount=item.get('percentage_discount')
            Product_description=item.get('product_description')
            Unique_id=item.get('unique_id')
            Product_sku=item.get('product_sku')
            Brand=item.get('brand')
            Rating=item.get('rating')
            Review=item.get('review')
            Color=item.get('color')
            Model_number=item.get('model_number')
            Depth=item.get('depth')
            Height=item.get('height')
            Width=item.get('width')
            Weight=item.get('weight')
            Image_url=item.get('image_url')
            Breadcrumbs=item.get('breadcrumbs')
            Amperage=item.get('amperage')
            Category=item.get('category')
            Appliance_series=item.get('appliance_series')
            Appliance_type=item.get('appliance_type')
            Energy_consumption=item.get('energy_consumption')
            Tier_rating=item.get('tier_rating')
            Handle_type=item.get('handle_type')
        
            self.all_items.append({
                'Product_name':Product_name,
                'Selling_price':Selling_price,
                'Price_was':Price_was,
                'Currency':Currency,
                'Pdp_ur':Pdp_ur,
                'Percentage_discount':Percentage_discount,
                'Product_description':Product_description,
                'Unique_id':Unique_id,
                'Product_sku':Product_sku,
                'Brand':Brand,
                'Rating':Rating,
                'Review':Review,
                'Color':Color,
                'Model_number':Model_number,
                'Depth':Depth,
                'Height':Height,
                'Width':Width,
                'Weight':Weight,
                'Image_url':Image_url,
                'Breadcrumbs':Breadcrumbs,
                'Amperage':Amperage,
                'Category':Category,
                'Appliance_series':Appliance_series,
                'Appliance_type':Appliance_type,
                'Energy_consumption':Energy_consumption,
                'Tier_rating':Tier_rating,
                'Handle_type':Handle_type
            })

            field_names=['Product_name','Selling_price','Price_was','Currency','Pdp_ur','Percentage_discount','Product_description','Unique_id',
                         'Product_sku','Brand','Rating','Review','Color','Model_number','Depth','Height','Width','Weight','Image_url','Breadcrumbs',
                         'Amperage','Category','Appliance_series','Appliance_type','Energy_consumption','Tier_rating','Handle_type']
            
            with open('DataHut_20250715.csv','w') as csv_file:
                writer=csv.DictWriter(csv_file,field_names)
                writer.writeheader()
                writer.writerows(self.all_items)

if __name__=='__main__':
    export=Export()
    export.start()
