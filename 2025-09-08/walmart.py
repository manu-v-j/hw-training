from pymongo import MongoClient
from parsel import Selector
MONGO_URL="mongodb://localhost:27017"
MONGO_DB='walmart'
COLLECTION='data'
client=MongoClient(MONGO_URL)
db=client[MONGO_DB]
for item in db[COLLECTION].find().limit(1):
    response=item.get('response','')
    sel=Selector(text=response)
    unique_id=''
    