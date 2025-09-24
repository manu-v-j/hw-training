from mongoengine import DynamicDocument,StringField,IntField,ListField,DictField,FloatField,connect
from settings import MONGO_DB,MONGO_URL,COLLECTION_DETAILS


class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias='default')
    meta={"db_alias":"default",'collection':COLLECTION_DETAILS}

    product_name=StringField()
    selling_price=StringField()
    regular_price=StringField()
    currency=StringField()
    pdp_url=StringField()
    product_decsription=StringField()
    rating=StringField()
    review=StringField()
    promotion_description=StringField()
    breadcrumb=StringField()
    images=StringField()

