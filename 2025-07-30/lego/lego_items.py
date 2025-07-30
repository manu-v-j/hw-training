from mongoengine import DynamicDocument,StringField,IntField,ListField,DictField,connect
from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS

class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias='default')
    meta={"db_alias":"default",'collection':COLLECTION_DETAILS}

    unique_id=StringField()
    competitor_name=StringField()
    product_name=StringField()
    brand=StringField()
    selling_price=StringField()
    regular_price=StringField()
    percentage_discount=StringField()
    pdp_url=StringField()
    features=DictField()
    color=StringField()
    product_description=StringField()
    availability=StringField()
    image=StringField()

