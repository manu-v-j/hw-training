import requests
from parsel import Selector
import re
import json


headers = {
    "authority": "www.walgreens.com",
    "method": "GET",
    "path": "/store/c/allergy-medicine/ID=361485-tier3",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "v2H=t; wag_sid=etm3kda9whk4c7xzi7gcdqnt; ... (TRUNCATED FOR BREVITY)",
    "priority": "u=0, i",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
}
count=0
url="https://www.walgreens.com/shop"
response=requests.get(url)
sel=Selector(text=response.text)
payload = {
                "id": ["20003545", "360545"]
        }

response=requests.post('https://www.walgreens.com/productsearch/v1/categories',json=payload)
data=response.json()
category=data.get("categories",[])
for item in category:
    category_url=item.get("url","")
    full_url=f"https://www.walgreens.com{category_url}"
    response=requests.get(full_url)
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
                print(f"https://www.walgreens.com{product_url}")
                count+=1
                print(count)


# response=requests.get("https://www.walgreens.com/store/c/productlist/N=360545/1/ShopAll=360545")
# sel=Selector(text=response.text)
# print(sel)
# # with open("result.html","w") as f:
# #     f.write(response.text)
# product_list = sel.xpath("//div[@class='product__text-title-contain']").getall()

# for product_html in product_list:
#     product_sel = Selector(text=product_html)
#     product_link = product_sel.xpath(".//a[@class='color__text-black']/@href").get()
#     print(f"https://www.walgreens.com{product_link}")


###############################PARSER##############################
# response=requests.get("https://www.walgreens.com/store/c/walgreens-neti-pot-kit/ID=prod6335256-product")
# sel=Selector(text=response.text)
# script=sel.xpath("//script[@type='application/ld+json']/text()").get()
# data=json.loads(script)
# product_name=data.get("name","")
# unique_id=data.get("prodID","")
# product_sku=data.get("sku")
# brand=data.get("brand",{}).get("name","")
# brand_type=data.get("brand",{}).get("@type","")
# offers_list=data.get("offers",[])
# rating=data.get("aggregateRating",{}).get("ratingValue","")
# review=data.get("aggregateRating",{}).get("reviewCount","")
# image_url=data.get("image",[])
# for item in offers_list:
#     selling_price=item.get("price","")
#     currency=item.get("priceCurrency","")
#     pdp_url=item.get("url","")
#     instock=item.get("availability","")




# url="https://www.walgreens.com/shop"
# response=requests.get(url)
# sel=Selector(text=response.text)
# category_links=sel.xpath("//li[@class='labelledIconContainer']/a/@href").getall()

# for idx, link in enumerate(category_links):
#     match = re.search(r'ID=(\d+)', link)
#     if match:
#         id_value = match.group(1)
#         if idx == 0:
#             payload = {
#                 "id": ["20003545", id_value]
#             }
#         else:
#             payload = {
#                 "id": [id_value]
#             }

#         category_links=[]
#         response=requests.post('https://www.walgreens.com/productsearch/v1/categories',json=payload)
#         data=response.json()
#         category=data.get("categories",[])
#         for item in category:
#             category_url=item.get("url","")
#             full_url=f"https://www.walgreens.com{category_url}"
#             # print(full_url)
#             response=requests.get(full_url)
#             sel=Selector(text=response.text)
#             product_list = sel.xpath("//div[@class='product__text-title-contain']").getall()

#             for product_html in product_list:
#                 product_sel = Selector(text=product_html)
#                 product_link = product_sel.xpath(".//a[@class='color__text-black']/@href").get()
#                 print(f"https://www.walgreens.com{product_link}")

#         category_links=[]
#         response=requests.post('https://www.walgreens.com/productsearch/v1/categories',json=payload)
#         data=response.json()
#         category=data.get("categories",[])
#         for item in category:
#             category_url=item.get("url","")
#             full_url=f"https://www.walgreens.com{category_url}"
#             print(full_url)
#             response=requests.get(full_url)
#             sel=Selector(text=response.text)
#             product_list = sel.xpath("//div[@class='product__text-title-contain']").getall()

#             for product_html in product_list:
#                 product_sel = Selector(text=product_html)
#                 product_link = product_sel.xpath(".//a[@class='color__text-black']/@href").get()
#                 print(f"https://www.walgreens.com{product_link}")


# response = requests.get("https://www.walgreens.com/store/c/allergy-medicine/ID=361485-tier3", headers=headers)
# sel = Selector(text=response.text)

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
#             print(product_url) 
      
