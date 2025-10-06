import requests
import json,re
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.lidl.ch/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
}


postal_data = {
    "Debrecen": (47.547, 7.5923),   #4000
    "Kecskemét": (47.0491,8.3184),  #6000
}

base_url = (
    "https://spatial.virtualearth.net/REST/v1/data/"
    "7d24986af4ad4548bb34f034b067d207/Filialdaten-CH/Filialdaten-CH"
    "?$select=*,__Distance"
    "&$filter=Adresstyp eq 1"
    "&$format=json"
    "&key=Arc9d68zjLXOr_lYSOpy2g-xMwgE3l9XXCruscSsw-R52Nx32jlIhc59YAdAXGVd"
)

for city, (lat, lon) in postal_data.items():
    url = f"{base_url}&spatialFilter=nearby({lat},{lon},5)"

    response = requests.get(url, headers=headers)
    data = response.json()
    result_list=data.get('d',{}).get('results',[])
    for item in result_list:
        city=item.get('Locality','')
        zipcode=item.get('PostalCode','')
        street=item.get('AddressLine','')
        print(street)

         
