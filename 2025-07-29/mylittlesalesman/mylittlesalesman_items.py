from mongoengine import DynamicDocument,StringField,IntField,ListField,DictField,connect
from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS

class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias='default')
    meta={"db_alias":"default",'collection':COLLECTION_DETAILS}

    price=StringField()
    description=StringField()
    specifications=DictField()
    images=ListField()
    location=StringField()
    contact_info=StringField()

