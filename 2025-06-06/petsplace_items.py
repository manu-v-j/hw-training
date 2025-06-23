from mongoengine import DynamicDocument,IntField,DictField,StringField,ListField,FloatField,connect
from settings import MONGO_URI,DB_NAME,COLLECTION_DETAIL

class ProductItem(DynamicDocument):
    connect(DB_NAME,host=MONGO_URI,alias='default')
    meta={"db_alias":"default","collection":COLLECTION_DETAIL}

    unique_id=StringField()
    product_name=StringField()
    brand=StringField()
    pdp_url=StringField()
    grammage_quantity=StringField()
    grammage_unit=StringField()
    instock=StringField()
    regular_price=StringField()
    currency=StringField()
    breadcrumb=ListField()
    description=StringField()
    material_composition=StringField()
    nutritional_information=StringField()
    feeding_recommendation=StringField()
    reviews=IntField()

