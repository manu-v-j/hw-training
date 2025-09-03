import requests,json
from parsel import Selector

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.stradivarius.com/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'ITXSESSIONID=9ad0eee2e2bbd8d67452f8b057d0b370; STDSESSION=cda591d6acf966b7e8d7bb6bb8b12327; bm_ss=ab8e18ef4e; bm_mi=933DF69FE311C549AFB63FCAED3850BB~YAAQNbxWaJCKLtCYAQAAJdt4AxzcXkr7mFhGRrbjwF4isgWG9eAma1v9qQKPlAk7HgRUegLyVSD9UgPLI7mps8GFp3rm+gc1N3i2dzlWQwKuX82rY4bGN8LqQtymU0zdi8Al6XExFdKYxGDM3xgcPR+5AsovzTK1KVjXMZPxolLZbPWVrdZnsLEymzbYU+02MRGE4GbLXSzdFAgvDRaHD70HGrW5K2lkmEk9EXi0JwQEnnVBeFG8rBZDnvSZIhNggA9dHYJrU2rMiqQWpVEXHUmpRVqOHZuELQbdtuNu1H9IaPqbzv7Q4WxIoiqK/6sTG+03CeFXlg==~1; IDROSTA=3286ddbb7434:2d7633bba16c9ef5759860058; UAITXID=fc92b99d09947e0336583ab7ab8de4cd2c64d791ef9adf969c5687eb85c69b6c; ak_bmsc=6553FCA4D72E5182EEF134FBD9176696~000000000000000000000000000000~YAAQNbxWaJ6KLtCYAQAAAv54AxxGJKbvumrUN+vyeun39dlzzgJbejuDvOzfvnhNnxBz4iDSPMs75/tsTart4gIoeFNjXFFIdT/3IdAyl0DjKhnr9dP1/D621EuxfVke5Wqo4bTOtGR0hFEKlFmExNXgNSbPNZ8npUrUh4gZEEgkExUkqRmERDQljG8kNQBwKQbwLSZRErKemCWr86wOlNEcXbwZ0/6mogKXFxAHfzwJTIAm0+hkznONWXJrNAlfT6vj5wjTgi4933QkHjfcDCcJ8FIb47G6HNC0+drJP9H+0k6Q+sIC27dqUEH3LC5ieystXXUOfQM1Q23l+CgDdPXlvzgYdb612RTCMFh3Hoyn52XZHAddN1RWhyVZGKCuISxprhVZKd94tYeZn9IBlIWwKyjj7Gqj/wa7prvGCqJs26cAZMXLjGGc//Tj3l0erhSY18Cy3FguvySx30SxWvlvGT77Rqu/kqd+GB+9mVYtMLoq4R0DOxBpYTkl52UHtdb3MqVVwA9pInKaCdZPwtUScm3XzmEzaZ2T9Fm9SXjzTzHU2Ljn2jD9fq41FzckRwo1gomh62daQhL4z3iwarpqQH6HjuyEx7H4sxSHXfrl9SvRYsQrGKtgVgdo; _gcl_au=1.1.677158018.1756699888; _ga=GA1.1.1588370446.1756699997; _imutc=e29f33deee890954414669cabdb3574e4f08259ecd15e55848f9e9020dfc6b10; optimizelyEndUserId=oeu1756700002982r0.5755830719933829; FPID=FPID2.2.9HWW%2B8yiaqynq2IX5XOJEhlMSzwVJ9wBzDqpFG1Id9w%3D.1756699997; FPLC=wn0a8eb%2Brwq59AmUkNUDnVjxM%2F607ePamYOwGV1PE%2BylFBGvqDqNQjMH59ZW8cUMJsHnnL7db5L2YKYJvc0DqygQe6GWSrBSb5IxmNTj%2BApj0TsTyyRa%2FsZFKIdvJw%3D%3D; _gtmeec=e30%3D; _fbp=fb.1.1756700003830.1882719002; _screload=; _ScCbts=%5B%22603%3Bchrome.2%3A2%3A5%22%5D; _sctr=1%7C1756665000000; ORA_FPC=id=13255061-7ad6-43a3-9b34-a0b3b61c7fef; WTPERSIST=; _abck=C303134E6745F7ABC49CA94840FBABB8~0~YAAQNbxWaOGKLtCYAQAAhu97Aw7BsC6zf6DiVrXRedl9bYLjNxA7syLqLcHdohSsfIMloLekO3KSVlOevdsC9mQiRNirBzbuNMlPXKmss/HHxcPXZLzg0j4C42+SmiwPISvtiqZ1RjnlosPpYfF9iY5mIEMksFaBBY2WCbROPeLzPJTMxcP4+x9noWWXSDEAKqaagj5xIugMlGLz2jolaedWDVeYOJjqNYNfkbq/DiihGDBUpwlxcBz05vwnd1gcNyECVts7ZoagPOqAFPbwi2oTshLLuMUC26bBsnEA9vYvyPtV6rE5MC8pqmDry8f+iRevEWEq8ky+vqufMOOtaUwG4HJO2kxafYgkgSWcPGdmCXtwyARG6xs5uCjzcB8MDBE/TYtZ98pCl2pnDG4io1NM/X+RJTADJqEQ3c2m+SSO+Ukk8z/WkBPj0Uf+SbWNcL96radLr8TXNnwQIOPyjJgEogjw7ANBJRYeP52wQhGpG7XKr/0GtGgwY/MkPE0JeGiRIZTzZOpPkqD6s7tjZZlZwZicVG9BFDjU9xLBMMmGbAuOutnB3tAN6rVdKXBcTP0qPGMGvPIvk49BRNNkYh+kURI7l+D0wSQHsVgQ6qlVb3T7bDqL0cIOgo1bzAxQyhwyTU8BOQ==~-1~-1~1756703484~~; OptanonConsent=isGpcEnabled=0&datestamp=01%2F09%2F2025&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=51fd17b6-6ac9-4c78-b1f1-8a40cd33fd02&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&intType=3&geolocation=IN%3BKL&AwaitingReconsent=false; _scid=h-8quMak5a94e75TbkcJZot05jnWXPGxKT8WpQ; _scid_r=gO8quMak5a94e75TbkcJZot05jnWXPGxKT8Wrg; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22WjpC5xhCyTov166cfWZb%22%2C%22expiryDate%22%3A%222026-09-01T04%3A19%3A11.711Z%22%7D; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknow%22%2C%22expiryDate%22%3A%222026-09-01T04%3A19%3A13.807Z%22%7D; _ga_NOTFORGA4TRACKING=GS2.1.s1756700001$o1$g1$t1756700379$j24$l0$h429498774; _ga_LQGSX5V976=GS2.1.s1756699997$o1$g1$t1756700379$j24$l0$h0; itx-audience-id=sales; itx-audience-progressive-entry=0; itx-seven-audience=%7B%22event%22%3A%22none%22%2C%22subevent%22%3A%22onevent%22%2C%22apply%22%3A%22true%22%7D; bm_s=YAAQNbxWaCyMLtCYAQAAGeOAAwMuCSPKLJ7BwS2qx7tH5cn6QvbnRGZ4x7A9m87MUT+s4eW3JMTmvxhwfuWjtclMSmXV2lIDJKLjI3nro2+gHOw1Q3Hhl6p+APnz1R7slC3CWUbXnyOBR1f2ScxjoZ23phOFewK7jQbHAJQRoeFd9mEDy8stYe9WlEs5Jiff+aea4tgdO9kYVVamU2MmFOP3GDXAaXvCdQrQQiaF6S8bxj1LlmIQ6R6xPmfRXw1Z9yaGYhRXzxt3Xb9U64U9DJTFHrOPhQTrdz8G6VVJZzA727VSmQixmDvnVPZoZEwkDIxqqHDUwBdlFJxn80WQd+d8XO9jlpNX04DCVpdz6ifyQ0pfkN3qlle+EOYPAOnOs0V4dwbrly/kdaM5jyYgjrGVPRRydeAeuoOwFSUtNQFsdKpmcNOGo6uWb6DrLt+BrRIieMXAyuzL2BwmvsXmCtCRN8dStCAPS1H0SdH0dvS0n2ZvI1FuDIquWx+7dNOHsaNMf0gAHyQh4zRGM2pcHFGyoir30/VeWW71HhNh6qmCSH7nTNn+jtDoX4LLF3iqgOt8N+Hn5RTuMsmV+hPEIzY3qxj9hjz8g7InXYzedjzU/CXC4A0J+i+1lrjdcMO47tLAwxV2ZjfpRQ==; bm_so=6364A35490835CD4470411EDF77FCE0FE6189163867415EAB412BBE2D04A0B51~YAAQNbxWaC2MLtCYAQAAGuOAAwT6Iyd6/ucHMQtQCVZSrTxchATwYOHQ0ranJ0948CU0tVgjWExYcLCfGNZi1qjUkhgJscarExD+pbTw8tDiTz1qTvMMO4UMXqWfiHbwjPbdVGk3n68Zm1Ai2G7hosT5yw/Oa3rNn+0gULx9yMDBfUgnTL8JoPtiTQsaZtNv69E5XqP4Ea/+ZyAfQbTavjb00TFfpshexMc3fjkj4BjWnFlsjVOLlzqUWR38sN2ZK+DHTtK/DSMChbm3J0life99NMpTjuxwpv9FS+MVVZFyKGjOXgIcp3vSabDzyMkjZFAKqy2MKcK+ESlX6F/5nwwdlUTj9UkoYaIBwP6L+RTCHLmRncMnbt1/GSnKnUeCWtnxXckicnRbYtlyWDNXUls9cclh16HZAljsuI60w2CvzcJdDpgR0Fvilie2W1+W03L1uo/OW3wMA60SxdLWcPBDYWRWablu6B6NtokIQfnOzV0OK7Sti5mOmw2byw==; bm_sz=A01E912EB1EF48953FD6419C40442E18~YAAQNbxWaC+MLtCYAQAAGuOAAxxfH+Cq/+EUtEK7XP9PLpL2b3xGuOKXcihJlOK8NHmU2CjOQ4xCZLkQxiJYzWyux7Bvhf8Xo0+SFU6RoHS+JvhDJM/Ag5DEs9r/NzTabFb6ZIL2axDKoj50c95SfEmfZFeLPE7UEDTAZbv4d9fxWblt4DsGP3b6TTb4lqiLkscI/pvttcmsZkAGYkWwoMDSOzSuGIyk/h8WrEiZIN4jni38ZBPXB+FitDiqjNxaO9fRp5XD7Y4pLQ6nohxfMPMJMw8bErqq8FrnFToQgxElIa4HuMQQvMbTos9e2Wu1V/+aBtCRs9JjAz3o9nSPjJvpvXtZaRwPW1YenK2oMhZx2jae1F04Hq+srIzfkiNvxxVvEWuPBymVheJLIOh28Dg3DRSSMS49UFbL9afn8xurgQ/m8YdTrXD7ndq/VrFLBwDqXtzfk0zoCmsFK9UwSXm4o1sEF12m/OPgJ12ClJyhG100uxw8u2+mj3MV/XmSpSrgnAUoURPoJUOd+kF19dgazzTaUT6s6xnxg/NVFhoT3s6TAEuc4euq0FzU1JhMelljbYjy13m0Hw==~3228737~3748152; optimizelySession=1756700403272; TS01e201b5=01bad81f5bcf8393a4192534fb5c4346a13a35179b53d92c8980442852efcdc210829ccbfe4e1fde1189920416d894efdce6ab32e3; OptanonAlertBoxClosed=2025-09-01T04:20:10.824Z; bm_sv=FEB0C4271BEA8C2D7405C4E61651308D~YAAQNbxWaDqMLtCYAQAAbg+BAxyLPNttTheKVpxjj7iHyOLsQsN213PG66BC7+Sg0oM5VAW9EVMiSIdAkFnypbvSO8jEiwlBGpQpGyHb1gVNNWtnnwxbVkaSGY0DzAVolgG1UevPgVbYuaZxFrgZi92juDF8s8lc/alVka+QB82Nc9QzqmezA96OL3ZIggKxCNSIWLUmCufm67ddqGWggVH16vXzgHpDD6SY7Qvja1MlV3TXmYERDgAH4cl/Uz21JLg7vuhN9OI=~1; bm_lso=6364A35490835CD4470411EDF77FCE0FE6189163867415EAB412BBE2D04A0B51~YAAQNbxWaC2MLtCYAQAAGuOAAwT6Iyd6/ucHMQtQCVZSrTxchATwYOHQ0ranJ0948CU0tVgjWExYcLCfGNZi1qjUkhgJscarExD+pbTw8tDiTz1qTvMMO4UMXqWfiHbwjPbdVGk3n68Zm1Ai2G7hosT5yw/Oa3rNn+0gULx9yMDBfUgnTL8JoPtiTQsaZtNv69E5XqP4Ea/+ZyAfQbTavjb00TFfpshexMc3fjkj4BjWnFlsjVOLlzqUWR38sN2ZK+DHTtK/DSMChbm3J0life99NMpTjuxwpv9FS+MVVZFyKGjOXgIcp3vSabDzyMkjZFAKqy2MKcK+ESlX6F/5nwwdlUTj9UkoYaIBwP6L+RTCHLmRncMnbt1/GSnKnUeCWtnxXckicnRbYtlyWDNXUls9cclh16HZAljsuI60w2CvzcJdDpgR0Fvilie2W1+W03L1uo/OW3wMA60SxdLWcPBDYWRWablu6B6NtokIQfnOzV0OK7Sti5mOmw2byw==^1756700414086',
}

