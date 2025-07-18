import requests
from xml.dom.minidom import parseString
import logging
import json

# Set logging level
logging.basicConfig(level=logging.INFO)
product_urls=[]
count = 1
limit = 500
site_urls = [
    'https://www.tesco.com/sitemaps/en-GB/groceries/products-1.xml',
    'https://www.tesco.com/sitemaps/en-GB/groceries/products-2.xml',
    'https://www.tesco.com/sitemaps/en-GB/groceries/products-3.xml',
    'https://www.tesco.com/sitemaps/en-GB/groceries/products-4.xml',
    'https://www.tesco.com/sitemaps/en-GB/groceries/products-5.xml',
    'https://www.tesco.com/sitemaps/en-GB/groceries/products-6.xml',
    'https://www.tesco.com/sitemaps/en-GB/groceries/products-7.xml',
    'https://www.tesco.com/sitemaps/en-GB/groceries/products-8.xml'
]

for url in site_urls:
    if count > limit:
        break
    response = requests.get(url)
    dom = parseString(response.content)
    for loc in dom.getElementsByTagName("loc"):
        if count > limit:
            break
        product_url = loc.firstChild.data
        logging.info(f"{count}: {product_url}")
        product_urls.append(product_url)
        count += 1

with open('product_link.json', 'w') as f:
    json.dump(product_urls, f, indent=2)