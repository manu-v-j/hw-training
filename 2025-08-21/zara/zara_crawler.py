from curl_cffi import requests
from parsel import Selector
from settings import headers,MONGO_URL,MONGO_DB,CATAEGORY_COLLECTION,COLLECTION
import re,json
from pymongo import MongoClient,errors
import logging
logging.basicConfig(level=logging.INFO)

class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]
        self.collection.create_index('link',unique=True)

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
        
        r2 = session.get(url, headers=headers, impersonate="chrome")
        return r2

    def start(self):
        with requests.Session() as s:
            for item in self.db[CATAEGORY_COLLECTION].find(): 
                base_url = item.get('link')
                page = 1
                while True:
                    url = f"{base_url}?page={page}"
                    print(url)
                    response = self.bypass_akamai(s, url, headers)
                    if response.status_code==200:
                        has_products=self.parse_item(response)
                        if not has_products:
                            break
                        page += 1
                    else:
                        break
                    
    def parse_item(self,response):
        sel = Selector(text=response.text)
        product_urls = sel.xpath("//a[contains(@class,'product-grid-product__link')]/@href").getall()
        if not product_urls:
            return False
        for url in product_urls:
            try:
                self.collection.insert_one({'link':url})
                logging.info(url)

            except errors.DuplicateKeyError:
                logging.info(f"Duplicate: {url}")
                      
        return product_urls           

if __name__=='__main__':
    crawler=Crawler()
    crawler.start()
