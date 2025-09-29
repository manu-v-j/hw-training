from curl_cffi import requests
from parsel import Selector
import json
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.decathlon.de/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-viewport-width': '1300',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'viewport-width': '1300',
    # 'cookie': 'WNF_AFF=1759124015.801.34.766501|2f867d28b506d0b70151b4dc5c6bab68; AUTH_STATE=eyJhcHAiOiJXTkYifQ%3D%3D; ecom_user_id=3e5990de-d478-4939-83ac-e15269f88d54; __cf_bm=eiMDzO6tQ4tzUARUuwV6zVP6zrGcge1xQ6ooQGBAyDw-1759124015-1.0.1.1-Xubu5RQNabHVmUX0OfVA58xldYumqBvd04JTBkJ9fJk4tAXchfjlrrrN_E6lG.SxBNflfKv10Gg1TkbJJk78Rh1Ok.r6UhXzgoXbk2YViOA; _cfuvid=s2z8cPWcOsRTWSXpGxnpcD1nrafInMMkVfzPIDtQujQ-1759124015399-0.0.1.1-604800000; didomi_token=eyJ1c2VyX2lkIjoiMTk5OTNmNjYtMTVkMS02OTk4LWExYmMtMGM2YjkyZWFmOGMxIiwiY3JlYXRlZCI6IjIwMjUtMDktMjlUMDU6MzM6NDEuNTk3WiIsInVwZGF0ZWQiOiIyMDI1LTA5LTI5VDA1OjM0OjE2LjYyMVoiLCJ2ZXJzaW9uIjoyLCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbImFuYWx5dGljcy1HTWdCV0dUaCIsImxlc2Nvb2tpZS1IWDJoNlRqYiIsIm1hcmtldGluZy1NUlpWcHJlYSIsInBlcnNvbmFsaXMtdGY4cFpUVkgiLCJjb29raWVzbmUtN1ZBTmVUcEwiXX0sInZlbmRvcnMiOnsiZW5hYmxlZCI6WyJjOmFtcGxpdHVkZS1xNlpmSlRMYSIsImM6c3BlZWRraXQtZGVDNmtNUkciLCJjOnlzYW5jZS0zeHdGeDllNyIsImM6ZmFjZWJvb2thLVF5TURMR0pRIiwiYzpjb21lY29nZXItaE1BREx5RlgiLCJjOmFidGFzdHlnLVhFakNKZ0VMIiwiYzpjb25uZXhpdHktYUNUQ0IyNEwiLCJjOnJ0YmhvdXNlLTJ5RFltaFJkIiwiYzpleGNlbnRvcy1UQmZHeXdGZyIsImM6Z29vZ2xlYWRzLUFrMzJUUERBIiwiYzphd2luZ2VybWEtamZZM2RwZzQiLCJjOmJpbmctbkxpUUxBQ2kiLCJjOmViYXljb21tZS1OTlVqRlZtRiIsImM6ZmFjZWJvb2tnLTZrR2NYaHIzIiwiYzpiYXRjaHdlYi0yQTd0SHBhQiIsImM6ZHluYW1pY3lpLUVUZWF4SGNrIiwiYzpzZWFyY2hodWItN2ZKd1pSVEciLCJjOmNvbnRlbnRzcS1WeFFjTXpwSCIsImM6ZHluYXRyYWNlLUVpVjROeVpNIiwiYzpzdGF0c2lnLXFiZUMyN0I4IiwiYzpwZXJzYWRvLUpOTXJuamJZIiwiYzphbGdvbGlhLWtkMzR5Q3hBIiwiYzpjbG91ZmxhcmUtSE5SV3JZWnkiLCJjOmFtcGxpdHVkZS1YejdRUGpEOSIsImM6YW1wbGl0dWRlLXlieTc2cHBMIiwiYzptZWRhbGxpYS13bUQ4WmY5aCIsImM6ZGVjYXRobG9uLTJWeWI0eXJuIiwiYzpkYXRhZG9nLXdjclY2SEZYIiwiYzpuZW9jb20tTFFUcGIyWTMiLCJjOmNvb2tpZXNhbi1hWTdXZWtLciJdfX0=; euconsent-v2=CQYgfgAQYgfgAAHABBENB9FgAP_gAAAAAAAAAMAAAAQAAAAA.f_wAAAAAAAAA; dkt_ecom_tracking=eyJhbXBsaXR1ZGUiOnsiZGV2aWNlSWQiOiJhYjRlMzg5NC1kNDFmLTRmMDMtYTI2Yy1iNGE3MTgyN2ZjZTgiLCJzZXNzaW9uSWQiOjE3NTkxMjQwNTY5MTN9fQ==; _gcl2_au=1.1.644326545.1759124057; _gcl_au=1.1.1897171137.1759124057; __ywtfpcvuid=7999822071759124059264; __ywtfpcsuid=1687672561759124059264; _dyjsession=1xxfcoc370kfjiwpico3xvcyvryqpkur; _dyid_server=-6800434477792617893; _cs_c=0; _ga=GA1.1.ab4e3894-d41f-4f03-a26c-b4a71827fce8; _fbp=fb.1.1759124060447.504958158254602625; kampyle_userid=8e3b-4d66-f0b0-5a3b-08ba-8baa-ad1b-0201; kampyleUserSession=1759124060833; kampyleUserSessionsCount=1; kampyleUserPercentile=10.40196072929045; USER_TOKEN_FOR_ANALYTICS=e021f364-8623-4967-b672-e7cb5c971bfa; kampyleSessionPageCounter=2; _uetsid=f2ec2ce09cf511f0886e1b5f56bd1483; _uetvid=f2ec7b609cf511f09e50535841865e37; _ga_HBR0KBN9QJ=GS2.1.s1759124060$o1$g1$t1759124289$j1$l0$h0; _ga_KHS6MFWBPD=GS2.1.s1759124060$o1$g1$t1759124289$j1$l0$h0; _cs_id=b7ba99d6-6740-af85-c659-1615c79e99d2.1759124060.1.1759124291.1759124060.1735129019.1793288060545.1.x; _cs_s=8.5.U.9.1759126146575; _dd_s=aid=71da8712-76a1-4eb1-9703-dec5799e3bfa&rum=0&expire=1759125267695',
}
##########################CRAWLER#############################
product=[]
start=0
while len(product)<=500:
    params = {
        'from': str(start),
        'size': '40',
    }

    response = requests.get('https://www.decathlon.de/herren/sportbekleidung', params=params, headers=headers,impersonate='chrome')
    sel=Selector(text=response.text)
    product_urls=sel.xpath("//div[contains(@class,'product-card-details__item')]/h2/a/@href").getall()
    for url in product_urls:
        full_url=f"https://www.decathlon.de{url}"
        product.append(full_url)
        print(full_url)

    start+=40