#############################CATEGORY$$#############################
# params = {
#     'languageId': '-1',
#     'typeCatalog': '1',
#     'appId': '1',
# }

# response = requests.get(
#     'https://www.stradivarius.com/itxrest/2/catalog/store/55009581/50331096/category',
#     params=params,
#     headers=headers,
# )
# data=response.json()


# ###############CRAWLER#####################################################
# params = {
#     'languageId': '-1',
#     'showProducts': 'false',
#     'priceFilter': 'true',
#     'appId': '1',
# }
# response = requests.get(
#     'https://www.stradivarius.com/itxrest/3/catalog/store/55009581/50331096/category/1020629924/product',
#     params=params,
#     headers=headers,
# )
# response.raise_for_status()
# data = response.json()

# element_list = data.get('gridElements', [])
# all_pids = []
# for item in element_list:
#     product_ids = item.get('ccIds', [])
#     all_pids.extend(product_ids)

# for pid in all_pids:
#     params = {
#         'languageId': '-1',
#         'categoryId': '1390584',
#         'productIds': str(pid),   
#         'appId': '1',
#     }

#     response = requests.get(
#         'https://www.stradivarius.com/itxrest/3/catalog/store/55009581/50331096/productsArray',
#         params=params,
#         headers=headers,
#     )
#     response.raise_for_status()
#     data = response.json()

#     product_list = data.get('products', [])
#     for product in product_list:
#         summary_list = product.get('bundleProductSummaries', [])
#         for item in summary_list:
#             url = item.get('productUrl', '').lstrip('/')
#             if url:
#                 full_url = f"https://www.stradivarius.com/ae/{url}"
#                 print(full_url)
               
#######################PARSER#####################################
params = {
    'languageId': '-1',
    'appId': '1',
}

response = requests.get(
    'https://www.stradivarius.com/itxrest/2/catalog/store/55009581/50331096/category/0/product/455321208/detail',
    params=params,
    headers=headers,
)

data=response.json()
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
product_id=data.get('id','')
product_summary_list=data.get('bundleProductSummaries',[])
for item in product_summary_list:
    product_description=item.get('detail',{}).get('longDescription','')
color=[]
color_list=data.get('bundleColors',[])
for c in color_list:
    colors = c.get('name', '')
    color.append(colors)
print(color)

for item in product_summary_list:
    color_list = item.get('detail',{}).get('colors', [])
    for color in color_list:
        sizes = color.get('sizes', [])
        for size in sizes:
            price = size.get('price', '')

