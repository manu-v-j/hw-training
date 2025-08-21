from curl_cffi import requests
from parsel import Selector
from zara_items import Product_Item
import re,json,csv
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_DETAILS,COLLLECTION_ERROR
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_DETAILS]
        self.collection_error=self.db[COLLLECTION_ERROR]

    def bypass_akamai(self,session, url, headers):
            r = session.get(url, headers=headers, impersonate="chrome")
            
            if "bm-verify" not in r.text:
                return r  
            
            
            token = re.search(r'"bm-verify":\s*"([^"]+)"', r.text)
            token = token.group(1) if token else None
            
            i_match = re.search(r"var i = (\d+);", r.text)
            concat_match = re.search(r'Number\("(\d+)" \+ "(\d+)"\)', r.text)
            
            if not (token and i_match and concat_match):
                raise RuntimeError("Could not parse Akamai challenge")
            
            i = int(i_match.group(1))
            concat_val = concat_match.group(1) + concat_match.group(2)
            pow_val = i + int(concat_val)
            
            payload = {"bm-verify": token, "pow": pow_val}
            
            verify_url = url.split("/", 3)[:3]
            verify_url = "/".join(verify_url) + "/_sec/verify?provider=interstitial"

            vr = session.post(verify_url, headers=headers, data=json.dumps(payload), impersonate="chrome")
            
            # print(" Verification POST:", vr.status_code, session.cookies.get_dict())
            
            r2 = session.get(url, headers=headers, impersonate="chrome",allow_redirects=False)
            return r2    
    def start(self):
        for item in self.db[COLLECTION].find().limit(1000):
            url=item.get('link')
            with requests.Session() as s:
                response = self.bypass_akamai(s, url, headers)
                if response.status_code==200:
                    self.parse_item(response,url)
                else:
                    self.collection_error.insert_one({'link':url})

    def parse_item(self,response,url):
        sel=Selector(text=response.text)

        #XAPTH
        PRICES_XPATH="//span[@class='money-amount__main']/text()"
        SCRIPT_XPATH="//script[@data-compress='true']/text()"
        PRODUCT_DESCRIPTION_XPATH="//div[@class='expandable-text__inner-content']/p//text()"
        COLOR_XPATH="//p[contains(@class,'product-color-extended-name ')]/text()"

        #EXTRACT
        prices_raw=sel.xpath(PRICES_XPATH).get()
        script_text = sel.xpath(SCRIPT_XPATH).get()
        product_description=sel.xpath(PRODUCT_DESCRIPTION_XPATH).getall()
        color=sel.xpath(COLOR_XPATH).get()

        #CLEAN
        if prices_raw:
            prices=prices_raw.replace(' AED','').replace(',','')
            prices=f"{float(prices):.2f}"
        product_description=' '.join(product_description)
        match = re.search(r'"productId":(\d+)', script_text)
        product_id=''
        if match:
            product_id = match.group(1)
        category_match=re.search(r'"section":"([^"]+)"', script_text)
        department=''
        if category_match:
            department = category_match.group(1)


        item={}
        item['prices']=prices
        item['product_id']=product_id
        item['product_description']=product_description
        item['color']=color
        item['department']=department
        item['sub_department']=''
        item['product_type']=''

        product_item=Product_Item(**item)
        product_item.save()

        logging.info(product_description)


if __name__=='__main__':
    parser=Parser()
    parser.start()