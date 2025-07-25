from mongoengine import DynamicDocument,IntField,StringField,ListField,FloatField,connect
from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS

class Product_Item(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias="default")
    meta={"db_alias":"default","collection":COLLECTION_DETAILS}

    product_id=StringField()
    product_name=StringField()
    brand=StringField()
    regular_price=StringField()
    selling_price=StringField()
    promotion_description=StringField()
    currency=StringField()
    pdp_url=StringField()
    breadcrumb=StringField()
    product_description=StringField()
    color=ListField()
    size=ListField()
    rating=StringField()
    review=StringField()
    features=StringField()
    material_care_instruction=StringField()
    availability=StringField()
    image_url=ListField()
                