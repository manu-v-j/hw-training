from mongoengine import DynamicDocument,StringField,ListField,FloatField,IntField,connect
from settings import MONGO_DB,MONGO_URI,COLLECTION_DETAILS

class ProductItem(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URI,alias="default")
    meta={"db_alias":"default","collection":COLLECTION_DETAILS}

    product_name=StringField()
    regular_price=StringField()
    currency=StringField()
    size=ListField()
    color=ListField()
    pdp_url=StringField()
    material=StringField()
    pattern=StringField()
    length=StringField()
    neck_style=StringField()
    clothing_fit=StringField()
    product_description=StringField()
    care_instructions=StringField()
    image_url=ListField()

 


