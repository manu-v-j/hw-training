from curl_cffi import requests
import json
from parsel import Selector
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.northernsafety.com',
    'Referer': 'https://www.northernsafety.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'x-algolia-api-key': 'NGFlNjBlNzU0OTUxZmY2Nzc3YThiZTFmODQxNzMwYzZmNWQ3MjFiNjQ2NTM0NDE0YmU3ZjQ1Y2RjZDMwZDkxM2ZpbHRlcnM9SXNQcml2YXRlJTNBZmFsc2UmdmFsaWRVbnRpbD0xNzU2OTY2MjQ2',
    'x-algolia-application-id': 'I45I79OC23',
}


# response = requests.get('https://www.northernsafety.com/All-Categories', headers=headers)
# # sel=Selector(text=response.text)
# print(response.status_code)


##########################CRAWLER#######################
# page = 0

# while True:
#     payload = {
#         "requests": [
#             {
#                 "indexName": "WebProd",
#                 "params": f"clickAnalytics=true&facetFilters=%5B%5B%22Categories.lvl2%3ASafety%20Products%20%3E%20Clothing%20%3E%20Chemical%20Resistant%20Clothing%20%26%20Accessories%22%5D%5D&facets=%5B%22*%22%5D&highlightPostTag=__%2Fais-highlight__&highlightPreTag=__ais-highlight__&hitsPerPage=24&maxValuesPerFacet=1000&page={page}&query=&userToken=anonymous-6d272426-caf9-4dd0-9955-a16888c27f25&analytics=true"
#             },
#         ]
#     }

#     response = requests.post(
#         'https://i45i79oc23-1.algolianet.com/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.23.2)%3B%20Browser',
#         headers=headers,
#         data=json.dumps(payload),
#     )
#     data = response.json()
#     result_list=data.get('results',[])
#     for list in result_list:
#         hits_list=list.get('hits',[])
#         for item in hits_list:
#             product_url=item.get('MaterialDetailPageURL','')
#             full_url=f"https://www.northernsafety.com{product_url}"
#             print(full_url)
#             print(page)
#     page+=1

######################################PARSER########################
import requests
cookies = {
    '_hjSessionUser_2090991': 'eyJpZCI6IjE1OGRiMDJlLTk3MTMtNThlNS1iMmNkLTE4ZjhiZWJkMTc1YSIsImNyZWF0ZWQiOjE3NTY4ODQ4MDcwMjksImV4aXN0aW5nIjp0cnVlfQ==',
    'CustomerTrackingId': 'bd8934b1-e4e0-4507-89e8-db34b33f5f89',
    'ai_user': '2F/DR|2025-09-03T08:50:23.924Z',
    '_ga': 'GA1.1.1389151866.1756889426',
    '_hjSession_2090991': 'eyJpZCI6IjM1ZTY0OWEyLWZhZTQtNDlkYS1iNGViLTA4MTRmN2NjYjlkZiIsImMiOjE3NTY4ODk0MjY1NTYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
    '_hjHasCachedUserAttributes': 'true',
    '__hstc': '209817226.1a35dc325ff892026c129cd6a1406618.1756889428337.1756889428337.1756889428337.1',
    'hubspotutk': '1a35dc325ff892026c129cd6a1406618',
    '__hssrc': '1',
    '_gcl_au': '1.1.162117646.1756889428',
    '_ALGOLIA': 'anonymous-1fbeff5e-5573-44f7-a7e8-83dc7e7bc75d',
    '_uetsid': '0c1c9ca088a311f0b633bf35da9119eb',
    '_uetvid': '0c1ce53088a311f09f62075d2ab2d171',
    'LPVID': 'I4MDIxNzY2NmY1NmYyMTZk',
    'LPSID-43298048': 'UKwtUb7fTxy4rjr8JhDLDg',
    '_fbp': 'fb.1.1756889432163.331157913252849878',
    '_ga_M67V68CZMT': 'GS2.1.s1756889425$o1$g1$t1756889643$j55$l0$h0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.northernsafety.com/Search/Safety-Products/Clothing/Chemical-Resistant-Clothing---Accessories',
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

url = "https://www.northernsafety.com/Product/155930/NSI-ActivGARD/6-mil-35-x-55-Blue-Vinyl-Sewn-Edge-Apron-Dozen"
response = requests.get(url,headers=headers)
print(response.status_code)








