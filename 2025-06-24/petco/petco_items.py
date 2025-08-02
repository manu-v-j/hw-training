from mongoengine import DynamicDocument,StringField,ListField,FloatField,DictField,BooleanField,IntField,connect
from settings import MONGO_URI,MONGO_DB,COLLECTION_DETAILS

class ProductItem(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URI,alias="default")
    meta={"db_alias": "default","collection": COLLECTION_DETAILS}
    product_name=StringField()
    brand=StringField()
    selling_price=FloatField()
    currency=StringField()
    product_sku=IntField()
    size=StringField()
    pdp_url=StringField()
    product_description=StringField()
    breadcrumb=ListField()
    rating=FloatField()
    review=IntField()
    image_url=ListField()
    nutritions=StringField()
    ingredients=StringField()


