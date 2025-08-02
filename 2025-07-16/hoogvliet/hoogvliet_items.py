from mongoengine import DynamicDocument,StringField,IntField,FloatField,ListField,DictField,connect
from settings import MONGO_URI,MONGO_DB,COLLECTION_DETAILS

class ProductItem(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URI,alias="default")
    meta={"db_alias":"default","collection":COLLECTION_DETAILS}

    product_name=StringField()
    regular_price=StringField() 
    currency=StringField()
    grammage_quantity=StringField()
    grammage_unit=StringField()
    ingredients=StringField()
    pdp_url=StringField()
    storage_instructions=StringField()
    country_of_origin=StringField()
    nutritions=DictField()
    image_url=StringField()
    breadcrumbs=ListField()
     

