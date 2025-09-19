import requests
import json
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.postgraduate.study.cam.ac.uk',
    'priority': 'u=1, i',
    'referer': 'https://www.postgraduate.study.cam.ac.uk/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
}

response = requests.get('https://gaobase.admin.cam.ac.uk/api/courses.datatable', headers=headers)
data=response.json()
with open("courses.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)