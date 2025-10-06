import requests
import json

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.lidl.si',
    'Referer': 'https://www.lidl.si/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'x-apikey': '16QaHsGX3Uc3JLhNlS2ZG1CmosbzVPs2',
}

postal_data = {
    "Ljubljana": (46.056946, 14.505751),
    # "Maribor": (46.554722, 15.645833),
    # "Celje": (46.240833, 15.267222),
}

for city, (lat, lon) in postal_data.items():
    lat_min = lat - 0.1
    lat_max = lat + 0.1
    lon_min = lon - 0.1
    lon_max = lon + 0.1

    url = (
        f"https://live.api.schwarz/odj/stores-api/v2/myapi/stores-frontend/stores"
        f"?limit=25&offset=0&country_code=SI"
        f"&geo_box={lat_min},{lon_min}:{lat_max},{lon_max}"
    )

    # print(f" Fetching stores for {city}")
    response = requests.get(url, headers=headers)
    data = response.json()
    number_locations=data.get('meta',{}).get('total','')
    item_list=data.get('items',[])
    for item in item_list:
        city=item.get('address',{}).get('city','')
        zipcode=item.get('address',{}).get('zip','')
        street=item.get('address',{}).get('streetName','')
        print(street)