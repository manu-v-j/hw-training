from mongoengine import DynamicDocument,StringField,ListField,FloatField,BooleanField,DictField,IntField,connect
from settings import MONGO_URI,DB_NAME,COLLECTION_DETAIL

class ProductItem(DynamicDocument):
    connect(DB_NAME,host=MONGO_URI,alias="default")
    meta={"db_alias":"default","collection":COLLECTION_DETAIL}
    url=StringField()
    product_name=StringField()
    sales_price=FloatField()
    product_sku=IntField()
    brand=StringField()
    total_number_of_reviews=IntField()
    star_rating=FloatField()
    review_title=StringField()
    review_text=StringField()
   



