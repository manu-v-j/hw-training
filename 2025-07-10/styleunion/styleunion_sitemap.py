import requests
from xml.dom.minidom import parseString
import logging
logging.basicConfig(level=logging.INFO)


count=1
response = requests.get('https://styleunion.in/sitemap_products_1.xml?from=7961041436921&to=8332742033657')
dom = parseString(response.content)

for loc in dom.getElementsByTagName("loc"):
    url = loc.firstChild.data
    count+=1
    logging.info(url)
    logging.info(count)