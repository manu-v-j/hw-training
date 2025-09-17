import requests
from xml.dom.minidom import parseString
import logging
logging.basicConfig(level=logging.INFO)


count=1
response = requests.get('https://www.lorespresso.com/en_gb/products-sitemap.xml')
dom = parseString(response.content)

for loc in dom.getElementsByTagName("loc"):
    url = loc.firstChild.data
    count+=1
    logging.info(url)
    logging.info(count)

