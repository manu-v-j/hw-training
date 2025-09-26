import requests
from parsel import Selector
import unicodedata


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJ2ZXIiOiIxLjAiLCJqa3UiOiJzbGFzL3Byb2QvYWFmdF9wcmQiLCJraWQiOiI0ZWNjMTZjZC1mZDkwLTQxNjQtYjdmNC0yMTZhMzJhMjEzYjIiLCJ0eXAiOiJqd3QiLCJjbHYiOiJKMi4zLjQiLCJhbGciOiJFUzI1NiJ9.eyJhdXQiOiJHVUlEIiwic2NwIjoic2ZjYy5zaG9wcGVyLW15YWNjb3VudC5iYXNrZXRzIHNmY2MuY2F0YWxvZ3Mgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5wYXltZW50aW5zdHJ1bWVudHMgc2ZjYy5zaG9wcGVyLWN1c3RvbWVycy5sb2dpbiBzZmNjLm9yZGVycyBzZmNjLnByb21vdGlvbnMucncgc2ZjYy5wcm9kdWN0cyBzZmNjLmludmVudG9yeS5pbXBleC1ncmFwaHMgc2ZjY19pbnZlbnRvcnlfcmVzZXJ2YXRpb25zIHNmY2Muc2Vzc2lvbl9icmlkZ2Ugc2ZjYy5pbnZlbnRvcnkucmVzZXJ2YXRpb25zLnJ3IHNmY2Muc2hvcHBlci1teWFjY291bnQucGF5bWVudGluc3RydW1lbnRzLnJ3IHNmY2NfaW52ZW50b3J5X2F2YWlsYWJpbGl0eSBzZmNjLnNob3BwZXItbXlhY2NvdW50LnByb2R1Y3RsaXN0cyBzZmNjLnNob3BwZXItY2F0ZWdvcmllcyBzZmNjLnNob3BwZXItbXlhY2NvdW50IHNmY2MuZ2lmdC1jZXJ0aWZpY2F0ZXMgc2ZjYy5zaG9wcGVyLXByb2R1Y3RzIHNmY2MucHJvbW90aW9ucyBzZmNjLmludmVudG9yeS5hdmFpbGFiaWxpdHkucncgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5ydyBzZmNjX2ludmVudG9yeV9pbXBleF9pbnZlbnRvcnlfcncgc2ZjYy5pbnZlbnRvcnkuYXZhaWxhYmlsaXR5IHNmY2Muc2hvcHBlci1iYXNrZXRzLW9yZGVycyBzZmNjLnNob3BwZXItY3VzdG9tZXJzLnJlZ2lzdGVyIHNmY2Muc2hvcHBlci1teWFjY291bnQucHJvZHVjdGxpc3RzLnJ3IHNmY2Muc2hvcHBlci1iYXNrZXRzLW9yZGVycy5ydyBzZmNjLmludmVudG9yeS5yZXNlcnZhdGlvbnMgc2ZjY19pbnZlbnRvcnlfYXZhaWxhYmlsaXR5X3J3IHNmY2NfaW52ZW50b3J5X3Jlc2VydmF0aW9uc19ydyBzZmNjLnNob3BwZXItZGlzY292ZXJ5LXNlYXJjaCBzZmNjLnNob3BwZXItZXhwZXJpZW5jZSBzZmNjLnNob3BwZXItbXlhY2NvdW50Lm9yZGVycyBzZmNjX2ludmVudG9yeV9pbXBleF9ncmFwaHMgc2ZjYy5zaG9wcGVyLXByb2R1Y3RsaXN0cyBzZmNjLnNob3BwZXItcHJvbW90aW9ucyBzZmNjLm9yZGVycy5ydyBzZmNjLmNkbi16b25lcy5ydyBzZmNjLmNkbi16b25lcyBzZmNjLnNob3BwZXItbXlhY2NvdW50LmFkZHJlc3NlcyBzZmNjLnRhX2V4dF9vbl9iZWhhbGZfb2Ygc2ZjYy5pbnZlbnRvcnkuaW1wZXgtaW52ZW50b3J5LnJ3IHNmY2MuaW52ZW50b3J5LmltcGV4LWludmVudG9yeSBzZmNjLmN1c3RvbWVybGlzdHMucncgc2ZjYy5zaG9wcGVyLXN0b3JlcyBzZmNjLnNvdXJjZS1jb2Rlcy5ydyBzZmNjLnByb2R1Y3RzLnJ3IHNmY2MucHdkbGVzc19sb2dpbiBzZmNjLnNob3BwZXItY29udGV4dC5ydyBzZmNjX2ludmVudG9yeV9pbXBleF9pbnZlbnRvcnkgc2ZjYy5jYXRhbG9ncy5ydyBzZmNjLnNob3BwZXItbXlhY2NvdW50LmFkZHJlc3Nlcy5ydyBzZmNjLnNob3BwZXItZ2lmdC1jZXJ0aWZpY2F0ZXMgc2ZjYy5zaG9wcGVyLXByb2R1Y3Qtc2VhcmNoIHNmY2MudHNfZXh0X29uX2JlaGFsZl9vZiBzZmNjLnNvdXJjZS1jb2RlcyBzZmNjLmN1c3RvbWVybGlzdHMgc2ZjYy5naWZ0LWNlcnRpZmljYXRlcy5ydyIsInN1YiI6ImNjLXNsYXM6OmFhZnRfcHJkOjpzY2lkOjJmNTVhMzU2LTEzOTItNGRlMC05Y2RmLWY3NGYwNjY2ZjQzZDo6dXNpZDphN2EwNjQyOC02NDJjLTQ3NmItYmYwOS0xNWRkOGRkZjJhMjEiLCJjdHgiOiJzbGFzIiwiaXNzIjoic2xhcy9wcm9kL2FhZnRfcHJkIiwiaXN0IjoxLCJkbnQiOiJudWxsIiwiYXVkIjoiY29tbWVyY2VjbG91ZC9wcm9kL2FhZnRfcHJkIiwibmJmIjoxNzU4ODcxMDk5LCJzdHkiOiJVc2VyIiwiaXNiIjoidWlkbzpzbGFzOjp1cG46R3Vlc3Q6OnVpZG46R3Vlc3QgVXNlcjo6Z2NpZDphYndyQkZrYndZa0hFUmxIb1d3V1lZbFh4Rzo6Y2hpZDpBVCIsImV4cCI6MTc1ODg3MjkyOSwiaWF0IjoxNzU4ODcxMTI5LCJqdGkiOiJDMkMtMTE3ODI3NzY5MTA3NDAzOTA1MTYxMTgwNTA1NjUxNjkwMTc5In0.l-XF3rzBoBZ8o98NSBemRui68d8GsucaIuHMlHzFZ7NJc9efnxJiF-9MFqISJ_R0MmLYbkS4ttsItBmwGWxoPQ',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
}

