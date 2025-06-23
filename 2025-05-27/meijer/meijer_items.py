from mongoengine import DynamicDocument,StringField,BooleanField,DictField,ListField,IntField,FloatField,connect
from settings import MONGO_URI,DB_NAME,COLLECTION_DETAIL

class ProductItem(DynamicDocument):
    connect(DB_NAME,host=MONGO_URI,alias='default')
    meta={"db_alias":"default","collection":COLLECTION_DETAIL}

    unique_id=StringField()
    product_name=StringField()
    grammage_quantity=StringField()
    grammage_unit=StringField()
    regular_price=FloatField()
    selling_price=FloatField()
    product_description=StringField()
    promotion_valid_upto=ListField()
    image_url=StringField()
    instock=StringField()
    netcontent=StringField()


