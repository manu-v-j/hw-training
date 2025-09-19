from mongoengine import DynamicDocument,StringField,IntField,ListField,DictField,FloatField,connect
from settings import MONGO_DB,MONGO_URL,COLLECTION_DETAILS


class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias='default')
    meta={"db_alias":"default",'collection':COLLECTION_DETAILS}

    product_name=StringField()
    size=StringField()
    colour=StringField()
    product_description=StringField()
    product_description=StringField()
    features=StringField()
    material=StringField()
    pdp_url=StringField()
    images=StringField()
    datasheets=StringField()
    declaration_conformity_eu=StringField()
    declaration_conformity_uk=StringField()
    sizing_chart=StringField()
               


