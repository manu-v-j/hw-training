from curl_cffi import requests
from parsel import Selector
import json
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.rewe.de/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'MRefererUrl=direct; _rdfa=s:3540f1a4-ea99-4dc7-b815-788e7c0bd7c4.MM9o8ij25R13DNeTA3Py1ClX75Ey7vKGzehc/Bp9YCA; intentionLayerIsForced=true; websitebot-launch=human-mousemove; consentSettings={%22Usercentrics-Consent-Management-Platform%22:1%2C%22Adobe-Launch%22:1%2C%22AWIN%22:1%2C%22Cloudflare%22:1%2C%22Keycloak%22:1%2C%22gstatic-com%22:1%2C%22JSDelivr%22:1%2C%22jQuery%22:1%2C%22Google-Ad-Manager-Basis%22:1%2C%22Funktionale-Cookies-und-Speicher%22:1%2C%22GfK-SENSIC%22:1%2C%22Realperson-Chat-Suite%22:1%2C%22Cloudflare-Turnstile%22:1%2C%22ChannelPilot%22:1%2C%22artegic-ELAINE-Software%22:1%2C%22Outbrain%22:1%2C%22RDFA-Technologie-Statistik-%22:1%2C%22Adobe-Analytics%22:1%2C%22Mouseflow%22:1%2C%22Facebook-Pixel%22:1%2C%22Microsoft-Advertising-Remarketing%22:1%2C%22Google-Maps%22:1%2C%22YouTube-Video%22:1%2C%22Google-Ads-Conversion-Tracking%22:1%2C%22Google-Ads-Remarketing%22:1%2C%22Snapchat-Advertising%22:1%2C%22Pinterest-Tags%22:1%2C%22trbo%22:1%2C%22TikTok-Advertising%22:1%2C%22LinkedIn-Ads%22:1%2C%22Taboola%22:1%2C%22Vimeo%22:1%2C%22Cmmercl-ly%22:1%2C%22Google-Ad-Manager%22:1%2C%22RDFA-Technologie-Marketing-%22:1%2C%22The-Trade-Desk%22:1%2C%22tms%22:1%2C%22necessaryCookies%22:1%2C%22cmpPlatform%22:1%2C%22marketingBilling%22:1%2C%22fraudProtection%22:1%2C%22basicAnalytics%22:1%2C%22marketingOnsite%22:1%2C%22extendedAnalytics%22:1%2C%22serviceMonitoring%22:1%2C%22abTesting%22:1%2C%22conversionOptimization%22:1%2C%22feederAnalytics%22:1%2C%22personalAdsOnsite%22:1%2C%22remarketingOffsite%22:1%2C%22userProfiling%22:1%2C%22sessionMonitoring%22:1%2C%22targetGroup%22:1%2C%22advertisingOnsite%22:1}; s_ecid=MCMID%7C05185131770769010744581356382857842559; s_cc=true; AMCVS_65BE20B35350E8DE0A490D45%40AdobeOrg=1; AMCV_65BE20B35350E8DE0A490D45%40AdobeOrg=179643557%7CMCMID%7C05185131770769010744581356382857842559%7CMCAID%7CNONE%7CMCOPTOUT-1754384359s%7CNONE%7CvVersion%7C5.5.0; trbo_usr=c7d65912669ad17836a42abd70aba918; trbo_session=635988218; _scid=ibCAGzdKJSVYW75MuxQU2MjFTJu9j3ua; _gcl_au=1.1.1033523176.1754377160; mf_2d859e38-92a3-4080-8117-c7e82466e45a=||1754377159767||0||||0|0|37.83505|0|; _pin_unauth=dWlkPU5ESmlOek0wWVRFdE16RmtaQzAwWVRVeUxUazVNMk10TldObU16aG1NREUzWkRjeg; _ScCbts=%5B%5D; _fbp=fb.1.1754377161137.837713466598381392; _sctr=1%7C1754332200000; mtc=s:eyJ0ZXN0Z3JvdXBzSGFzaCI6ImQzNTgxOThlNWVkZDE1YmNmOGRhYjNiMGJmYmFjM2IwZjY5MmJkYmQzMDRhZDQ1MmNhZDQ3YmYwMzliOGFlZWUiLCJoYXNoIjoiTVY4Vnk1bkhYQU0xbHgzTjFaaU5pdz09Iiwic3RhYmxlIjpbImNhdGVnb3J5LW92ZXJ2aWV3LXJlbmRlcmVyIiwiYWJ0LXBkcC1jb21iaW5lZC1kZXNjcmlwdGlvbiIsInByZWZpbGxlZC1sb3dyYXRlIiwic3BzLXN0b2NrIiwicmV3ZS1zc28iLCJwYXliYWNrLWV2b3VjaGVyIiwicGF5YmFjay1jYXJkLWNoYW5nZSIsInBheWJhY2stcmV3ZS1uZXdzbGV0dGVyIiwicGF5bWVudC1lbmFibGUtZ29vZ2xlLXBheSIsImNoZWNrb3V0LW1scy1jdXN0b21lci1hc3NpZ25tZW50IiwicGF5YmFjay10YXJnZXRlZC1idXJuIiwic2ZzLXBpY2t1cC1zdGFnZ2VyaW5nLWluZm9ib3giLCJwYXliYWNrLWVjb3Vwb24tYXBpIiwib2ZmZXItZGV0YWlscy10cmFja2luZyIsInBheWJhY2stdGFyZ2V0ZWQtYm9udXMtY291cG9uIiwiY2F0ZWdvcnktb3ZlcnZpZXctcmVuZGVyZXItcmVsb2FkIiwiaGlkZS1wYXliYWNrIiwidHJveSJdLCJyZHRnYSI6W10sIm10Y0V4cGlyZXMiOjB9.cmIFsx1J9I4lFWMl7d7Mm3XqF0AOz6OZWBpUrN565WY; rstp=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhZXMxOTIiOiIwNjIzYTJlM2EyYTNjODFkNTZlNGE5NWI5OTRlZjQ3OTdlMmFhNTk5ZTE4MTU1NmM5ZmZmMzE5ZGVmMDhkNDg3OTQ2ODE0NDQxNzg4YzJlOWU5NTQ5MmJlZjYwYTUzNWEwNDdiYjUyYmE0MTQ1NDI3ODRjZmZjMjVmZGE1NjlkMWRhZDQ2YjEyZTg1NTE0ZjNkMDBlYTk1N2IwMThkMzBhNDQ2ODQxZTY0YjA0OGVlNTgzYzJjZGZhMmIyNGExYWFkYmViNTQyODQ0M2E3MThhMjdjOWQyMTdkMjIyOTNkNWJhZGFjYzMyMGY1NDMwMThmMmMyYmE3NzZiZjEzMmY4MmRkNzA0Zjk5YmNkMjAyOGQyMmNjMjU5YzBiN2EzYzQ0MGY4Zjg4MjExMzg4ODUwZjYzZjA0Y2U3Y2Q5OWQ5YTE5ZGNjMmUzN2I3MjYyNmVmZmE5NWY0YWEzZjlhN2VjM2RiNjliOGVkMjQ3M2JjN2JlNjk4ZWE1NmI1YmY0NDBmNmEyZTNiNDY0Mzk4NjhmZjA2NGIxZDQwMWVhNjJiYjJhM2M1NDU5MzVkNWJkY2EwMjUwMzY0NTY0NjE5MWU4OGIwYjkwNmUyNTdlMGM1NDFlMWFhYmViZWU0ZWFlYjQxMWI2MDFlMmY0OTZjNmY2Y2VjOWJlMjc1NzRkNDViMCIsImV4cCI6MTc1NDM3ODQyNSwiaWF0IjoxNzU0Mzc3ODI1LCJpdiI6ImJmaEt5Tk5TaGFzS2RnUlBIQk1NUFEifQ.fpYT4A47XFBI0cP1_yoNoTewuAYFNEsHr2dfX281PSzneL7Bk2WCdhEtlQmrg2KjUb6fKlgqB2valKgEJaWEDA; adwords-ASLS-visitadd-session-launch=AW-802830374/LaQBCM-o0NEDEKbw6P4C; __cf_bm=Gn3p4H7wA5ZM1h7ghMDugzsJ8H1p.yoGFBDFmesOhY0-1754377870-1.0.1.1-L2Hb1sbBrYA8GB3xFGAyEYJ3CaTDR7DaDxc85s6d3t0jU00zT4CidYKmzG31x87fPqxG9R2xIGzyG5eVMG4vbSnGFVVHIRdHXAUoPeDLUuM; _cfuvid=4lsu9d8fk3.qxKVwmMRniRnbP0_8y8s5k9_aU6CGGsc-1754377870578-0.0.1.1-604800000; cf_clearance=2sO_I2ZbMex_LFX3l2le13RyPWR3OnddK5oq_buBNmo-1754377873-1.2.1.1-47HNf905Z_UFf_aWj7tENsQCLLAC.vBKEbPyssXt7FgsjVi5Ib2PYzFBY8FKHvJLgZkCH0P_VQPiBLDoG4ebAQZOJaIpBLnSjYuBQu_SIAXloyaHPf62p1cjajnuI2F0d3O7V.CCCAb0l1W2ONAtPAig_WooGbmQEEnCk4O_rALfmAPufrXUC8u1sKSriRJm2I1Hd5mI2H4c3pqcm8EEDP8AWZxb_1Ofk_ski9wvufE; icVarSave=tc119_t%2CSearchBoost-Ctrl; s_sq=%5B%5BB%5D%5D; c_lpv_a=1754378161571|dir_direct_nn_nn_nn_nn_nn_nn_nn; trbo_us_c7d65912669ad17836a42abd70aba918=%7B%22saleCount%22%3A0%2C%22sessionCount%22%3A1%2C%22brandSessionCount%22%3A1%2C%22pageViewCountTotal%22%3A13%2C%22sessionDurationTotal%22%3A1003%2C%22externalUserId%22%3A%22%22%2C%22userCreateTime%22%3A1754377159%7D; trbo_sess_635988218=%7B%22firstClickTime%22%3A1754377159%2C%22lastClickTime%22%3A1754378162%2C%22pageViewCount%22%3A13%2C%22sessionDuration%22%3A1003%7D; perfTimings=event188=2.18%2Cevent189; perfLoad=2.18; _scid_r=mjCAGzdKJSVYW75MuxQU2MjFTJu9j3uadgwhHw; s_ppn=startseite; _uetsid=b605e43071c911f0a38849a0c38372a5|og6rga|2|fy7|0|2043; dicbo_id=%7B%22dicbo_fetch%22%3A1754378163976%7D; __gads=ID=cd2df54c31f5d6b6:T=1754377158:RT=1754378163:S=ALNI_MZK970TLpN3l7H0KcZDgOw-OAMqpg; __gpi=UID=0000117b4853e066:T=1754377158:RT=1754378163:S=ALNI_MaaQ3zdwbauwm4wqbFwbOd-THnMvQ; __eoi=ID=992639c71899c492:T=1754377158:RT=1754378163:S=AA-AfjbQgM5ncIoCM5iI-XPzAxpO; _uetvid=b606069071c911f0a0a271d54c07aed6|1xroe1e|1754378164481|9|1|bat.bing.com/p/insights/c/e',
}

