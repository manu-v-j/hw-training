import requests
from settings import headers
import json
from parsel import Selector
response=requests.get('https://auchan.hu/api/v2/products/sku/791178?category_id=5680&hl=hu',headers=headers)
data=response.json()
output_file = 'product_details.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)