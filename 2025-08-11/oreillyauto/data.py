from settings import headers, MONGO_URL, MONGO_DB, CATAEGORY_COLLECTION, COLLECTION
import requests
from parsel import Selector
from pymongo import MongoClient,errors
import re, json, json5, logging
import logging
logging.basicConfig(level=logging.INFO)

url='https://www.oreillyauto.com/detail/c/challenger-lifts/tools---equipment/lift-equipment/lift---4-post-above-ground/f0eb6fd291cf/challenger-lifts-4-post-lift/cgl0/4030eax'
response=requests.get(url,headers=headers)
if response.status_code==200:
    sel=Selector(text=response.text)
    product_name=sel.xpath("//h1[contains(@class,'js-ga-product-name')]/text()").get()
    script_one=sel.xpath("//script[@type='application/ld+json'][3]/text()").get()
    json_data_one = json.loads(script_one)
    product_description = json_data_one.get('description', '')
    upc=json_data_one.get('sku','')
    brand=json_data_one.get('brand',{}).get('name','')
    image=sel.xpath("//script[contains(text(), 'primaryImage')]/text()").get()
    image_url = ''
    if image:
        match = re.search(r"primaryImage\s*=\s*'([^']+)'", image)
        if match:
            image_url = match.group(1)
            if image_url.startswith("//"):
                image_url = "https:" + image_url

    brand_information_js=sel.xpath("//script[contains(text(), 'brandInformation')]/text()").get()
    brand_match = re.search(r"window\._ost\.brandInformation\s*=\s*'(.*?)';", brand_information_js, re.S)
    brand_information = brand_match.group(1).replace("\\'", "'") if brand_match else ''  

    breadcrumb_script=sel.xpath("//script[contains(text(),'breadcrumbs.push')]/text()").getall()
    desired_order = [-1000, 3500, 3501, 4000]

    breadcrumbs = {}

    for script in breadcrumb_script:
        matches = re.findall(r"'sequenceNumber':(-?\d+).*?'text':'([^']+)'", script, re.DOTALL)
        for seq, text in matches:
            seq = int(seq)
            if seq in desired_order:
                breadcrumbs[seq] = text

    breadcrumb = [breadcrumbs[seq] for seq in desired_order if seq in breadcrumbs]

    print(breadcrumb)