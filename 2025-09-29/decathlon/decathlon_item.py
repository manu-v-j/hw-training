from mongoengine import DynamicDocument,StringField,IntField,ListField,DictField,FloatField,connect
from settings import MONGO_DB,MONGO_URL,COLLECTION_DETAILS


class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias='default')
    meta={"db_alias":"default",'collection':COLLECTION_DETAILS}

    unique_id=StringField()
    product_name=StringField()
    brand=StringField()
    selling_price=StringField()
    regular_price=StringField()
    currency=StringField()
    pdp_url=StringField()
    product_description=StringField()
    rating=StringField()
    review=StringField()
    breadcrumb=StringField()
    color=StringField()
    size=StringField()
    warranty=StringField()
    promotion_description=StringField()
    care_instructions=StringField()
    material_composition=StringField()
    image_url=StringField()

 