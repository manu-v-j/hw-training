from mongoengine import DynamicDocument,StringField,ListField,FloatField,IntField,connect
from settings import MONGO_DB,MONGO_URI,COLLECTION_DETAILS

class ProductItem(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URI,alias="default")
    meta={"db_alias":"default","collection":COLLECTION_DETAILS}

    product_name=StringField()
    regular_price=StringField()
    currency=StringField()
    product_description=StringField()
    pdp_url=StringField()
    size=ListField()
    clothing_length=StringField()
    clothing_fit=StringField()
    style=StringField()
    neck_style=StringField()
    country_of_origin=StringField()
    manufacturer_address=StringField()
    importer_address=StringField()
    material_composition=StringField()
    material=StringField()
    care_instructions=ListField()
    image_url=ListField()
    color=StringField()
    relative_color=ListField()
    breadcrumbs=ListField()


     