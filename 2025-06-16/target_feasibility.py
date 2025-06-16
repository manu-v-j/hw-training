import requests
from parsel import Selector
import json
import re
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}
params = {
    "key": "9f36aeafbe60771e321a7cc95a78140772ab3e96",
    "tcin": "83995324", 
    "channel": "WEB",
    "pricing_store_id": "1092",
    "has_pricing_store_id": "true"
}


###############################PARSER##############################

url = "https://redsky.target.com/redsky_aggregations/v1/web/pdp_client_v1"

response = requests.get(url, params=params, headers=headers)
if response.status_code==200:
    data=response.json()
    retailer_id=data.get("data",{}).get("product",{}).get("tcin","")
    retailer_url=""
    product_name=data.get("data",{}).get("product",{}).get("item",{}).get("product_description",{}).get("title","")
    breadcrumb_list=data.get("data",{}).get("product",{}).get("category",{}).get("breadcrumbs",[])
    breadcrumb=[item.get("name","") for item in breadcrumb_list]
    image_url=data.get("data",{}).get("product",{}).get("item",{}).get("enrichment",{}).get("image_info",{}).get("primary_image",{}).get("url","")
    childdren_list=data.get("data",{}).get("product",{}).get("children",[])
    promo_description=''
    product_description=data.get("data",{}).get("product",{}).get("item",{}).get("product_description",{}).get("downstream_description","")
    country_of_origin=data.get("data",{}).get("product",{}).get("item",{}).get("handling",{}).get("import_designation_description")
    selling_price=data.get("data",{}).get("product",{}).get("price",{}).get("current_retail","")
    regular_price=data.get("data",{}).get("product",{}).get("price",{}).get("current_retail","")
    upc=data.get("data",{}).get("product",{}).get("item",{}).get("primary_barcode","")
    specification_list=data.get("data",{}).get("product",{}).get("item",{}).get("product_description",{}).get("bullet_descriptions",[])
    specification = [desc.split('</B>')[-1].strip() for desc in specification_list]
    grammage=specification[5]
    features=specification[2]
    ingredients=""
    warning=""
    ZIPCODE=""
    rating=data.get("data",{}).get("product",{}).get("ratings_and_reviews",{}).get("statistics",{}).get("rating",{}).get("average","")
    review=data.get("data",{}).get("product",{}).get("ratings_and_reviews",{}).get("statistics",{}).get("rating",{}).get("count","")


