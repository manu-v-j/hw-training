import requests
import xml.etree.ElementTree as ET
product_link=[]
product_list=[]
url='https://www.westside.com/sitemap.xml'
response=requests.get(url)
if response.status_code==200:
    xml_content=response.content

    root=ET.fromstring(xml_content)
    namespace={'ns':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    for url in root.findall('ns:sitemap',namespaces=namespace):
        loc=url.find('ns:loc',namespaces=namespace)
        if loc is not None and 'products' in loc.text:
            product_list.append(loc.text)
for url in product_list:
    response_product=requests.get(url)
 
    if response_product.status_code == 200:
        xml_content = response_product.content
        root = ET.fromstring(xml_content)

        for url in root.findall('ns:url', namespaces=namespace):
            loc = url.find('ns:loc', namespaces=namespace)
            lastmod = url.find('ns:lastmod', namespaces=namespace)

            if loc is not None:
                product_link.append(loc.text)

print(len(product_link))