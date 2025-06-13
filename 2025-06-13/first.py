import requests
import re
import json

payload = {
    "passkey": "tpcm2y0z48bicyt0z3et5n2xf",
    "apiversion": "5.5",
    "displaycode": "2001-en_us",
    "resource.q0": "products",
    "filter.q0": "id:eq:300429178",
}

response = requests.get("https://api.bazaarvoice.com/data/batch.json", params=payload)
raw_text = response.text

json_str = re.sub(r'^BV\._internal\.dataHandler0\((.*)\)$', r'\1', raw_text)

json_obj = json.loads(json_str)

pretty_json = json.dumps(json_obj)

print(pretty_json)