###################################################CRAWLER#########################
product=[]
page=1
while True:
    url=f'https://shop.rewe.de/c/fleisch-fisch/?page={page}'
    print(url)
    response=requests.get(url,headers=headers,impersonate='chrome')
    sel=Selector(text=response.text)
    product_urls=sel.xpath("//a[contains(@class,'productDetailsLink')]/@href").getall()
    if not product_urls:
        break
    for link in product_urls:
        full_url=f'https://shop.rewe.de{link}'
        product.append(full_url)
        # print(full_url)
    page+=1

##############################################PARSER#################################
url='https://shop.rewe.de/p/mini-babybel-original-kaese-snack-9-stueck-180g/8186850'
response=requests.get(url,headers=headers,impersonate='chrome')
if response.status_code==200:
    sel=Selector(text=response.text)
    product_name=sel.xpath("//h1[@class='pdpr-Title']/text()").get()
    brand=sel.xpath("//h3[contains(text(),'Marke')]/following-sibling:: text()").get()
    product_decsription=sel.xpath("//h2[contains(text(),'Produktbeschreibung')]/following-sibling:: div//text()").getall()
    ingredients=sel.xpath("//h3[contains(text(),'Zutaten')]/following-sibling:: text()").getall()
    nutritions={}
    rows=sel.xpath("//table[contains(@class,'pdpr-NutritionTable')]//tbody/tr")
    for row in rows:
        key = row.xpath("./td[1]/text()").get().strip()
        value = row.xpath("./td[2]/text()").get().strip()
        nutritions[key] = value
    country_of_origin=sel.xpath("//h3[contains(text(),'Ursprungsland')]/following-sibling::text()").get()
    breadcrumb=sel.xpath("//ul[@class='lr-breadcrumbs__list']//text()").getall()
    json_data = sel.xpath("//script[contains(@id,'pdpr-propstore')]/text()").get()
    data=json.loads(json_data)
    selling_price=data.get('productData',{}).get('pricing',{}).get('price','')
    information_list=data.get('productData',{}).get('mediaInformation',[])
    for list in information_list:
        image_url=list.get('mediaUrl','')
    promotion_description=sel.xpath("//div[@class='pdpr-Price__BulkMarketingMessage']/text()").get()
