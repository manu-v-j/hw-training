from curl_cffi import requests
from parsel import Selector
from pymongo import MongoClient
from settings import headers,MONGO_DB,MONGO_URI,COLLECTION,DETAILS_COLLECTION,COLLECTION_ERROR
import re,json,logging,time
from homedepot_items import ProductItem
logging.basicConfig(level=logging.INFO)

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[DETAILS_COLLECTION]
        self.collection_error=self.db[COLLECTION_ERROR]
        
    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get('link')
            response=requests.get(url,headers=headers)
            time.sleep(3)
            if response.status_code==200:
                self.parse_item(response,url)
            else:
                self.collection_error.insert_one({'link':url})

    def parse_item(self,response,url):
        sel=Selector(text=response.text)

        #XPATH
        product_name_xpath="//h1[contains(@class,'sui-h4-bold')]/text()"
        selling_price_xpath="//span[@class='sui-font-display sui-leading-none sui-px-[2px] sui-text-9xl sui--translate-y-[0.5rem]']/text()"
        price_was_xpath="//span[@class='sui-line-through']//text()"
        currency_xpath="//span[@class='sui-font-display sui-leading-none sui-text-3xl']/text()"
        percentage_discount_xpath="//span[@class='sui-text-success']/div/span/text()[2]"
        script_xpath="//script[@id='thd-helmet__script--productStructureData']/text()"

        #EXTRACT
        product_name=sel.xpath(product_name_xpath).get()
        selling_price=sel.xpath(selling_price_xpath).get()
        price_was=sel.xpath(price_was_xpath).get()
        currency=sel.xpath(currency_xpath).get()
        percentage_discount=sel.xpath(percentage_discount_xpath).get()
        script=sel.xpath(script_xpath).get()

        product_description = unique_id = product_sku = brand = rating = review = ''
        color = model_number = depth = height = width = weight = ''
        image_url = []
        breadcrumbs = []
        amperage = appliance_series = category = appliance_type = ''
        energy_consumption = tier_rating = handle_type = ''
        if script:
            data=json.loads(script)
            product_description=data.get('description','')
            unique_id=data.get('productID','')
            product_sku=data.get('sku','')
            brand=data.get('brand',{}).get('name','')
            rating=data.get('aggregateRating',{}).get('ratingValue','')
            review=data.get('aggregateRating',{}).get('reviewCount','')
            color=data.get('color','')
            model_number=data.get('model','')
            depth=data.get('depth','')
            height=data.get('height','')
            width=data.get('width','')
            weight=data.get('weight','')
            image_url=data.get('image',[])

        script = sel.xpath("//script[contains(text(), 'window.__APOLLO_STATE__')]/text()").get()
        if script:
            match = re.search(r'\{.*\}', script, re.DOTALL)
            if match:
                json_str = match.group(0)
            data_one=json.loads(json_str)
            breadcrumbs_list=data_one.get(f'base-catalog-{unique_id}',{}).get('taxonomy',{}).get('breadCrumbs',[])
            breadcrumbs=[item.get('label','') for item in breadcrumbs_list]
            group_list=data_one.get(f'base-catalog-{unique_id}',{}).get('specificationGroup',[])
            for group in group_list:
                for spec in group.get('specifications', []):
                    if spec.get('specName') == 'Amperage (A)':
                        amperage = spec.get('specValue', '')
                    
                    if spec.get('specName') == 'Appliance Category':
                        category = spec.get('specValue', '')
                    if spec.get('specName') == 'Appliance Category':
                        category = spec.get('specValue', '')
                    if spec.get('specName') == 'Appliance Series':
                        appliance_series = spec.get('specValue', '')
                    
                    if spec.get('specName') == 'Appliance Type':
                        appliance_type= spec.get('specValue', '')

                    if spec.get('specName') == 'Energy Consumption (kWh/year)':
                        energy_consumption= spec.get('specValue', '')
                    if spec.get('specName') == 'Energy Efficiency Tier Rating':
                        tier_rating= spec.get('specValue', '')
                    if spec.get('specName') == 'Handle Type':
                        handle_type= spec.get('specValue', '')

        #CLEAN
        if percentage_discount:
            percentage_discount=re.sub(r'[()]','',percentage_discount).strip()
        if review is not None:
            review = str(review)
        else:
            review = ''
        if rating is not None:
            rating=str(rating)
        else:
            rating=''
        
        
        item = {}
        item['product_name'] = product_name
        item['selling_price'] = selling_price
        item['price_was'] = price_was
        item['currency'] = currency
        item['pdp_url'] = url
        item['percentage_discount'] = percentage_discount
        item['product_description'] = product_description
        item['unique_id'] = unique_id
        item['product_sku'] = product_sku
        item['brand'] = brand
        item['rating'] = rating
        item['review'] = review
        item['color'] = color
        item['model_number'] = model_number
        item['depth'] = depth
        item['height'] = height
        item['width'] = width
        item['weight'] = weight
        item['image_url'] = image_url
        item['breadcrumbs'] = breadcrumbs
        item['amperage'] = amperage
        item['category'] = category
        item['appliance_series'] = appliance_series
        item['appliance_type'] = appliance_type
        item['energy_consumption'] = energy_consumption
        item['tier_rating'] = tier_rating
        item['handle_type'] = handle_type

        product_item=ProductItem(**item)
        product_item.save()
        logging.info(item)

        
        

if __name__=='__main__':
    parser=Parser()
    parser.start()