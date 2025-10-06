import requests
import re,json
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.lidl.ie/',
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
    "Dublin": (53.3494, -6.2606),
    "Cork": (51.8985, -8.4756),
    "Limerick": (52.6638, -8.6267),
    "Galway": (53.2707, -9.0568),
}

base_url = (
    "https://spatial.virtualearth.net/REST/v1/data/"
    "94c7e19092854548b3be21b155af58a1/Filialdaten-RIE/Filialdaten-RIE"
    "?$select=*,__Distance"
    "&$filter=Adresstyp eq 1"
    "&$format=json"
    "&jsonp=Microsoft_Maps_Network_QueryAPI_1"
    "&key=Ap3P77iJrwF6TtEn3OH6986-LY-D-TV3yiBKvr_jjMmTnkF2C6cUzG9CGvrzSL7W"
)

for city, (lat, lon) in postal_data.items():
    url = f"{base_url}&spatialFilter=nearby({lat},{lon},5)"

    response = requests.get(url, headers=headers)
    raw_text = response.text

    match = re.search(r'Microsoft_Maps_Network_QueryAPI_1\((.*)\)', raw_text, re.DOTALL)
    if match:
        json_str = match.group(1)
        data = json.loads(json_str)
        result_list=data.get('d',{}).get('results',[])
        for item in result_list:
            city=item.get('Locality','')
            zipcode=item.get('PostalCode','')
            street=item.get('AddressLine','')

              
     

