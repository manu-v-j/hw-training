import requests
import json,re
from parsel import Selector
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://thehouseofrare.com',
    'priority': 'u=1, i',
    'referer': 'https://thehouseofrare.com/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'unbxd-device-type': '{ "type":"desktop" , "os": "Linux" , "source": "browser" }',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
}
start=0
product=[]
while len(product)<=300:

    params = {
        'p': 'category_handle_uFilter:"rare-rr-men-shirts"',
        'uid': 'uid-1759297095483-81114',
        'facet.multiselect': 'true',
        'variants': 'true',
        'variants.fields': 'variantId,v_Size,v_availableForSale,v_sku',
        'variants.count': '20',
        'fields': 'title,uniqueId,price,imageUrl,productUrl,meta_my_fields_main_title,handle,images,variants,meta_my_fields_sub_title,compareAtPrice,computed_discount,grouped_products,meta_custom_variant_color_image,meta_my_fields_COLOR,swatch_image_url,meta_custom_gender,meta_custom_best_price,best_price,url,v_sku,gst_saving_amount',
        'spellcheck': 'true',
        'pagetype': 'boolean',
        'start': str(start),
        'rows': '20',
        'sort': '',
    }

    response = requests.get(
        'https://search.unbxd.io/e94cac92f0f2da84ae5ca93f42a57658/ss-unbxd-aapac-prod-shopify-houseofrare58591725608684/category',
        params=params,
        headers=headers,
    )
    data=response.json()
    product_list=data.get('response',{}).get('products',[])
    for item in product_list:
        url=item.get('productUrl','')
        full_url=f"https://thehouseofrare.com/collections/rare-rr-men-shirts/{url}"
        print(full_url)
        product.append(full_url)
    
    start+=20


base_url="https://thehouseofrare.com/products/layerr-26-mens-shirt-dark-brown"
response=requests.get(base_url,headers=headers)
sel=Selector(text=response.text)
product_name=sel.xpath("//div[contains(@class,'product-heading')]//text()").getall()
selling_price=sel.xpath("//span[@class='money']/text()").get()
size=sel.xpath("//span[@class='size-title']/text()").getall()
product_description=sel.xpath("//div[contains(text(),'Description')]/following-sibling:: div //text()").getall()
manufacturer_address=sel.xpath("//div[text()='Manufacturer Details']/following-sibling::div//text()").getall()
breadcrumb=sel.xpath("//nav[@class='breadcrumb']//text()").getall()
image_url=sel.xpath("//a[@id='main-zoom-image-js']/@href").getall()
color=sel.xpath("//div[@class='color-title']/text()").getall()
