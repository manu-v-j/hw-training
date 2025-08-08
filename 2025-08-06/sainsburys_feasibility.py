from curl_cffi import requests
import random
import json
from settings import MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_DETAILS
from pymongo import MongoClient
client=MongoClient(MONGO_URL)
db=client[MONGO_DB]
collection=db[COLLECTION]
collection_details=db[COLLECTION_DETAILS]

# proxies = {
#     "http": "http://8.211.195.139:6379",
#     "https": "http://8.211.195.139:6379"
# }

cookies = {
    'akaas_gol_random': '83',
    'ak_bmsc': '40FDC69ACAD0F1B84B2B5665C5AF1BAA~000000000000000000000000000000~YAAQtULHF2qHCn+YAQAArIf5hxwf9odi/i7N7ZAOnMFlNRgCh4S2gWEQPz/Nq3nahM7vqhiNgjtoHMuMomPUSdk/J7twtzzNid7wTsdtp1KB4UHVVLVCJvG12EoY0fzMhnoZH+WDHwCDfy4gjB1gmdMHPlpjUxx6ZZT+9GloWCRq1m7JpnGfxD+UvCo6z+hGVKl/juhFA8Y7VIuJ7Z/TWARD9k3Nz9xVH0j+SzAjLdQFHsW4fYMz2QOLDN8ySoxemXvDCBAHLKXLcTZFoWiQuJL88x33SGG5d/IOBQKvYvjhUM665Qxt/kcwlsppTf+6Mh5RhNdRymAyajdyGasJ8GcwNnwJvLZW1g0584ln6G4SC92rol5cDe14NFo9zSB0yl665QBehKP/2l3OIp5GtOBfhkpbUTSCZsXQ7zCOo2LFHcOzYZ1fCx0=',
    'last_button_track': 'false',
    'AWSALB': 'mmv9XcsQBI4Lax3P0UchE4prRF6wi+e0TADktDu3wawwnxWYeGBP4cyon9+MEI5HK479ljEssYFqkMllhFHVQ+TrsJeLJauYpibWhkGnevai4LcIMBO+gh92Q8wB',
    'JSESSIONID': '00001XcysqT5b1jXIUUEgEmK8Bb:1iodtp52s',
    'AWSALBCORS': 'mmv9XcsQBI4Lax3P0UchE4prRF6wi+e0TADktDu3wawwnxWYeGBP4cyon9+MEI5HK479ljEssYFqkMllhFHVQ+TrsJeLJauYpibWhkGnevai4LcIMBO+gh92Q8wB',
    'Apache': '10.8.240.11.1754627939914929',
    'search_redirect_flag': '0',
    'OptanonAlertBoxClosed': '2025-08-08T04:39:01.196Z',
    'bm_sz': '0BF366C8BFACE17BADA9BCF15775A147~YAAQtULHF/mOCn+YAQAAC8T5hxzOtgoDIgxDNLwzsXowTCoMR4vgbPu+2KWRppnNssv6wJxTXhlfNyNREnc6Sg1K1jeZQrzPcgG8uyHlFKAGxnuiaJleo3AAvuZmN+sbn0obgPQDRhCPtQo5gy73pN/eTYGOMKCgUYJz/x2qvmPv3DlIUu/cazeS78U7EpJ3q7WizoXHkD0r7+4k+Sx2RLjR5quG/Z18HwpgiSF3C/+b0Qkcq3mIGbVqK44siAb5cLMu7mWRpNWOXwwEeyfhGyohKdEZ2p28TvCSDa6HjL7YD+//jlH3k/AJCNmqR6M9mOP3Sex6K+aSbaI2tR8/qO0BYz9xENLH8P8d2oFEgnJsLt9dNt3w57azdjy9A3xw3iyy4Uo7OU/QIxVCh2gR2JGTYjPiWMWHFBlZBU7uzj1MnjPmlQ0W81x3nWKXb61dte9Ebdn9wng=~3749172~3551793',
    '_abck': 'B879324683358F9747471803B0C4C94B~0~YAAQtULHFxiPCn+YAQAAmsT5hw43P68vuptrqkRbWilQ4SwvXtOckgqFU2cZlvVufqxKWKcEXmZSvyQdk8TMg6S6kshE8If5HzJ0QsIQIT7SEFiC27iJ46BS+2H3Jr10pkAEEzpoJjLjHURlK+aAhWtUXn3yY28+L0XliXdbxBIEIRE9d0GjGdC0jasXSwe72+tAH+Ju5dTQffKc0KtDVt1xtgcKz5hbiTr2HIDS9U6kB+hg/nbkFsGJi/44no5s9k/g6kb0+4jYy4w8RlnjZrUjHSuAPghWt31lb370k4Ud2UZyc8PIaAF6E6WGsT3xI49XN2J2dAuEF3sCDxZcoFbzrzKex+Gs8tG2mYguqGS/nfSh77KZqXyLCKZ9giy3Pu6a0OP/mQntJegWWP/bbO4zdJ6mC9wq5bTM2bNSiCROqOrt1EytWobx/NIfejlp88qO0evwJSd7FTvHVMUDStu9WxJGgS0ZROx4X69gDTFGdJjXN7TAQvu3eglYSw9Do/YNT1xVKSp0PccjUaOExZutEYs1j+DGch1aB5MITU5ftMPMOb39jTRDAn++XYnC9UtzM8P0Qf+Dm5WzGQ+QBNzTkX4+n///RWFgIlYbgDeRCed4sxGyy0Llwqi+44fkKG8=~-1~-1~-1',
    'RT': '"z=1&dm=www.sainsburys.co.uk&si=0bdbea7a-844c-428f-a6d7-1ed1f7b83fa8&ss=me2c61yb&sl=1&tt=795&bcn=%2F%2F684d0d4c.akstat.io%2F"',
    'utag_main': 'v_id:019887f98e9d001dcef93cba82b705065005f05d00bd0$_sn:1$_ss:0$_st:1754629749998$ses_id:1754627935905%3Bexp-session$_pn:2%3Bexp-session$previousPageName:web%3Agroceries%3Abrowse%3Afruit%20and%20vegetables%3Aflowers%20and%20plants%3Bexp-session$previousPageType:shelf%3Bexp-session$previousSiteSection:browse%3Bexp-session$previousPagePath:%2Fgol-ui%2Fgroceries%2Ffruit-and-vegetables%2Fflowers-and-plants%2Fc%3A1020005%3Bexp-session',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Aug+08+2025+10%3A09%3A10+GMT%2B0530+(India+Standard+Time)&version=202501.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=643466be-2f02-4db3-9860-509718733e6a&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=1%3A1%2C2%3A0%2C3%3A0%2C4%3A0&intType=2&geolocation=IN%3BKL&AwaitingReconsent=false',
    'akavpau_vpc_gol_default': '1754628251~id=ddc6a26ee6c36ed0f5803c62d755ebb3',
    'akaas_gol_global': '1762403951~rv=11~id=8a9dcc3dae62a97605ec2f163e80b042',
    'bm_sv': 'BDD449DCF4C531A67E73DBAA8FF6AE7F~YAAQtULHF/CPCn+YAQAAasr5hxyksxwLQ0wxxh92JZ9EJqh1HthuzhrHNej+Imxg9fVkDEr4yAxumSIq4kTDAAs9lK2Mqi5ije7zBjKkFfi6oKwdYSr+iBoc1bWzJ0epY62w+urirkyK3GLMQGiWs2mSnZDBgaww07uINs0V4Gjve+Yo5n5acUvCHQrW8bUtnwRS31KUQWjlJxdZ/uVI7RMxfV4bduqarH08MZ9FIzT0LcRc8wTgEuQVRe5jLwWeXQK7wIDu~1',
}

