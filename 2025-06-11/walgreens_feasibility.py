import requests
from parsel import Selector
import re
import json

cookies={
  "v2H": "t",
  "shop": "aem",
  "s_fid": "43EA4ADDC8C16D5B-2EF521932052DA72",
  "rvi": "prod6018396-prod6393228-prod5816033-300434400-300433947-300442613-300442614-prod6212605-300429178-prod6286387-prod6017176-300436121-prod6291622-prod6335256",
  "__gads": "ID=5e460f8d6260f2f5:T=1749632040:RT=1749804772:S=ALNI_MbTFyqS9eIvIROe-7d2kOzcCbmCuQ",
  "__gpi": "UID=000011297efc274f:T=1749632040:RT=1749804772:S=ALNI_Ma46AdkA51A4QPe7nABNJC3bEEZ8Q",
  "__eoi": "ID=a4ce20b41a41c6a0:T=1749632040:RT=1749804772:S=AA-AfjZngERovZp_sGONkHZmZ7uH",
  "AKA_A2": "A",
  "XSRF-TOKEN": "1QGeI9sbrE3Arg==.26ckxw0GD44jNRWWUEYZpJYAhdhWYv6BFeaw/OxFhsk=",
  "wag_sid": "yz8jschoqk4sv7aw03i4m1da",
  "alg_idx_qry": "{\"indexNames\":[\"productSku\"],\"queryIds\":[\"e048273233b5234199a649d1949e54fd\"],\"abTests\":[{\"indexName\":\"productSku\",\"abTestID\":89003,\"abTestVariantID\":2}]}",
  "s_ppv": "Walgreens%2520%257C%2520Walgreens,8,7,7,1285,45,2",
  "akavpau_walgreens": "1749904132~id=540a25791b0d78255610fc06234ca434",
  "ak_bmsc": "5976251A5ED1B46A5AF578A32F1CD7A9~000000000000000000000000000000~YAAQtULHF1zM2FqXAQAAv3Rlbhyghi5sLT309XEvlHTuv5GO47paojyD3u7QFh4XKDxlt87QLp1wcMqxCTDeawDmfTzscieAHnlkKKCaqGEuQDABI2ZDw40iYyb2x1cYb/5Lb/nmFCtIc4izFb8eQyIq2okItjpmwEG97juN0XK60ePPDielzGHuvdDnkcpISCoErdNOkxffkfL7uLBorLIB1Rpld4AEc7aoUyo4eo45jMINkhmD3OwWcKBFkOLTeeYksdZzGyDgkjU/1UmKVz79dNsbxWRRV1j6yYaxdAEwWouENWysl3fmiouQ2DzV1qS8BXkF6ovsmBLtgxuAOKQ+3bBwT/pYHsUl+XEI9/bM+u/270mdU0co4uIrOQ9HHJ4SX7HnlQ0vDkR8R441TgeShjI3mt8iAmnGCqzApjttADA6ANmESa9bq813dgsMIlFYNi3Tv6l0SjpS9m536WJah2AAPd4D7igkmS6WUexvaYUdG7+SDl5Bm7NT/ffjOsZ/AEwL3EpOQntjvlo8//pu5Gi4oXjyKV+zjSBtr3207TjWVd3VgTnPIw=="
}

##############################CRAWLER##############################

count=0
payload = {
                "id": ["20003545", "360545"]
        }

response=requests.post('https://www.walgreens.com/productsearch/v1/categories',json=payload)
data=response.json()
category=data.get("categories",[])
for item in category:
    category_url=item.get("url","")
    full_url=f"https://www.walgreens.com{category_url}"
    print(full_url)
    response=requests.get(full_url,headers=headers,cookies=cookies)
    sel=Selector(text=response.text)
    script_content = sel.xpath('//script[contains(text(), "window.getInitialState")]/text()').get()

    if script_content:
        json_match = re.search(r'return\s*(\{.*})', script_content, re.DOTALL)
        match=json_match.group(1)
        if match.endswith('}'):
            match=match[:-1]
            data=json.loads(match)
            result_list=data.get("searchResult",{}).get("productList",[]) 
            for item in result_list:
                product_url=item.get("productInfo",{}).get("productURL","")
                # print(f"https://www.walgreens.com{product_url}")
                count+=1
                print(count)


###############################PARSER##############################
response=requests.get("https://www.walgreens.com/store/c/walgreens-neti-pot-kit/ID=prod6335256-product")
sel=Selector(text=response.text)
script=sel.xpath("//script[@type='application/ld+json']/text()").get()
data=json.loads(script)
product_name=data.get("name","")
unique_id=data.get("prodID","")
product_sku=data.get("sku")
brand=data.get("brand",{}).get("name","")
brand_type=data.get("brand",{}).get("@type","")
offers_list=data.get("offers",[])
rating=data.get("aggregateRating",{}).get("ratingValue","")
review=data.get("aggregateRating",{}).get("reviewCount","")
image_url=data.get("image",[])
for item in offers_list:
    selling_price=item.get("price","")
    currency=item.get("priceCurrency","")
    pdp_url=item.get("url","")
    instock=item.get("availability","")


# from curl_cffi import requests
# count=0

# response=requests.get("https://www.walgreens.com/store/c/productlist/N=360545/1/ShopAll=360545",cookies=cookies)
# sel=Selector(text=response.text)
# script_content = sel.xpath('//script[contains(text(), "window.getInitialState")]/text()').get()

# if script_content:
#     json_match = re.search(r'return\s*(\{.*})', script_content, re.DOTALL)
#     match=json_match.group(1)
#     if match.endswith('}'):
#         match=match[:-1]
#         data=json.loads(match)
#         result_list=data.get("searchResult",{}).get("productList",[]) 
#         for item in result_list:
#             product_url=item.get("productInfo",{}).get("productURL","")
#             print(f"https://www.walgreens.com{product_url}")
#             count+=1
#             print(count)
