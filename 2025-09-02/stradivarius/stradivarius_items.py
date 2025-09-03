from mongoengine import DynamicDocument,StringField,IntField,ListField,DictField,FloatField,connect
from settings import MONGO_DB,MONGO_URL,COLLECTION_DETAILS


class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias='default')
    meta={"db_alias":"default",'collection':COLLECTION_DETAILS}

    prices=FloatField()
    product_id=IntField()
    product_description=StringField()
    color=ListField()
    pdp_url=StringField()
    department=StringField()
    sub_department=StringField()
    product_type=StringField()

      


