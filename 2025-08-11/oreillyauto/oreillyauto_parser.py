import requests
from parsel import Selector
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_DETAILS,cookies
from oreillyauto_items import Product_Item
from pymongo import MongoClient
import json,re,html
import logging,time
logging.basicConfig(level=logging.INFO)

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_DETAILS]

    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get('link')
            reason=item.get('matched')
            response=requests.get(url,headers=headers)
            if response.status_code==200:
                self.parse_item(response,url,reason)
    def parse_item(self,response,url,reason):
        sel=Selector(text=response.text)

        #XPATH
        PRODUCT_NAME_XPATH="//h1[contains(@class,'page-title')]/text()"
        PART_XPATH="//dd[contains(@class,'js-ga-product-line-number')]/text()"
        LINE_XPATH="//dd[contains(@class,'js-ga-product-line-code')]/text()"
        SCRIPT_ONE_XPATH="//script[@type='application/ld+json'][3]/text()"
        IMAGE_XPATH="//script[contains(text(), 'primaryImage')]/text()"
        BREADCRUMB_SCRIPT_XPATH="//script[contains(text(),'breadcrumbs.push')]/text()"
        WARRANTY_XPATH="//product-details/@data-warranty-data"
       
        #EXTRACT
        product_name=sel.xpath(PRODUCT_NAME_XPATH).get()
        part=sel.xpath(PART_XPATH).get()
        line=sel.xpath(LINE_XPATH).get()
        script_one=sel.xpath(SCRIPT_ONE_XPATH).get()
        image=sel.xpath(IMAGE_XPATH).get()
        breadcrumb_script=sel.xpath(BREADCRUMB_SCRIPT_XPATH).getall()
        warranty_raw=sel.xpath(WARRANTY_XPATH).get()

        #CLEAN
        payload = {
                'pricingLineCodeItemNumbers': [
                    {
                        'itemNumber': f'{part}',
                        'lineCode': f'{line}',
                    },
                ],
                'availabilityLineCodeItemNumbers': [
                    {
                        'itemNumber': f'{part}',
                        'lineCode': f'{line}',
                    },
                ],
            }
        res = requests.post(
        'https://www.oreillyauto.com/product/pricing-availability/v2',
        cookies=cookies,
        headers=headers,
        json=payload,
        )
        data = res.json()
        key = f"{line}-{part}"

        selling_price = data.get("pricingMap", {}).get(key, {}).get("salePrice", "")
        if selling_price:
            selling_price = f"{float(selling_price):.2f}"
        regular_price=data.get("pricingMap", {}).get(key, {}).get("retailPrice", "")
        if regular_price:    
            regular_price = f"{float(regular_price):.2f}"


        json_data_one = json.loads(script_one)
        upc=json_data_one.get('sku','')
        brand=json_data_one.get('brand',{}).get('name','')

        image_url = ''
        if image:
            match = re.search(r"primaryImage\s*=\s*'([^']+)'", image)
            if match:
                image_url = match.group(1)
                if image_url.startswith("//"):
                    image_url = "https:" + image_url
                else:
                    image_url = "https://images.oreillyauto.com" + image_url

        description_script = sel.xpath("//script[contains(text(),'window._ost.description')]/text()").get()
        product_description = ''

        if description_script:
            match = re.search(r"window\._ost\.description\s*=\s*'(.*?)';", description_script, re.DOTALL)
            if match:
                raw_desc = match.group(1)

                raw_desc = raw_desc.replace("\\/", "/").replace('\\"', '"')

                raw_desc = re.sub(r"<\s*li\s*>", ", ", raw_desc, flags=re.IGNORECASE)
                raw_desc = re.sub(r"</?\s*(p|ul|li)\s*>", " ", raw_desc, flags=re.IGNORECASE)

                product_description = Selector(text=raw_desc).xpath("string(.)").get()

                product_description = re.sub(r"\s*,\s*", " ", product_description).strip()
                product_description = re.sub(r"\s+", " ", product_description).strip()


        desired_order = [-1000, -500, 2500,2501,2502, 4000]

        breadcrumbs = {}
        for script in breadcrumb_script:
            matches = re.findall(r"sequenceNumber':(-?\d+).*?'text':'([^']+)'", script, re.DOTALL)
            for seq, text in matches:
                seq = int(seq)
                if seq in desired_order:
                    if seq == -500:
                        text = f"search for '{text}'"
                    breadcrumbs[seq] = text
        breadcrumb = [breadcrumbs[seq] for seq in desired_order if seq in breadcrumbs]
        breadcrumb = ' > '.join(breadcrumb)

        warranty_json = html.unescape(warranty_raw)
        warranty_data = json.loads(warranty_json)
        warranty=warranty_data.get('warranty')

        item={}
        item['product_name']=product_name
        item['product_description']=product_description
        item['upc']=upc
        item['brand']=brand
        item['selling_price']=selling_price
        item['regular_price']=regular_price
        item['currency']='USD'
        item['pdp_url']=url
        item['warranty']=warranty
        item['breadcrumb']=breadcrumb
        item['image_url']=image_url
        item['match_reason']=reason

        product_item=Product_Item(**item)
        product_item.save()

        logging.info(product_description)

if __name__=='__main__':
    parser=Parser()
    parser.start()