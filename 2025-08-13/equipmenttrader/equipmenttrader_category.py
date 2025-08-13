import requests
from parsel import Selector
from settings import headers,base_url

class Category:
    def __init__(self):
        pass

    def start(self):
        response=requests.get(base_url,headers=headers)
        