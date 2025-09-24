import requests
from parsel import Selector
import json
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.coursesu.com/drive/home',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'sid=7h_tz5fybCK1FZcgymHAYpWaqpU_T4HF4J0; newsletterDisplayNb=0; dwanonymous_8ce4ace52d14ef4ce78780bbb2b979c7=bcqwtP5Q5jWwy2XLBfMvaMpg5c; dwsid=TFDysyucVTDgwZHSs4_3zjfVtemDIbjXtUlOycZcurTNmEx9CGw29ql7GXFznO0vPZtrakrS-avWcJosXwY5Ig==; __cf_bm=NIttuWDhNNwLmty6tqhKRjC0fQyQhY_NbyrGThVa0mk-1758694603-1.0.1.1-QpAviJqYOyo7ffxcakRFe8vCpFIGrkRx8Ne4bmuygOxH_KuVKSnwMh1QYujtXwD7p8WN0qE9jMzcpGhIfXSEIlXHnOVWq5RKgDClqPWjs.w; KPVAL_DFS=20px; KPVAL_DWW=700px; cpc_bing=true; TCPID=125931146511243870501; cf_clearance=vEJqSOXnFt3D0zxFEqhXBIhbYkwhx5Jyb_4AeVQv374-1758694611-1.2.1.1-uYqMyraBvKXeUshyYpoKP3mPe3nW6w5hHjnzFIKm.oTeB5n7o8SBWkbklxXvcZMcnpC1Udy867ePKvspQsGQUvxSriWcS4ajl2QbrHRc7jeuOymz9ts7bk4qGGoIYQyB0EdlnGW1U4AbiKmb8MZVxCTwZe.a9xqidAzr6LGNYBgPIy7c2OOXQCc8lql_05GUxkpokhDJJPsrMMX_mtvELCt.UxvnSwIGZf0lz.k.4jo; TC_PRIVACY=0%40001%7C36%7C3692%401%2C2%2C3%2C4%40%401758694613674%2C1758694613674%2C1774246613674%40; TC_PRIVACY_CENTER=1%2C2%2C3%2C4; AMCVS_9300575E557F044A7F000101%40AdobeOrg=1; s_cc=true; AMCV_9300575E557F044A7F000101%40AdobeOrg=1585540135%7CMCIDTS%7C20356%7CMCMID%7C44833661304382982640444335744244609906%7CMCAAMLH-1759299414%7C6%7CMCAAMB-1759299414%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1758701816s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; _scid=uXgJ39L87OhRU_GLj327_oaNxVBZiGJS; tfpsi=c26485dc-c33e-46f2-8d5d-65a6fba80734; _ScCbts=%5B%22152%3Bchrome.2%3A2%3A5%22%2C%22172%3Bchrome.2%3A2%3A5%22%5D; _lm_id=1XW7IPNZMBMKGS5X; _gcl_au=1.1.1710473607.1758694622; _fbp=fb.1.1758694622408.656912986797985456; _tt_enable_cookie=1; _ttp=01K5X5WHQA7E5DZJRZX9JW93MQ_.tt.1; _cs_c=1; _pin_unauth=dWlkPU5ESmlOek0wWVRFdE16RmtaQzAwWVRVeUxUazVNMk10TldObU16aG1NREUzWkRjeg; __cq_dnt=0; dw_dnt=0; dwac_8d8721aecf7af8fe498c1f352b=7h_tz5fybCK1FZcgymHAYpWaqpU_T4HF4J0%3D|dw-only|||EUR|false|Europe%2FParis|true; cqcid=bcqwtP5Q5jWwy2XLBfMvaMpg5c; cquid=||; tCdebugLib=1; __cq_uuid=bcqwtP5Q5jWwy2XLBfMvaMpg5c; _cs_cvars=%7B%7D; currentUserUrlForAccount=https%3A%2F%2Fwww.coursesu.com%2Fc%2Fpains-viennoiseries-et-patisseries; s_sq=%5B%5BB%5D%5D; __cq_bc=%7B%22bbqx-DigitalU%22%3A%5B%7B%22id%22%3A%227629181%22%7D%2C%7B%22id%22%3A%221943611%22%7D%5D%7D; cto_bundle=Ky84zV96T2FwUEI4THJodzZjenFNWGxic29VQTVvcllDbTRCNzBHUTA2TENFczZFUVVWN09uWW5mdzdXbngwSThXU1hKQkFYTCUyRm9xQ294dU1QOXBTWTglMkZ1dTBqUUkzUlZqTDNmbVAyYUxtdERobGFha3glMkJ3eHZMaUgyR3pLb0NxcEJPUHhrQmk3RldRbDh5TWxKWjJQV3NNUTBjRFV0c3d2SHlRNEk1bTBLUGVGWlUxJTJCNjZaSVlBWkRvYzY4RXVNSGVOJTJGR2ZrOGVNZ3pWY3JVVGphM2toRXRGdEpweklqQlp0YXElMkZSWWhWU3BzS2d4NjJmZWpKcEk3UGsyWFVXUEZZWWdEMUlVRFclMkJjY0NpbkgzTFhieGR2YnM3aUNhWkM4QTYwRWdjUzNIWiUyRmlvTkclMkZuM0NRUE91UDJQaW5iSW9pRXRUbg; __cq_seg=0~0.15!1~-0.66!2~0.18!3~-0.21!4~-0.03!5~-0.11!6~0.07!7~0.03!8~-0.33!9~0.58; _scid_r=yfgJ39L87OhRU_GLj327_oaNxVBZiGJSSmXINA; _tq_id.TV-5445189054-1.22e4=9663a508b49b761b.1758694621.0.1758694997..; ttcsid=1758694622977::RFf7DDBjin-U2h_8D3yU.1.1758694998601.0; _cs_id=df4fe4b0-6740-a806-b3b9-da7e45b6cceb.1758694623.1.1758694999.1758694623.1739955371.1792858623158.1.x; _uetsid=156bb110990e11f09a46230e8500d7da; _uetvid=156c1b30990e11f09428b390cf464e2b; ttcsid_CG0ANABC77U7TJLU08C0=1758694622975::Zr7EcE-j4dmezXQYoAwt.1.1758695002703.0; datadome=henVX80mJIm01fM46ak901_jycQ4K~QvD_JJdAi4S9BTkG1spzvxPEOpvea1QGpqCoaZpciuzg~C3LMHKJTcKfYM2cXiEcV~u6GY2p0MjhQg5CpMcy2gRaH9aaS6ZxuH; _cs_s=8.5.U.9.1758696841878; _dd_s=logs=1&id=6929ecfa-7dac-4fdc-afce-4eeb40d5a63d&created=1758694613616&expire=1758695923155',
}

