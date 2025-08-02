import requests
import gzip
import io
from xml.dom.minidom import parseString
import logging
import json
logging.basicConfig(level=logging.INFO)

url = "https://www.hoogvliet.com/sitemap-product-0.xml.gz?SyndicationID=SiteMapXML"
response = requests.get(url)

with gzip.GzipFile(fileobj=io.BytesIO(response.content)) as gz:
    xml_content = gz.read().decode('utf-8')

dom = parseString(xml_content)
product_list = []
count = 1

while count <= 500:
    for loc in dom.getElementsByTagName("loc"):
        url = loc.firstChild.data
        logging.info(f"{count}: {url}")
        count += 1
        product_list.append(url)
        if count > 500:
            break
    break  

with open('product_link.json', 'w') as f:
    json.dump(product_list, f, indent=2)