from mongoengine import DynamicDocument,StringField,IntField,FloatField,ListField,connect
from settings import MONGO_DB,MONGO_URI,DETAILS_COLLECTION

class ProductItem(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URI,alias="default")
    meta={"db_alias":"default","collection":DETAILS_COLLECTION}

    product_name=StringField()
    selling_price=StringField()
    price_was=StringField()
    currency=StringField()
    pdp_url=StringField()
    percentage_discount=StringField()
    product_description=StringField()
    unique_id=StringField()
    product_sku=StringField()
    brand=StringField()
    rating=StringField()
    review=StringField()
    color=StringField()
    model_number=StringField()
    depth=StringField()
    height=StringField()
    width=StringField()
    weight=StringField()
    image_url=ListField()
    breadcrumbs=ListField()
    amperage=StringField()
    category=StringField()
    appliance_series=StringField()
    appliance_type=StringField()
    energy_consumption=StringField()
    tier_rating=StringField()
    handle_type=StringField()


