from mongoengine import DynamicDocument,StringField,IntField,ListField,DictField,FloatField,connect
from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS

class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias='default')
    meta={"db_alias":"default",'collection':COLLECTION_DETAILS}

    product_name=StringField()
    product_description=StringField()
    upc=StringField()
    brand=StringField()
    selling_price=StringField()
    regular_price=StringField()
    currency=StringField()
    pdp_url=StringField()
    warranty=StringField()
    breadcrumb=StringField()
    image_url=StringField()
    match_reason=StringField()
    