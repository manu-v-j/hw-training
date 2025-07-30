import requests
from parsel import Selector
from settings import headers
import json
import re
import logging
logging.basicConfig(level=logging.INFO)

class Parser:
    def __init__(self):
        pass

    def start(self):
        url='https://www.lego.com/en-gb/product/izzie-s-dream-animals-71481'
        response=requests.get(url,headers=headers,verify=False)
        if response.status_code==200:
            self.parse_item(response)
    def parse_item(self,response):
        sel=Selector(text=response.text)

        #XPATH
        PRODUCT_NAME_XPATH="//h1[contains(@class,'ProductOverviewstyles__NameText-sc-1wfukzv-5')]/span/text()"
        SELLING_PRICE_XPATH_RAW="//span[contains(@class,'ProductPrice_salePrice__L9pb9')]/text()"
        REGULAR_PRICE_XPATH_RAW="//span[contains(@class,'ProductPrice_regularPrice__NVDdO')]/text()"
        IMAGE_URL_XAPTH_RAW="//picture[@class='ProductGallery_styledPicture__wQV8N']/source/@srcset"
        SCRIPT_XPATH="//script[@id='__NEXT_DATA__']/text()"
        #EXTRACT
        product_name=sel.xpath(PRODUCT_NAME_XPATH).get()
        selling_price_raw=sel.xpath(SELLING_PRICE_XPATH_RAW).get()
        regular_price_raw=sel.xpath(REGULAR_PRICE_XPATH_RAW).get()
        image_url_raw=sel.xpath(IMAGE_URL_XAPTH_RAW).get()
        script=sel.xpath(SCRIPT_XPATH).get()

        #CLEAN
        data = json.loads(script)
        details=data.get('props',{}).get('pageProps',{}).get('__APOLLO_STATE__',{})
        product_details=data.get('props',{}).get('pageProps',{}).get('__APOLLO_STATE__',{}).get('SingleVariantProduct:63963864-019f-4fa8-9c77-7a21202e3b6f',{})
        unique_id=product_details.get('productCode','')
        id=product_details.get('variant',{}).get('id','')
        match = re.search(r'\d+', id)
        if match:
            id=match.group()
        product_description=product_details.get('featuresText','')
        desc_selector = Selector(text=product_description)
        description = " ".join(desc_selector.xpath("//p/text() | //li/text()").getall()).strip()
        product_attribute=data.get('props',{}).get('pageProps',{}).get('__APOLLO_STATE__',{}).get(f'ProductVariant:{id}',{})
        features=data.get('props',{}).get('pageProps',{}).get('__APOLLO_STATE__',{}).get(f'$ProductVariant:.attributes6470378',{})

        point=product_attribute.get('vipPoints','')
        # print(description)
        availability=sel.xpath("//span[@class='ds-body-md-medium']/text()").getall()
        single_variant_keys = [key for key in details.keys() if key.startswith('SingleVariantProduct:')]
        print(id)
        print(details.keys())
        print(f'ProductVariant:{id}')

if __name__=='__main__':
    parser=Parser()
    parser.start()