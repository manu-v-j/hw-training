from mongoengine import DynamicDocument,StringField,IntField,ListField,DictField,FloatField,connect
from settings import MONGO_DB,MONGO_URL,COLLECTION_DETAILS


class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias='default')
    meta={"db_alias":"default",'collection':COLLECTION_DETAILS}

    product_name=StringField()
    stock_number=StringField()
    upc=StringField()
    product_number=StringField()
    part_number=StringField()
    images=StringField()
    brand=StringField()
    product_description=StringField()
    pdp_url=StringField()
    specifications=DictField()
    regulatory_data_sheet=StringField()
    other=StringField()
    catalogs=StringField()
    brochures=StringField()
   
       

       
       
               


