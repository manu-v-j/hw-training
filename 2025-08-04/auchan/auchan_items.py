from mongoengine import DynamicDocument,StringField,IntField,ListField,DictField,connect
from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS

class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias='default')
    meta={"db_alias":"default",'collection':COLLECTION_DETAILS}

    unique_id=StringField()
    product_name=StringField()
    regular_price=StringField()
    selling_price=StringField()
    percentage_discount=IntField()
    breadcrumb=StringField()
    pdp_url=StringField()
    uom=StringField()
   

    regular_price = regular_price if regular_price != selling_price else ""