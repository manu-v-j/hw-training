from curl_cffi import requests
import json
from parsel import Selector
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.northernsafety.com',
    'Referer': 'https://www.northernsafety.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'x-algolia-api-key': 'ZmUxYjcxZjZmZDg0M2QzYmVkNzc3ZjhkY2EyOWEyODkxMzg0YmVlOTgwODBhYzQ4MDM5M2QxN2E4NjVkYTM5OWZpbHRlcnM9SXNQcml2YXRlJTNBZmFsc2UmdmFsaWRVbnRpbD0xNzU3Mzg5MTk1',
    'x-algolia-application-id': 'I45I79OC23',
}




##########################CRAWLER#######################
import urllib.parse
import re
import requests
product_links=[]
url = "https://www.northernsafety.com/Search/Safety-Products/Clothing/Chemical-Resistant-Clothing---Accessories"
parts = [s for s in url.split("/") if s][3:]

category, subcategory, product = parts

product_text = product.replace("---", " & ")

category_text = category.replace("-", " ")
subcategory_text = subcategory.replace("-", " ")
product_text = product_text.replace("-", " ")

page = 0
while True:
    
    facet_string = f"Categories.lvl2:{category_text} > {subcategory_text} > {product_text}"

    facet_encoded = urllib.parse.quote(facet_string)
    print(facet_encoded)
    payload = {
        "requests": [
            {
                "indexName": "WebProd",
                "params": f"clickAnalytics=true&facetFilters=%5B%5B%22{facet_encoded}%22%5D%5D"
                          f"&facets=%5B%22*%22%5D&highlightPostTag=__%2Fais-highlight__"
                          f"&highlightPreTag=__ais-highlight__&hitsPerPage=24"
                          f"&maxValuesPerFacet=1000&page={page}&query="
                          f"&userToken=anonymous-1fbeff5e-5573-44f7-a7e8-83dc7e7bc75d&analytics=true"
            }
        ]
    }

    response = requests.post(
        "https://i45i79oc23-1.algolianet.com/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.23.2)%3B%20Browser",
        headers=headers,
        json=payload)  

    data = response.json()
    result_list = data.get('results', [])

    for list in result_list:
        hits_list = list.get('hits', [])
        for item in hits_list:
            hits_found = True
            product_url = item.get('MaterialDetailPageURL', '')
            full_url = f"https://www.northernsafety.com{product_url}"
            print(full_url)
            product_links.append(full_url)

    if not hits_list:
        break  
    page += 1
    print("Page:", page)

print(len(product_links))
######################################PARSER########################
# import requests,re

# url = "https://www.northernsafety.com/Product/27504/NSI-Ruf-flex-Lite/Black-Rubber-Palm-Coated-Nylon-String-Knit-Gloves"
# response = requests.get(url,headers=headers)
# sel=Selector(text=response.text)

# Company_Name='northernsafety'
# Manufacturer_Name=''
# script=sel.xpath("//script[contains(text(),'productDetails:')]/text()").get()
# product_details_json=re.search(r'productDetails:\s*(\{.*\})',script)
# if product_details_json:
#     text=product_details_json.group(1)
#     data=json.loads(text)
#     Brand_Name=data.get('brand','')
#     name=data.get('materialName','')
#     Item_Name=f"{Brand_Name}{name}"

#     lowest_price=data.get('lowestPrice','')
#     highest_price=data.get('highestPrice','')
#     Price=f"{lowest_price}-{highest_price}"

#     vendor_part_number_list=data.get('vendorPartNumbers',[])
#     for item in vendor_part_number_list:
#         vendor_part_number=item.get('partNumber','')

#     product_description=data.get('bulletPoints',[])
#     category_list=data.get('breadcrumbsInfo',{}).get('breadcrumbs',[])
#     product_category=category_list[0].get('title','')

#     status_list=data.get('stockStatuses',[])
#     for s in status_list:
#         if s.get('isAvailable',''):
#             Availability="In Stock"
#         else:
#             Availability="Out of Stock"
#     Unit_of_Issue=Price
#     QTY_Per_UOI = ''
#     for item in data.get("availablePrices", []):
#         for p in item.get("pricings", []):
#             quantity_range = p.get("quantityRange", "")
#             if quantity_range.startswith("1-"):
#                 QTY_Per_UOI = p.get('price','')
#     Manufacturer_Name=Brand_Name
#     Manufacturer_Part_Number=''
#     Country_of_Origin=''
#     UPC=''
#     Model_Number=''    
