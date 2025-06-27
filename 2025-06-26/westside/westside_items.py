from mongoengine import DynamicDocument,StringField,IntField,ListField,FloatField,DictField,connect
from settings import MONGO_URI,MONGO_DB,COLLECTION_DETAILS

class ProductItem(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URI,alias="default")
    meta={"db_alias":"default","collection":COLLECTION_DETAILS}

    product_name=StringField()
    brand=StringField()
    regular_price=StringField()
    currency=StringField()
    breadcrumb=ListField()
    color=ListField()
    product_description=StringField()
    country_of_origin=StringField()
    instructions=StringField()
    material_composition=StringField()
    size=ListField()
    image_urls=ListField()
    pdp_url=StringField()
    fit_guide=StringField()
    body_fit=StringField()
    product_sku=IntField()
    manufacturer_address=StringField()
    product_dimensions=StringField()
    product_quantity=StringField()

