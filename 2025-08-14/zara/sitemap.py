from curl_cffi import requests
import gzip
import io
from xml.dom.minidom import parseString
import logging
import json
logging.basicConfig(level=logging.INFO)

url = "https://www.zara.com/sitemaps/sitemap-am-en.xml.gz"
response = requests.get(url)

with gzip.GzipFile(fileobj=io.BytesIO(response.content)) as gz:
    xml_content = gz.read().decode('utf-8')

dom = parseString(xml_content)

product_list = []
count = 1
for loc in dom.getElementsByTagName("loc"):
    url_value = loc.firstChild.data
    logging.info(f"{count}: {url_value}")
    count += 1