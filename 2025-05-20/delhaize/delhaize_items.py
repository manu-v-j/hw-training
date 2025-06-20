from mongoengine import DynamicDocument, StringField, BooleanField, DictField, ListField, IntField, FloatField,connect
from settings import MONGO_URI, DB_NAME,COLLEC_DETAIL

class ProductItem(DynamicDocument):
    connect(DB_NAME, host=MONGO_URI, alias='default')
    meta={"db_alias": "default","collection": COLLEC_DETAIL}
    
    product_name=StringField()
    price=FloatField()
    currency=StringField()
    producer_name=StringField()
    producer_address=StringField()
    grape_variety=StringField()
    product_url=StringField()
    images=StringField()



  