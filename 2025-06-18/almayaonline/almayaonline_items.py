from mongoengine import DynamicDocument, StringField, BooleanField, DictField, ListField, IntField, FloatField,connect
from settings import COLLECTION_DETAILS,MONGO_URI, DB_NAME

class ProductItem(DynamicDocument):
    connect(DB_NAME, host=MONGO_URI, alias='default')

    meta={"db_alias": "default","collection": COLLECTION_DETAILS}
    url=StringField()
    product_name=StringField()
    grammage_quantity=StringField()
    grammage_unit=StringField()
    product_decsription=StringField()
    currency=StringField()
    regular_price=StringField()
    image_url=StringField()



