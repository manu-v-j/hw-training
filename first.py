from curl_cffi import requests
from parsel import Selector
import time

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

cookies = {
    
    'ak_bmsc': '952DBDD72DFCDA7EDA1298D26C7FCAB5~000000000000000000000000000000~YAAQHbxWaOJ1/aaYAQAAbFG/wBzRp7I7Pj6yGg4w+xHAAI48HPSzWRSvdm35qsKfaJGwoF3KdgbLwXrO/4F7c4uuO1QWUl4RwnMxrCYqz64BGcMo/9j/j4UfF7QetIiiZrj8MkYMKLGEWAQHgKGNXocHbglWw4sxPBvZLWKl4FTfHPsReemjVvCwyz9JBmb3spYy+dpGGO2BelB1BvsIucH9Ots2bYj2WYVpG8kdPXcIdDpcOj9at/HMFWO1gvh78ji5Lo5nHxqwwjNBggs2lDw5V8IXV4Th4s/+oeGWHVensoy7kqzdEQ4jHA0zSSc/9ajDejx6jbpYgaxqSN965cxTFVYbsy9liTn8MgaiAyZC7uZGFI0+ljSRHxI/Ixev4z/pkSaDDdfX/uoSNMdmw303FASM6H92jsu2zocU1AfIB5YyhwxRPWN6CejUHXrkby3ED7jy6FCYnGEx5htGhoMxz7BLdIb6myPWsIePjYgOnUIzd011fPyTFdS5zlfdogQQZ2LU1sLhojgPdZWXDQupWQY2I9izYRKKl63kbAmqC1n1',
}
# with requests.Session() as s:
#     s.headers.update(headers)

#     home_url = "https://www.zara.com/ae/en"
#     r = s.get(home_url, impersonate="chrome")
#     print("Initial:", r.status_code)

#     category_url = "https://www.zara.com/ae/en/man-shirts-l737.html"
#     r = s.get(category_url, impersonate="chrome")
#     print("Category:", r.status_code)
#     sel=Selector(text=r.text)
#     print("Cookies after category:", s.cookies.get_dict()) 
#     category_urls=sel.xpath("//li[contains(@class,'layout-categories-category') and contains(@data-layout,'products-category-view')]/a/@href").getall()
#     print(category_urls)




# from playwright.sync_api import sync_playwright
# from curl_cffi import requests
# from parsel import Selector
# import time


# def get_zara_session():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()

#         # Homepage
#         page.goto("https://www.zara.com/ae/en", wait_until="domcontentloaded")
#         page.wait_for_selector("body")
#         time.sleep(6)

#         # Category
#         page.goto("https://www.zara.com/ae/en/man-shirts-l737.html", wait_until="domcontentloaded")
#         page.wait_for_selector("body")
#         time.sleep(6)

#         cookies = context.cookies()
#         cookie_dict = {c["name"]: c["value"] for c in cookies}
#         headers = {
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#             'accept-language': 'en-US,en;q=0.9',
#             'cache-control': 'max-age=0',
#             'priority': 'u=0, i',
#             'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Linux"',
#             'sec-fetch-dest': 'document',
#             'sec-fetch-mode': 'navigate',
#             'sec-fetch-site': 'same-origin',
#             'sec-fetch-user': '?1',
#             'upgrade-insecure-requests': '1',
#             'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
#         }

#         browser.close()
#         return headers, cookie_dict


# if __name__ == "__main__":
#     headers, cookies = get_zara_session()
#     print(cookies)
#     with requests.Session() as s:
#         s.headers.update(headers)
#         s.cookies.update(cookies)

#         url = "https://www.zara.com/ae/en/man-shirts-l737.html"
#         r = s.get(url, impersonate="chrome")
#         print("Status:", r.status_code)

#         sel = Selector(text=r.text)
#         category_urls = sel.xpath("//li[contains(@class,'layout-categories-category')]//a/@href").getall()
#         print(category_urls)


# from curl_cffi import requests
# from parsel import Selector


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
    
    print(" Verification POST:", vr.status_code, session.cookies.get_dict())
    
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

with requests.Session() as s:
    url = "https://www.zara.com/ae/en/man-shirts-l737.html"
    response = bypass_akamai(s, url, headers)
    
    # print("Final status:", response.status_code)
    # print("Cookies after bypass:", s.cookies.get_dict())
    sel=Selector(text=response.text)
    product_urls=sel.xpath("//a[contains(@class,'product-grid-product__link link')]/@href").getall()
    print(product_urls)
