import requests
from parsel import Selector

access_token = None
refresh_token = "qjk9XFOplWxFuR_JgZCgVBc7lVkXHOF5pSp-vruH-FI"
client_id = "2f55a356-1392-4de0-9cdf-f74f0666f43d"


def refresh_access_token():
    global access_token, refresh_token

    headers = {
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.bipa.at",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    }

    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
    }

    response = requests.post(
        "https://www.bipa.at/mobify/proxy/api/shopper/auth/v1/organizations/f_ecom_aaft_prd/oauth2/token",
        headers=headers,
        data=data,
    )

    if response.status_code == 200:
        tokens = response.json()
        access_token = tokens.get("access_token", "")
        refresh_token = tokens.get("refresh_token", refresh_token)
        print(" Access token refreshed")
    else:
        print(" Token refresh failed:", response.status_code, response.text)
        access_token = None


def api_get(url, params=None):
    global access_token

    if not access_token:
        refresh_access_token()
        if not access_token:
            return None

    headers = {
        "accept": "*/*",
        "authorization": f"Bearer {access_token}",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 401:
        refresh_access_token()
        if access_token:
            headers["authorization"] = f"Bearer {access_token}"
            response = requests.get(url, headers=headers, params=params)

    return response

product_urls = []
offset = 0

while True:
    params = {
        "siteId": "AT",
        "refine": "cgid=pflege-gesicht",
        "currency": "EUR",
        "locale": "de-AT",
        "expand": "availability,images",
        "offset": str(offset),
        "limit": "20",
    }

    response = api_get(
        "https://www.bipa.at/mobify/proxy/api/search/shopper-search/v1/organizations/f_ecom_aaft_prd/product-search",
        params=params,
    )
    if not response or response.status_code != 200:
        break

    data = response.json()
    hits_list = data.get("hits", [])
    if not hits_list:
        break

    for item in hits_list:
        product_id = item.get("productId", "")
        url = f"https://www.bipa.at/p/{product_id}"
        print(url)
        product_urls.append(url)

    offset += 20

print(f"Collected {len(product_urls)} product URLs")

# base_url="https://www.bipa.at/p/loreal-paris-setting-spray-infaillible-3-second-setting-mist/B3-436474"

# for base_url in product:
#     response=requests.get(base_url,headers=headers)
#     sel=Selector(text=response.text)
#     product_name=sel.xpath("//h1[contains(@class,'chakra-heading')]/text()").get()
#     brand=sel.xpath("//a[contains(@class,'chakra-link css-14do5ft')]/text()").get()
#     selling_price=sel.xpath("//p[@data-testid='product-view-price']/text()").get()
#     product_description=sel.xpath("//ul[@class='css-tu0njr']/li/text()").getall()
#     instructionforuse=sel.xpath("//p[contains(@class,'css-hd1mf2')]/text()").get()
#     image_url=sel.xpath("//img[@class='chakra-image css-1jxic4p']/@src").getall()
#     breadcrumb=sel.xpath("//li[contains(@class,'chakra-breadcrumb__list-item')]/a/text()").getall()
#     ingredients=sel.xpath("//h3[text()='Inhaltsstoffe']/following-sibling::div/p/text()").get()
#     labelling=sel.xpath("//span[text()='Kennzeichnung']/following-sibling::text()").get()
#     storage_instructions=sel.xpath("//span[text()='Aufbewahrungshinweis']/following-sibling::text()").get()
#     country_of_origin=sel.xpath("//span[text()='Herkunftsländer']/following-sibling::text()").get()

#     print(product_name,base_url)