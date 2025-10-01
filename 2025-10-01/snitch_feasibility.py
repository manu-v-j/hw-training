import requests
import json

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Headers': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.snitch.com',
    'Referer': 'https://www.snitch.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'client-id': 'snitch_secret',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

page=1
product=[]
while len(product)<=100:
    params = {
        'page': str(page),
        'limit': '100',
        '0': '[object Object]',
        'product_type': 'Shirts',
    }

    response = requests.get('https://mxemjhp3rt.ap-south-1.awsapprunner.com/products/plp/v2', params=params, headers=headers)
    print(params)
    data=response.json()
    product_list=data.get('data',{}).get('products',[])
    if not product_list:
        break
    for item in product_list:
        id=item.get('shopify_product_id','')
        handle=item.get('handle','')
        full_url=f"https://www.snitch.com/men-shirts/{handle}/{id}/buy"
        product_name=item.get('title','')
        selling_price=item.get('selling_price','')
        rating=item.get('average_rating','')
        review=item.get('total_rewiews_count','')
        size_list=item.get('variants',[])
        for value in size_list:
            size=value.get('size','')
        product_description=item.get('short_description','')
        fit_guide=item.get('fit','')
        washcare=item.get('washcare','')
        material=item.get('material','')
        image_url=item.get('images',[])
        product.append(full_url)
        print(full_url)
        print(product_name,selling_price)
    page+=1


###############PARSER########################
# base_url="https://mxemjhp3rt.ap-south-1.awsapprunner.com/products/shop-the-look?product_id=8777775841442"
# response=requests.get(base_url,headers=headers)
# data=response.json()
# data = response.json()
# with open('product.json', 'w') as f:
#     json.dump(data, f, indent=4)
# product=data.get('data',{}).get('shop_the_look',[])
# for item in product:
#     if item.get('shopify_product_id','')==8777775841442:
#         product_name=item.get('title','')
#         selling_price=item.get('selling_price','')
#         rating=item.get('average_rating','')
#         review=item.get('total_rewiews_count','')
#         size_list=item.get('variants',[])
#         for value in size_list:
#             size=value.get('size','')
#         product_description=item.get('short_description','')
#         fit_guide=item.get('fit','')
#         washcare=item.get('washcare','')
#         material=item.get('material','')
#         image_url=item.get('images',[])

#         print(product_name)