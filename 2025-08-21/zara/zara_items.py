from mongoengine import DynamicDocument,StringField,IntField,ListField,DictField,FloatField,connect
from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS

class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias='default')
    meta={"db_alias":"default",'collection':COLLECTION_DETAILS}

    prices=StringField()
    product_id=StringField()
    product_description=StringField()
    color=StringField()
    department=StringField()
    sub_department=StringField()
    product_type=StringField()
 

  
