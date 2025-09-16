import requests
from parsel import Selector
from settings import headers,cookies
import json,re,html


# products=[]
# page=1
# max_page=20
# while page<=max_page:
#     base_url = f'https://www.oreillyauto.com/shop/b/ignition---tune-up/spark-plugs/b14eb31b13d7?page={page}'
#     response = requests.get(base_url, headers=headers)
#     print("Scraping:", base_url)

#     sel = Selector(text=response.text)
#     product_links = sel.xpath("//a[@class='js-product-link product__link']/@href").getall()

#     for url in product_links:
#         full_url = f"https://www.oreillyauto.com{url}"
#         print(full_url)
#         products.append(full_url) 
#         pass
#     page+=1



# #########################PARSER##########################
base_url="https://www.oreillyauto.com/detail/c/iridium-xp/ignition---tune-up/spark-plugs/b14eb31b13d7/autolite-iridium-xp-spark-plug/ato6/xp104"
response=requests.get(base_url,headers=headers)
if response.status_code==200:
    sel=Selector(text=response.text)
    product_name=sel.xpath("//h1[contains(@class,'page-title')]/text()").get()
    part=sel.xpath("//dd[contains(@class,'js-ga-product-line-number')]/text()").get()
    line=sel.xpath("//dd[contains(@class,'js-ga-product-line-code')]/text()").get()
    payload = {
                    'pricingLineCodeItemNumbers': [
                        {
                            'itemNumber': f'{part}',
                            'lineCode': f'{line}',
                        },
                    ],
                    'availabilityLineCodeItemNumbers': [
                        {
                            'itemNumber': f'{part}',
                            'lineCode': f'{line}',
                        },
                    ],
                }
    res = requests.post(
        'https://www.oreillyauto.com/product/pricing-availability/v2',
        cookies=cookies,
        headers=headers,
        json=payload,
        )
    data = res.json()
    key = f"{line}-{part}"

    selling_price = data.get("pricingMap", {}).get(key, {}).get("salePrice", "")
    if selling_price:
        selling_price = f"{float(selling_price):.2f}"
    regular_price=data.get("pricingMap", {}).get(key, {}).get("retailPrice", "")
    if regular_price:    
        regular_price = f"{float(regular_price):.2f}"

    script_one=sel.xpath("//script[@type='application/ld+json'][3]/text()").get()
    json_data_one = json.loads(script_one)
    upc=json_data_one.get('sku','')
    brand=json_data_one.get('brand',{}).get('name','')
    image_script=sel.xpath("//script[contains(text(), 'primaryImage')]/text()").get()
    image_url = ''
    if image_script:
        match = re.search(r"primaryImage\s*=\s*'([^']+)'", image_script)
        if match:
            image_url = match.group(1)
            if image_url.startswith("//"):
                image_url = "https:" + image_url      

    details=sel.xpath("//script[contains(text(),'window._ost.description')]/text()").get()
    product_description = ''
    if details:
            match = re.search(r"window\._ost\.description\s*=\s*'(.*?)';", details, re.DOTALL)
            if match:
                raw_desc = match.group(1)
                raw_desc = raw_desc.replace("\\/", "/").replace('\\"', '"')

                raw_desc = re.sub(r"<\s*li\s*>", ", ", raw_desc, flags=re.IGNORECASE)
                raw_desc = re.sub(r"</?\s*(p|ul|li)\s*>", " ", raw_desc, flags=re.IGNORECASE)

                product_description = Selector(text=raw_desc).xpath("string(.)").get()

                product_description = re.sub(r"\s*,\s*", " ", product_description).strip()
                product_description = re.sub(r"\s+", " ", product_description).strip()

    breadcrumb_script=sel.xpath("//script[contains(text(),'breadcrumbs.push')]/text()").getall()
    desired_order = [-1000, -500, 2500,2501,2502, 4000]

    breadcrumbs = {}
    for script in breadcrumb_script:
        matches = re.findall(r"sequenceNumber':(-?\d+).*?'text':'([^']+)'", script, re.DOTALL)
        for seq, text in matches:
            seq = int(seq)
            if seq in desired_order:
                if seq == -500:
                    text = f"search for '{text}'"
                breadcrumbs[seq] = text
    breadcrumb = [breadcrumbs[seq] for seq in desired_order if seq in breadcrumbs]
    breadcrumb = ' > '.join(breadcrumb)

    brand_informatiom = ''
    if details:
            match = re.search(r"window\._ost\.brandInformation\s*=\s*'(.*?)';", details, re.DOTALL)
            if match:
                raw_desc = match.group(1)
                raw_desc = raw_desc.replace("\\/", "/").replace("\\'", "'")
                brand_informatiom = Selector(text=raw_desc).xpath("string(.)").get()
                brand_informatiom = re.sub(r"\s*,\s*", " ", brand_informatiom).strip()
                brand_informatiom = re.sub(r"\s+", " ", brand_informatiom).strip()

    warranty_row=sel.xpath("//product-details/@data-warranty-data").get()
    warranty_json = html.unescape(warranty_row)
    warranty_data = json.loads(warranty_json)
    warranty=warranty_data.get('warranty','')
    print(image_url)