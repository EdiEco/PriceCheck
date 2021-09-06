import re
import requests
import io
from bs4 import BeautifulSoup
from Plugin import Plugin

class PluginDell(Plugin):
    """Plugin class"""
    def __init__(self):
        self.name = "Dell"
        self.url = "dell.com"

    def getValue(self, url):
        text_name = "N\A"
        text_price = "N\A"
        text_available = "N\A"

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        product_name = soup.find('div', attrs={'class': 'pg-title'}).find('h1').find('span')
        product_price = soup.find('div', attrs={'class': 'ps-dell-price'})
        product_available = soup.find('a', attrs={'data-testid': 'addToCartButton'})

        if product_name != None:
            text_name = self.formatProductName(product_name.text)
        else:
            text_name = ""

        if product_price != None:
            text_price = self.formatProductPrice(product_price.text)
        else:
            text_price = ""

        if product_available != None:
            text_available = "Available"
        else:
            text_available = "Not Available"   

        print(self.name + " | " + text_name + " | " + text_price + " | " + text_available)

