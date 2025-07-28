from curl_cffi import requests
from parsel import Selector
import html
import json
import re
import logging
logging.basicConfig(level=logging.INFO)
headers={
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'priority':'u=0,i',
    'referer':'https://www.oreillyauto.com/shop/b/accessories/atv---motorcycle-accessories/338fb64b0473',
    'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'Linux',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1'
    
}

############################################CRAWLER########################################
# page=1
# while True:
#     url=f'https://www.oreillyauto.com/shop/b/battery---accessories/batteries/31624da3221a?page={page}'
#     print(page)
#     response=requests.get(url,headers=headers)
#     sel=Selector(text=response.text)
#     product_urls=sel.xpath("//a[@class='js-product-link product__link']/@href").getall()
#     if not product_urls:
#         break
#     for url in product_urls:
#         full_url=f"https://www.oreillyauto.com{url}"
#         print(full_url)
        
#     page+=1


###########################################PARSER$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
url='https://www.oreillyauto.com/detail/c/platinum/battery---accessories/batteries/31624da3221a/super-start-platinum-agm-top-post-battery-group-size-140r-h4-535-cca-80-minute-rc/ssbq/140rplt'
response=requests.get(url,headers=headers)
if response.status_code==200:
    sel=Selector(text=response.text)
    product_name=sel.xpath("//h1[contains(@class,'js-ga-product-name')]/text()").get()
    script_one=sel.xpath("//script[@type='application/ld+json'][3]/text()").get()
    json_data_one = json.loads(script_one)
    product_description = json_data_one.get('description', '')
    upc=json_data_one.get('sku','')
    brand=json_data_one.get('brand',{}).get('name','')
    image=sel.xpath("//script[contains(text(), 'primaryImage')]/text()").get()
    image_url = ''
    if image:
        match = re.search(r"primaryImage\s*=\s*'([^']+)'", image)
        if match:
            image_url = match.group(1)
            if image_url.startswith("//"):
                image_url = "https:" + image_url

    brand_information_js=sel.xpath("//script[contains(text(), 'brandInformation')]/text()").get()
    brand_match = re.search(r"window\._ost\.brandInformation\s*=\s*'(.*?)';", brand_information_js, re.S)
    brand_information = brand_match.group(1).replace("\\'", "'") if brand_match else ''  

    breadcrumb_script=sel.xpath("//script[contains(text(),'breadcrumbs.push')]/text()").getall()
    breadcrumb= []
    for script in breadcrumb_script:
        matches = re.findall(r"'text':'([^']+)'", script)
        breadcrumb.extend(matches)

    script_content = sel.xpath("//script[contains(text(),'window._ost.epcAttributes')]/text()").get()
    attr_match = re.search(r"window\._ost\.epcAttributes\s*=\s*(\[[^\]]+\]);", script_content, re.S)
    attributes_data = attr_match.group(1).strip() if attr_match else ""

    if attributes_data:
        attributes_data = attributes_data.replace("'", '"')  
        attributes_data = re.sub(r'(\w+):', r'"\1":', attributes_data) 
        attributes = json.loads(attributes_data)
    else:
        attributes = []

    product_specification= {
        "attributes": {attr["attributeKey"]["description"]: attr["attributeValue"]["description"] for attr in attributes},
    }

    warranty_raw = sel.xpath("//product-details/@data-warranty-data").get()
    warranty_json = html.unescape(warranty_raw)
    warranty_data = json.loads(warranty_json)
    warranty=warranty_data.get('warranty')



