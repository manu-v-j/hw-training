import requests
import json
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.lidl.it',
    'Referer': 'https://www.lidl.it/',
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
    "Vicenza": (45.7279, 11.6313),
    "Padova": (45.6305, 11.9361),
  
}

delta_1=0.364
delta_2=0.182
for city, (lat, lon) in postal_data.items():
    geo_box=f"{lat - delta_1},{lon - delta_2}:{lat},{lon}"
    base_url=f"https://live.api.schwarz/odj/stores-api/v2/myapi/stores-frontend/stores?limit=25&offset=0&country_code=IT&geo_box={geo_box}"
    response = requests.get(
        base_url,
        headers=headers,
    )

    data=response.json()
    number_locations=data.get('meta',{}).get('total','')
    item_list=data.get('items',[])
    for item in item_list:
        city=item.get('address',{}).get('city','')
        zipcode=item.get('address',{}).get('zip','')
        street=item.get('address',{}).get('streetName','')
        print(city) 