product=[]
offset=20
while len(product)<10:
    params = {
        'siteId': 'AT',
        'refine': 'cgid=pflege-gesicht',
        'currency': 'EUR',
        'locale': 'de-AT',
        'expand': 'availability,images',
        'offset': str(offset),
        'limit': '20',
    }

    response = requests.get(
        'https://www.bipa.at/mobify/proxy/api/search/shopper-search/v1/organizations/f_ecom_aaft_prd/product-search',
        params=params,
        headers=headers,
    )
    
    data = response.json()
    hits_list = data.get('hits', [])
    if not hits_list:
        break

    for item in hits_list:
        product_id = item.get('productId', '')
        url = f"https://www.bipa.at/p/{product_id}"
        print(url)
        product.append(url)

    offset+=20

print(len(product))

# base_url="https://www.bipa.at/p/loreal-paris-setting-spray-infaillible-3-second-setting-mist/B3-436474"

for base_url in product:
    response=requests.get(base_url,headers=headers)
    sel=Selector(text=response.text)
    product_name=sel.xpath("//h1[contains(@class,'chakra-heading')]/text()").get()
    brand=sel.xpath("//a[contains(@class,'chakra-link css-14do5ft')]/text()").get()
    selling_price=sel.xpath("//p[@data-testid='product-view-price']/text()").get()
    product_description=sel.xpath("//ul[@class='css-tu0njr']/li/text()").getall()
    instructionforuse=sel.xpath("//p[contains(@class,'css-hd1mf2')]/text()").get()
    image_url=sel.xpath("//img[@class='chakra-image css-1jxic4p']/@src").getall()
    breadcrumb=sel.xpath("//li[contains(@class,'chakra-breadcrumb__list-item')]/a/text()").getall()
    ingredients=sel.xpath("//h3[text()='Inhaltsstoffe']/following-sibling::div/p/text()").get()
    labelling=sel.xpath("//span[text()='Kennzeichnung']/following-sibling::text()").get()
    storage_instructions=sel.xpath("//span[text()='Aufbewahrungshinweis']/following-sibling::text()").get()
    country_of_origin=sel.xpath("//span[text()='Herkunftsländer']/following-sibling::text()").get()

    print(product_name,base_url)