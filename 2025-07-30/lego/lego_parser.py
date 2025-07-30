import requests
from parsel import Selector
from settings import headers
import json
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
        FEATURES_XPATH="//div[contains(@class,'ProductAttributesstyles__ValueWrapper-sc-1sfk910-5')]/p/text()"
        PRODUCT_DESCRIPTION_XPATH="//div[@class='ProductFeaturesstyles__FeaturesText-sc-tutz3a-2 cePksm']//text()"
        product_name=sel.xpath(PRODUCT_NAME_XPATH).get()
        selling_price_raw=sel.xpath(SELLING_PRICE_XPATH_RAW).get()
        regular_price_raw=sel.xpath(REGULAR_PRICE_XPATH_RAW).get()
        # features=sel.xpath(FEATURES_XPATH).getall()
        # proudct_specification=sel.xpath(PRODUCT_DESCRIPTION_XPATH).getall()
        script=sel.xpath("//script[@id='__NEXT_DATA__']/text()").get()
        logging.info(script)
        data = json.loads(script)

        output_file = "lego_data.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

if __name__=='__main__':
    parser=Parser()
    parser.start()