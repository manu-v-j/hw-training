from mongoengine import DynamicDocument,StringField,IntField,ListField,DictField,connect
from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS

class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias='default')
    meta={"db_alias":"default",'collection':COLLECTION_DETAILS}

    unique_id=StringField()
    product_name=StringField()
    brand=StringField()
    
    item['unique_id']=unique_id
        item['product_name']=product_name
        item['brand']=brand
        item['grammage_quantity']=grammage_quantity
        item['grammage_unit']=grammage_unit
        item['pdp_url']=url
        item['selling_price']=selling_price
        item['currency']='Euro'
        item['country_of_origin']=country_of_origin
        item['product_description']=product_description
        item['breadcrumb']=breadcrumb
        item['ingredients']=ingredients
        item['nutritions']=nutritions
        item['storage_instructions']=storage_instructions
        item['image_url']=image_url