#######################CRAWLER###################
product=[]
page=1
while True:
    base_url=f"https://www.coursesu.com/c/high-tech?page={page}"
    response = requests.get(base_url, headers=headers)
    sel=Selector(text=response.text)
    product_urls=sel.xpath("//a[@class='product-tile-link']/@href").getall()
    if not product_urls:
        break
    print(base_url)
    for url in product_urls:
        full_url=f"https://www.coursesu.com{url}"
        product.append(full_url)
    
    page+=1

print(len(product))

###############################PARSER######################
for base_url in product:
    # base_url="https://www.coursesu.com/p/gache-pur-beurre-tranches-epaisses-terroir-de-loire-maline-thomas-500g/7629181.html"
    response=requests.get(base_url,headers=headers)
    sel=Selector(text=response.text)
    script=sel.xpath("//script[@type='application/ld+json']/text()").get()

    if script:
        data = json.loads(script)
        product_name=data.get('name','')
        # backend
        mpn=data.get('mpn','')
        sku=data.get('sku','')
        brand=data.get('brand',{}).get('name','')
        image_url=data.get('image',[])
    else:
        print(" No JSON script found on page")
   

    rating=sel.xpath("//span[contains(@class,'bv-rating-stars-container')]/@aria-label").get()
    review=sel.xpath("//span[contains(@class,'review-link')]/text()").get()
    netweight=sel.xpath("//p[@class='pdp-description-text' and contains(text(), 'Poids net')]/text()").get()
    legal_name=sel.xpath("//p[@class='pdp-description-text' and contains(text(), 'Dénomination légale')]/text()").get()
    ingredients=sel.xpath("//h3[text()='Ingrédients']/parent::li/following-sibling::li//p[2]/text()").get()
    storage_instructions=sel.xpath("//h3[text()='Instruction de conservation']/parent::li/following-sibling::li/p/text()").get()
    breadcrumb=sel.xpath("//ol[contains(@class,'breadcrumb')]/li//a//text()").getall()

    print(product_name)