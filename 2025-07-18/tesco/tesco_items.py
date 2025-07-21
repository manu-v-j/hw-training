from mongoengine import DynamicDocument,StringField,IntField,FloatField,ListField,DictField,connect
from settings import MONGO_URL,MONGO_DB,COLLECTION_DETAILS

class ProductItem(DynamicDocument):
    connect(MONGO_DB,host=MONGO_URL,alias="default")
    meta={"db_alias":"default","collection":COLLECTION_DETAILS}

    product_name=StringField()
    regular_price=StringField()
    currency=StringField()
    pdp_url=StringField()
    ingredients=StringField()
    allergens=StringField()
    grammage_quantity=StringField()
    grammage_unit=StringField()
    nutritions=DictField()
    storage_instructions=StringField()
    preparation_instructions=StringField()
    recycling_information=StringField()
    color=ListField()
    size=ListField()
    material=StringField()
    grape_variety=StringField()
    country_of_origin=StringField()
    care_instructions=StringField()
    manufacturer_address=StringField()
    return_address=StringField()
    rating=StringField()
    review=StringField()
    breadcrumbs=ListField()
    image_url=ListField()
    offer_valid_from=StringField()
    offer_valid_upto=StringField()
      