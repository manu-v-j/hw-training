from curl_cffi import requests
from parsel import Selector
import re
cookies = {
   
    'CookiesConsent': 'C0001%3BC0002%3BC0003%3BC0004',
    'ITXDEVICEID': '81a685da5966b7f75e5caf4b29e77b3d',
    'UAITXID': 'ee7e4b878bdb2fc67d242e515e49cc3248effd2cc1dd5d5318b1104c0bc97ce4',
    'FPID': 'FPID2.2.TVIWqysY0ITFmgkuME3T6%2BId9Z0WfxBS5avitilC1PQ%3D.1755148206',
    '_gtmeec': 'e30%3D',
    'FPLC': '%2Bzp79MNCKViYdj8sU3RTN5wcmhbk5%2B%2FfTDgxOp7G0R0dRnlZT%2FGe6S9hq0xUma2yeh4zXOA1z0zkELEu25DDxx9dAIOC29fteJmcxKFrTyyFnS1EW5nIqIyLjeGpNg%3D%3D',
    '_fbp': 'fb.1.1755148212229.1139399720',
    'cart-was-updated-in-standard': 'true',
    '_UserReference': '925faa3ff1a057b4b3ed01fdb1ce2a40',
    'bm_sz': '46B7D52A6E2DCFF8A34AF74564F3E912~YAAQVbxWaNRhw6aYAQAAWyM4qBwmaC3H5H1bM5wS9CfVDMwLCg0YcSHM+Z5LvNTFiZUCIu7qBWCnYmELtw2JtaPQRLMwXMC2gxJmrpVu5PBDyKweCG3TbsmyiDUXmGW8jzdPCTF1QlHukZo84jyF9w6EVdfT3aUrsmM42z0Zdwb1QBPf69Qk2zhhMoZ6AnjFvZX2c+jm+s+aOqK1URuvFGi0jeoILfeZigVXkpFKVeHkZWARNMd0dGBjBZ7Dr2kpLirQ/DI6RzfkZBErQSpNBkzTbmFOFygc1NCGzm4eA8kgzL3KO2Wfn8pvuAaEIuz5aet1Q/2MfS5QmFZgjxiOYKQUrsaY4jtwU/Yc3Dh/nPfuolrhjjfkWw0DcFdR3LNKI4GxCOHz/XFjVZo1gCmQaIOZNUBrJvNgxdEtJb4aNVXmmCzTc/vyXdK7/wenQMJde7gOAPKu13/gUwNU6Yqe10JA1MYC9Ub4ucp4ezaNmT55j+EBKHHzCZa1a7p26OnHcUNon3YjtF/tI4YPT3y900ZZCBW8EFYdPrAxeQkN3QaktXbrxOZf+yUOyeKESCZim96ORMqF6sPCEco5ix0zVDY0D0PlfqJIJtb5dVQkTzQkHvwoCIbHSYi9Cs8=~3488055~3487045',
    'IDROSTA': 'e55c311e84d8:21534c69461706520c46d903e',
    'ITXSESSIONID': 'a75ef285bb7b15a35c8f46d3090823f6',
    'OptanonAlertBoxClosed': '2025-08-14T11:32:17.547Z',
    'TS0122c9b6': '01bad81f5b6e557dfc2028c8fbc3a34c7e7ced1ca9af0e024abb218fbdff308aa2ba152c146e50b359d85df3ffca693cafbc2c4994',
    '_abck': '9FF0DC407AB009278480DED2A06EECA4~0~YAAQVbxWaD17w6aYAQAAKipaqA5T0RdLsAeLbfU+RATYK5dj7KhkTa8GXGB5mz72tiGl+tyWnd0MO8oDX2A8zmYA4IH3umGXAmxHA68FRtuqhbzpmsnIqjqcru0PPzJ7fqC8X20zWBnLhBqYMKcNdqtuWncZhj0zMjh9/ODj/sCNV+gdpduT/E98X6nGv8pqED1R3qSr4BDjRG7PhZHrAj48/hpZT1FkPOZLugJxIkp8jimbQGOZLidbgXokycbk2fju9GjiQosir50IZFJ9pnxmBTHctxv+RU2kMPvGljEhexFlCvBWpl3mdq4bpZVW0UY/ZNDXIPvGMJRV8bmeEw1Ce9+kpgGCer3BGtepwSKLxQiCSkfcr3QLXO5ST/zHw09f23PM+g/l2uyCI3aJRfft4qIscNBFDPeFepnHmt1J57g+FPaY61ZBOkI8ENJokr4Giz43wkqY8ef7oxrLEnFoKqP/5wWZUYUdHAmVg826vRifsGF/X067Ln8wxgp627Zw7/jC0A6rRZhy4toIMgoAk2aIwgik8fJAt1ovqs+g5TpZ0G3elu62ewDqL3120NnRDeAPxh/LvM5/durHbXJl+F34bOQ1rhEBCDAAxTx1bjJVItdsOqTPI7R3KjlXTfzTcGnfpqMFoxt7u90ragJbZepOYDFa76DnqKjAhFgu3+4+SEeCL2+tXuNPVLIDDmatpgz5pMILD6qwBYDYlCICoTKLYONESCde2Yg=~-1~-1~1755173315',
    'bm_sv': '14839182B5A3D8E10751FFA77E88E9D3~YAAQVbxWaD57w6aYAQAAKypaqBxJkfSFef2K9bag2dtgfspgXZpoiTbvCFrI5/PhOsydHpLlGdC5XnqK9vmTLhJNwLIn4mi8P3xPi7rTZCzsvCU+NovkjFsFHYebqSVDIpEX3Xz5qx916pSby/jfmc2sIjVaeYt7DnzaUK43txTIvaxDF2AhfnDFIEMC2WsbJRDHS7FReEUYGXgG3j8puB+TZIIjdOgF7yaZwp9Hrq9+5CaUc1QISOypgvdGcA==~1',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Aug+14+2025+17%3A02%3A18+GMT%2B0530+(India+Standard+Time)&version=202505.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=39b813ef-0a6c-4154-9761-7957e4afb484&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=IN%3BKA&AwaitingReconsent=false',
    'lastRskxRun': '1755171138760',
    '_ga_NOTFORGA4TRACKING': 'GS2.1.s1755171135$o4$g1$t1755171218$j60$l0$h1668692215',
    '_ga_HCEXQGE0MW': 'GS2.1.s1755171135$o3$g1$t1755171218$j60$l0$h0',
    'ak_bmsc': '332F3CB033331A4B2B6C523FCC3C8507~000000000000000000000000000000~YAAQVbxWaHN8w6aYAQAARGxbqBxo+0qd9AP36iKxzcGjUt1HOdsI88HRBSH7WAa7MsL43a9Q6REMvCLlSQQRZhn94zRf7YTiI65Di0X6tzm+ZaouSO9WY/hxvYMxEM06igiKVeFtr7wqp6PpchDB18Vr/L8wRh71SLS8UkVKDafxk3EyBlFKyYAoh16d/rRainNzyw0qWAv/OiT4+M1YHPYMtzdO1/5gm/15YdU4tkAKBQHhC7Rp7KSo0J9xU5XkFlQ67m7qLQ1sUr3j15PegnqxSvJoLwOwzmbGUmNjs/Qe4FKDv+rNUlRjy7JNWIOG+2tW7U/QbD2H3IPH5iVwxS9GMjo+0Np4rfZkyMorgxRpoxnCNi4ozauV0JvbMAZFj6fxCm6rN1ntZ9/d0K8pG2iz3GMEbX+NhTXZLbDJfv7sjoOUZXH5uQcpofiLrS288r0Nc+8NTZvVt5NMXp0kdYwu5/n0J998mhm79M5bCvu+BNIACRFF',
}
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
respose=requests.get('https://www.zara.com/ae/',headers=headers,cookies=cookies,impersonate='chrome')
sel=Selector(text=respose.text)
category_urls=sel.xpath("//li[contains(@class,'layout-categories-category') and contains(@data-layout,'products-category-view')]/a/@href").getall()
print(category_urls)

#########################CRAWLER###############################################
product_link=[]
page=1
while True:
    base_url=f"https://www.zara.com/ae/en/man-shirts-l737.html?page={page}"
    response = requests.get(base_url, cookies=cookies, headers=headers,impersonate='chrome')
    sel=Selector(text=response.text)
    product_urls=sel.xpath("//a[contains(@class,'product-grid-product__link link')]/@href").getall()
    print(len(product_urls))
    if not product_urls:
        break
    print(base_url)
    for url in product_urls:
        product_link.append(url)

    page+=1


########################PARSER###############
url="https://www.zara.com/ae/en/faded-sweatshirt-p03253345.html"
response=requests.get(url,headers=headers,cookies=cookies,impersonate='chrome')
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



