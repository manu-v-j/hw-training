from mongoengine import DynamicDocument,StringField,IntField,ListField,DictField,FloatField,connect
from settings import MONGO_DB,MONGO_URL,COLLECTION_DETAILS


class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias='default')
    meta={"db_alias":"default",'collection':COLLECTION_DETAILS}

    product_name=StringField()
    unique_id=StringField()
    grammage_quantity=StringField()
    grammage_unit=StringField()
    pdp_url=StringField()
    rating=StringField()
    review=StringField()
    netweight=StringField()
    country_of_origin=StringField()
    breadcrumb=StringField()
    legal_name=StringField()
    ingredients=StringField()
    storage_instructions=StringField()
    image_url=ListField()

 
     
       