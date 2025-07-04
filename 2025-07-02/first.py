import requests

url = "https://translate-pa.googleapis.com/v1/translateHtml?key=AIzaSyATBXajvzQLTDHEQbcpq0Ihe0vWDHmO520"

payload = [
    [
        ["11110509", "04-07-2025", "OtherData"], 
        "mr", 
        "en"
    ], 
    "te_lib"
]

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

response = requests.post(url, headers=headers, json=payload, verify=False)
print(response.text)
