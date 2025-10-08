import requests
from xml.dom.minidom import parseString
import logging
logging.basicConfig(level=logging.INFO)


count=1
response = requests.get('https://www.bol.com/sitemap/nl-nl/product-983')
dom = parseString(response.content)

for loc in dom.getElementsByTagName("loc"):
    url = loc.firstChild.data
    count+=1
    logging.info(url)
    logging.info(count)

