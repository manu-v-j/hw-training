from mongoengine import DynamicDocument,StringField,IntField,ListField,DictField,FloatField,connect
from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS

class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias='default')
    meta={"db_alias":"default",'collection':COLLECTION_DETAILS}

    product_id=StringField()
    product_name=StringField()
    brand=StringField()
    grammage_quantity=StringField()
    grammage_unit=StringField()
    pdp_url=StringField()
    selling_price=StringField()
    regular_price=StringField()
    currency=StringField()
    country_of_origin=StringField()
    breadcrumb=StringField()
    product_description=StringField()
    image_url=ListField()

