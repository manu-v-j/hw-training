import re
import urllib.parse

url = "https://www.northernsafety.com/Search/Safety-Products/Clothing/Chemical-Resistant-Clothing---Accessories"
parts = [s for s in url.split("/") if s][3:]

category, subcategory, product = parts

product_text = product.replace("---", " & ")

category_text = category.replace("-", " ")
subcategory_text = subcategory.replace("-", " ")
product_text = product_text.replace("-", " ")

facet_string = f"Categories.lvl2:{category_text} > {subcategory_text} > {product_text}"

facet_encoded = urllib.parse.quote(facet_string)

print(facet_encoded)
