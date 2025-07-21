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
            product_name=item.get('product_name')
            regular_price=item.get('regular_price')
            currency=item.get('currency')
            pdp_url=item.get('pdp_url')
            ingredients=item.get('ingredients')
            allergens=item.get('allergens')
            grammage_quantity=item.get('grammage_quantity')
            grammage_unit=item.get('grammage_unit')
            nutritions=item.get('nutritions')
            storage_instructions=item.get('storage_instructions')
            preparation_instructions=item.get('preparation_instructions')
            recycling_information=item.get('recycling_information')
            color=item.get('color')
            size=item.get('size')
            material=item.get('material')
            grape_variety=item.get('grape_variety')
            country_of_origin=item.get('country_of_origin')
            manufacturer_address=item.get('manufacturer_address')
            return_address=item.get('return_address')
            rating=item.get('rating')
            review=item.get('review')
            breadcrumbs=item.get('breadcrumbs')
            image_url=item.get('image_url')
            offer_valid_from=item.get('offer_valid_from')
            offer_valid_upto=item.get('offer_valid_upto')


            self.all_items.append({
                'Product_name':product_name,
                'Regular_price':regular_price,
                'Currency':currency,
                'Pdp_url':pdp_url,
                'Ingredients':ingredients,
                'Allergens':allergens,
                'Grammage_quantity':grammage_quantity,
                'Grammage_unit':grammage_unit,
                'Nutritions':nutritions,
                'Storage_instructions':storage_instructions,
                'Preparation_instructions':preparation_instructions,
                'Recycling_information':recycling_information,
                'Color':color,
                'Size':size,
                'Material':material,
                'Grape_variety':grape_variety,
                'Country_of_origin':country_of_origin,
                'Manufacturer_address':manufacturer_address,
                'Return_address':return_address,
                'Rating':rating,
                'Review':review,
                'Breadcrumbs':breadcrumbs,
                'Image_url':image_url,
                'Offer_valid_from':offer_valid_from,
                'Offer_valid_upto':offer_valid_upto

            })

            field_names=['Product_name','Regular_price','Currency','Pdp_url','Ingredients','Allergens','Grammage_quantity','Grammage_unit','Nutritions',
                         'Storage_instructions','Preparation_instructions','Recycling_information','Color','Size','Material','Grape_variety',
                         'Country_of_origin','Manufacturer_address','Return_address','Rating','Review','Breadcrumbs','Image_url','Offer_valid_from',
                         'Offer_valid_upto']
            
            with open('tesco_20250718.csv','w') as csv_file:
                writer=csv.DictWriter(csv_file,field_names)
                writer.writeheader()
                writer.writerows(self.all_items)


if __name__=='__main__':
    export=Export()
    export.start()