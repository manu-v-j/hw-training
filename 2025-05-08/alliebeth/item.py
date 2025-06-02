from mongoengine import DynamicDocument,StringField
from settings import DB_NAME,COLLEC_DETAIL

class ProductItem(DynamicDocument):

    meta={"collection":COLLEC_DETAIL,"db":DB_NAME}

    url=StringField()
    name=StringField()
    phone=StringField()
    address=StringField()
    about=StringField()