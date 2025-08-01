import requests
from parsel import Selector
url='https://www.robertsbrothers.com/roster/Agents'
response=requests.get(url)
print(response.status_code)