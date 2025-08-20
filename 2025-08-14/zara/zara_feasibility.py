
import re
import json
from curl_cffi import requests
from parsel import Selector

def bypass_akamai(session, url, headers):
    r = session.get(url, headers=headers, impersonate="chrome")
    
    if "bm-verify" not in r.text:
        return r  
    
    
    token = re.search(r'"bm-verify":\s*"([^"]+)"', r.text)
    token = token.group(1) if token else None
    
    # Extract i and j calculation
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

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
}

#########################CATEGORY##############################################

# with requests.Session() as s:
#     url = "https://www.zara.com/ae"
#     response = bypass_akamai(s, url, headers)
#     sel=Selector(text=response.text)
#     category_urls=sel.xpath("//li[contains(@class,'layout-categories-category') and contains(@data-layout,'products-category-view')]/a/@href").getall()
#     print(category_urls)



#########################CRAWLER###############################################
# product_link=[]
# page=1
# while True:
#     with requests.Session() as s:
#         url=f"https://www.zara.com/ae/en/man-shirts-l737.html?page={page}"
#         response = bypass_akamai(s, url, headers)
#         sel=Selector(text=response.text)
#         product_urls=sel.xpath("//a[contains(@class,'product-grid-product__link link')]/@href").getall()
#         print(len(product_urls))
#         if not product_urls:
#             break
#         print(url)
#         for url in product_urls:
#             product_link.append(url)

#         page+=1


########################PARSER###############
with requests.Session() as s:
    url="https://www.zara.com/ae/en/faded-sweatshirt-p03253345.html"
    response = bypass_akamai(s, url, headers)
    if response.status_code==200:
        sel=Selector(text=response.text)
        prices=sel.xpath("//span[@class='money-amount__main']/text()").get()

        script_text = sel.xpath('//script[@data-compress="true"]/text()').get()
        match = re.search(r'"productId":(\d+)', script_text)
        product_id=''
        if match:
            product_id = match.group(1)
        category_match=re.search(r'"section":"([^"]+)"', script_text)
        department=''
        if category_match:
            department = category_match.group(1)
        sub_department=''
        product_description=sel.xpath("//div[@class='expandable-text__inner-content']/p/text()").get()
        color=sel.xpath("//p[contains(@class,'product-color-extended-name ')]/text()").get()
        product_type=''



