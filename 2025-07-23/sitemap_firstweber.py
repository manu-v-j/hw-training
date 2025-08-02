from curl_cffi import requests
import gzip
import io
from xml.dom.minidom import parseString
import logging
logging.basicConfig(level=logging.INFO)

url = "https://www.firstweber.com/sitemapbio.xml.gz"
response = requests.get(url,impersonate='chrome')

with gzip.GzipFile(fileobj=io.BytesIO(response.content)) as gz:
    xml_content = gz.read().decode('utf-8')

dom = parseString(xml_content)

count = 1
for loc in dom.getElementsByTagName("loc"):
    url = loc.firstChild.data
    logging.info(f"{count}: {url}")
    count += 1
    print(count)