print(len(product))

##########################PARSR#############################
base_url="https://www.decathlon.de/p/mp/jako/jako-damen-longsleeve-run-2-0/_/R-p-d925fbbb-95ce-4b7b-a450-59259d295ed9?mc=d925fbbb-95ce-4b7b-a450-59259d295ed9_c5c218c236&c=BLAU_k%C3%B6nigsblau_atlantikblau"
response=requests.get(base_url,headers=headers,impersonate='chrome')
sel=Selector(text=response.text)
unique_id=sel.xpath("//div[@class='product-info__product-id']/span/text()").getall()
product_name=sel.xpath("//h1[@class='vp-title-m']/text()").get()
brand=sel.xpath("//span[@class='vp-title-s']/text()").get()
product_description=sel.xpath("//div[@class='product-info__description']/span/text()").get()
selling_price=sel.xpath("//span[contains(@class,'price-base__current-price')]/text()").get()
regular_price=sel.xpath("//span[contains(@class,'price-base__previous-price')]/text()").get()
breadcrumb=sel.xpath("//a[@class='breadcrumb-item']/span/text()").getall()
script=sel.xpath("//script[@type='application/ld+json']/text()").get()
data=json.loads(script)
image_url=data.get('image','')
warranty=sel.xpath("//span[contains(text(),'Garantie')]/text()").get()
care_instructions=sel.xpath("//h3[contains(@class,'care-instructions__title ')]/following-sibling::div//text()").getall()
material_composition=sel.xpath("//p[@class='specifications__item vp-body-s']/text()").get()
promotion_description=sel.xpath("//span[@class='price-base__commercial-message']/text()").get()
print(promotion_description)