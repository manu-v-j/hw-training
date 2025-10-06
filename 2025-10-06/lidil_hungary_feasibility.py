import requests
import json,re
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.lidl.hu/',
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
    "Budapest": (47.4997, 19.0506),   # 1051
    "Debrecen": (47.5316, 21.6273),   # 4024
 
}

base_url = (
    "https://spatial.virtualearth.net/REST/v1/data/"
    "4c781cd459b444558df3d574f082358d/Filialdaten-HU/Filialdaten-HU"
    "?$select=*,__Distance"
    "&$filter=Adresstyp eq 1"
    "&$format=json"
    "&key=AtyLGapcn9s0j908FQtR0SAftUVJ4ZS7y2WpYPJdxn3xc2cXSKZ7Nsemr5qJsXLO"
)

for city, (lat, lon) in postal_data.items():
    url = f"{base_url}&spatialFilter=nearby({lat},{lon},5.8095405)"
    
    response = requests.get(url, headers=headers)
    data = response.json()
    item_list=data.get('d',{}).get('results',[])
    for item in item_list:
        city=item.get('Locality','')
        zipcode=item.get('PostalCode','')
        street=item.get('AddressLine','')
        print(street)
    
