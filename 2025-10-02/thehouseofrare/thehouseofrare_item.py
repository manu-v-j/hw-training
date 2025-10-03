from mongoengine import DynamicDocument,StringField,IntField,ListField,DictField,FloatField,connect
from settings import MONGO_DB,MONGO_URL,COLLECTION_DETAILS

class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias='default')
    meta={"db_alias":"default",'collection':COLLECTION_DETAILS}

    product_name=StringField()
    selling_price=FloatField()
    regular_price=FloatField()
    currency=StringField()
    pdp_url=StringField()
    product_description=StringField()
    percentage_discount=StringField()
    size=StringField()
    color=StringField()
    breadcrumb=StringField()
    manufacturer_address=StringField()
    images=StringField()


   