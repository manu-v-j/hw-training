from mongoengine import DynamicDocument, StringField, BooleanField, DictField, ListField, IntField, FloatField,connect
from settings import COLLEC_DETAIL
from settings import MONGO_URI, MONGO_DB
class ProductItem(DynamicDocument):
    connect(MONGO_DB, host=MONGO_URI, alias='default')

    meta={"db_alias": "default","collection": COLLEC_DETAIL}
    retailer_id=StringField()
    product_name=StringField()
    product_description=StringField()
    grammage=StringField()
    upc=IntField()
    ingredients=StringField()
    warning=StringField()
    product_sku=StringField()
    brand=StringField()
    rating=FloatField()
    review=IntField()
    image_url=ListField()
    retailer_URL=StringField()
    selling_price=FloatField()

     