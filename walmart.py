from pymongo import MongoClient
from parsel import Selector
import json,re
MONGO_URL="mongodb://localhost:27017"
MONGO_DB='walmart'
COLLECTION='data'
client=MongoClient(MONGO_URL)
db=client[MONGO_DB]
for item in db[COLLECTION].find().limit(1):
    response=item.get('response','')
    sel=Selector(text=response)
    unique_id=''
    competitor_name='walmart'
    store_name=''
    store_addressline1=''
    store_addressline2=''
    store_suburb=''
    store_state=''
    store_postcode=''
    store_addressid=''
    extraction_date=''
    script_text=sel.xpath("//script[@type='application/ld+json' and @data-seo-id='schema-org-product']/text()").get()
    data=json.loads(script_text)
    product_name=data.get('name','')
    brand=data.get('brand',{}).get('name','')
    brand_type=''
    grammage_quantity=re.search(r'\d+(\.\d+)?',product_name)
    if grammage_quantity:
        grammage_quantity=grammage_quantity.group(0)
    grammage_unit = re.search(r'\b(oz|ml|g|kg|lb|l)\b', product_name, re.IGNORECASE)
    if grammage_unit:
        grammage_unit=grammage_unit.group(0)
    drained_weight=''
    script_text = sel.xpath("//script[@id='__NEXT_DATA__' and @type='application/json']/text()").get()
    data = json.loads(script_text)

    modules = data.get('props', {}).get('pageProps', {}).get('initialData', {})\
    .get('data', {}).get('seoItemMetaData',{})
    breadcrumb=modules.get('breadCrumbs',[])
    producthierarchy_level1 = breadcrumb[0].get('name', '') if len(breadcrumb) > 0 else ''
    producthierarchy_level2 = breadcrumb[1].get('name', '') if len(breadcrumb) > 1 else ''
    producthierarchy_level3 = breadcrumb[2].get('name', '') if len(breadcrumb) > 2 else ''
    producthierarchy_level4 = breadcrumb[3].get('name', '') if len(breadcrumb) > 3 else ''
    producthierarchy_level5 = breadcrumb[4].get('name', '') if len(breadcrumb) > 4 else ''
    producthierarchy_level6 = breadcrumb[5].get('name', '') if len(breadcrumb) > 5 else ''
    producthierarchy_level7 = breadcrumb[6].get('name', '') if len(breadcrumb) > 6 else ''

    regular_price=



    