USER_AGENTS = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
]
impersonate_list = [
    'chrome',              
    'chrome99',
    'chrome100',
    'chrome101',
    'chrome104',
    'chrome106',
    'chrome107',
    'chrome109',
    'chrome110',
    'chrome99_android',
]
impersonate=random.choice(impersonate_list)
print(impersonate)
user_agent = random.choice(USER_AGENTS)

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.sainsburys.co.uk',
    'priority': 'u=1, i',
    'referer': 'https://www.sainsburys.co.uk/gol-ui/groceries',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-ba911c9ae54ed6c07446b562209ba550-431b2dddfeb165c0-01',
    'tracestate': '2092320@nr=0-1-1782819-181742266-431b2dddfeb165c0----1754566174966',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'wcauthtoken': '',
}
print(user_agent)
session = requests.Session()
# session.http_version = 2
response = session.get(
    'https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?filter[keyword]=&filter[category]=188701&browse=true&hfss_restricted=false&categoryId=188701&page_number=1&sort_order=FAVOURITES_FIRST&favouritesPriority=true&include[PRODUCT_AD]=citrus&citrus_placement=category-only&salesWindow=1',
    cookies=cookies,
    headers=headers,impersonate=impersonate
)
print(response.status_code)

# data=response.json()
# product_list=data.get('products',[])
# for product in product_list:
#     full_url=product.get('full_url',{})
#     # collection.insert_one({'link':full_url})
#     print(full_url)

# ###############################PARSER##################################
# for item in db[COLLECTION].find().limit(10):
#     url=item.get('link')
#     parts = url.split('/')
#     name=parts[-1]
    
#     url = f"https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?filter[product_seo_url]=gb%2Fgroceries%2F{name}&include[ASSOCIATIONS]=true&include[PRODUCT_AD]=citrus"


#     response = session.get(url,headers=headers,cookies=cookies,impersonate='chrome')
#     data=response.json()
#     product_details=data.get('products',[])
#     for item in product_details:
#         product_name=item.get('name','')
#         selling_price=item.get('unit_price',{}).get('price','')
#         product_description=item.get('description',[])
#         review=item.get('reviews',{}).get('total','')
#         rating=item.get('reviews',{}).get('average_rating','')
#         image_url=item.get('assets',{}).get('plp_image','')
#         currency='GBP'
#         breadcrumb_list=item.get('breadcrumbs',[])
#         for data in breadcrumb_list:
#             breadcrumb=data.get('label','')
#         print(name)

