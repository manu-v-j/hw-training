from mongoengine import DynamicDocument,StringField,IntField,ListField,DictField,FloatField,connect
from settings import MONGO_DB,MONGO_URL,COLLECTION_DETAILS

class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias='default')
    meta={"db_alias":"default",'collection':COLLECTION_DETAILS}

    product_name=StringField()
    selling_price=FloatField()
    regular_price=FloatField()
    currency=StringField()
    grammage_quantity=StringField()
    grammage_unit=StringField()
    product_unique_key = StringField(required=True, unique=True) 
    product_description=StringField()
    price_per_unit=StringField()
    image_url=StringField()
  
    


     
           


   