from curl_cffi import requests
import gzip
import io
from xml.dom.minidom import parseString
import logging
import json
logging.basicConfig(level=logging.INFO)



headers={
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'priority':'u=0,i',
    'referer':'https://www.oreillyauto.com/shop/b/accessories/atv---motorcycle-accessories/338fb64b0473',
    'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'Linux',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1'
    
}
url = "https://www.oreillyauto.com/sitemap1.xml.gz"
response = requests.get(url, headers=headers)

with gzip.GzipFile(fileobj=io.BytesIO(response.content)) as gz:
    xml_content = gz.read().decode('utf-8')

dom = parseString(xml_content)

product_list = []
count = 1
for loc in dom.getElementsByTagName("loc"):
    url_value = loc.firstChild.data
    logging.info(f"{count}: {url_value}")
    count += 1


