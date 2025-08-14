from curl_cffi import requests
from parsel import Selector
import re
cookies = {
   
    'CookiesConsent': 'C0001%3BC0002%3BC0003%3BC0004',
    'ITXDEVICEID': '81a685da5966b7f75e5caf4b29e77b3d',
    'UAITXID': 'ee7e4b878bdb2fc67d242e515e49cc3248effd2cc1dd5d5318b1104c0bc97ce4',
    'FPID': 'FPID2.2.TVIWqysY0ITFmgkuME3T6%2BId9Z0WfxBS5avitilC1PQ%3D.1755148206',
    '_gtmeec': 'e30%3D',
  
    'bm_sz': '46B7D52A6E2DCFF8A34AF74564F3E912~YAAQTdcLF2uZN5yYAQAAPprYpxz3dkZgVj2/eoWyhMgpG+cTBZZKEHHyhkhmPM2+58TXC3c+EpraK9AB5jDLAirWLoP5+Wb4VHtyKlO2vK7XLJZ7sqyrPBU6lzZOYsNwJjwLaxxIDp035vh5j0qSxH8FJBBLvGw4JnyfFyQAlLVlv+fOUQb0TEE1n55rgf5wyk9PxPFkGfdcsNg7liv0jNLPSUCPEDFR1Gw2XCUvRnbuOfjPzjTjw8SJlUUF6J7liUXnN17zjhu4jt0ePoPiy1jOO1QM6Sg/93oCjLL0lRbxflXRf7IJeGRtTWCpf7BzQvKsi5G6Y7HRjPttIV3W0KBVI3Y3F54rU7qNiIHtojhpnfoSouj+dA/ED2S0L+aJmohaRTnhBlPA7pDta/y/fGbOP44nB3bH4GFWEVbrGp8FLkz5k119g5bthSugBDQ0nKrCBCAs5Lv/9iq6E4mgEhIkZK2RSb0hgNAXR+VhzjfQwefAnGPSZIAKJiUhcKW5BCDVegAGTbK8VTl1v+RgMB3y83XOS7HlolsijRyaEOM/Oyv6XRbjkNQcc3FpBx6BBfEFi9l7nVj58Z9uvYiabNmOcwuLRjoFlm+rirgf6TD1V2REMKK+/GEKaFl+lRn5~3488055~3487045',
    'OptanonAlertBoxClosed': '2025-08-14T09:10:48.841Z',
    'TS0122c9b6': '011e7fa59d45b7a880cffcacb89357659d8accb1221f57ae0503ee6ea629cf88ff37b98d41c274faef0114cd51d0b89805f7b34f3b',
    'lastRskxRun': '1755163329003',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Aug+14+2025+14%3A52%3A09+GMT%2B0530+(India+Standard+Time)&version=202505.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=39b813ef-0a6c-4154-9761-7957e4afb484&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=IN%3BKA&AwaitingReconsent=false',
    '_ga_HCEXQGE0MW': 'GS2.1.s1755160276$o2$g1$t1755163350$j3$l0$h0',
    '_abck': '9FF0DC407AB009278480DED2A06EECA4~0~YAAQLmbJFx32xp+YAQAAdFbjpw4FNPoVSS2HKN2DjPl8b5LZbQnfzJrt2F6FOiRmh7jDHnFQ5PUqwsDkdRXCb3NLawhW7Q+h8IBIEOu3X9R9nZr9OSgVL64vkOB6SXEsY2wX9V4Bp+9TNfR9PVSRXasS2HqIWQzIkxa/8KUBNUDqdLZ0knbA1qanpl/RhMCmBZkS3oXswmGZTnsnWQ33i8PZOv2LfYTeRaMPPVK2qgxllYhZF4kKEWlJAd/xyJDMlPrO9p0Jd4TGB7Ur8YPi53cqUZLtK6XkWIEs+6lyWz0arCE7WDWdnru0Q5OBklEX+cqnyjAwm5A1x00ym2CE6x3IZtgRaKLiJ5lznVJKfGyTwCJBMxfiooa0eyJC7CqT+NEPuDwtOZ8NPAktDVsYfDDhB9Dn6IfQzmy1kDLCyKzCTyp5bHvChy6POsA18MHDSPb8A/XWvVugz2/Xs0ns4xM5LexuVnEi1oax6jHd5LVRxg2zquU/ux59OyLIAMhheCJQ0lP7XPY6WgPcz9a3VnhFGUCAI53UEO8RcD6YA2gdXfTD/NwyTo3DatnU517AClEFrGDGw7uF8eIVSyJSrqGSkrR/pE2tMPkMvt+/ad1TNKluMzylUogPUVtAfU7iEYoTco+EaMAhA8MM+rhWB/1/fVsjObl8/EvxMb11JLuXCGXlVhbz9hNyVLAuRF8Z976YbPKYu65r4AppFODQVnauCqmXSIn6RCvawe0=~-1~-1~1755166110',
    '_ga_NOTFORGA4TRACKING': 'GS2.1.s1755160269$o2$g1$t1755163653$j60$l0$h1590916913',
    'ak_bmsc': '1B4E682703D5AB43B9E2FCA3CA33F708~000000000000000000000000000000~YAAQLmbJFxYPx5+YAQAAXPznpxx7aMBRXAn20kJXSK6gflN+PmWK6uKGTQxFMwJJw7w97fJVDcIqwuDMO5+Ln+yjo7lwJxmajhrjAcfxACWVZ/8oxQT9WfPckp80Zm3gq0Bq525uCE/JClnm1Rz7gEPsCRjjbE6hLABRyng8l/7i0HwAVi5EitbJ2kXKDTY8OFb0+fHiqaY3SnR/33NpchRghxpAuFDTszE9N6Cp3TsX3b7tpk13f3QLzrSDZPAf9wD7D8Wxcxxzh8eRaL1zSVk5BqOhzOGFbakCtXJh2WZ8Jj7RPXBzfVPypwJQdUw3bwl2Br41HwQnN8xe+qYdiCO8LHU3M8xZoBuRRkj3vCQYcPqpUCix/fLH86VSRdtAH8gCTah+IKSmfB+eEvczCsxmcuMn1fC95diIYW6uGn6eJxzM96KXZd8ohdxOD7byPB5XQuB3EdO7BEQmS9iUTe8jXpyiR6w8j6p5gBA7QAh2j2Xwhly0',
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
    category=''
    if category_match:
        category = category_match.group(1)
  
    product_description=sel.xpath("//div[@class='expandable-text__inner-content']/p/text()").get()
    color=sel.xpath("//p[contains(@class,'product-color-extended-name ')]/text()").get()



