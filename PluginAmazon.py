import re
import requests
import io
from bs4 import BeautifulSoup
from Plugin import Plugin

class PluginAmazon(Plugin):
    """Plugin class"""
    def __init__(self):
        self.name = "Amazon"
        self.url = "amazon.ca"

    def getValue(self, url):
        text_name = "N\A"
        text_price = "N\A"
        text_available = "N\A"
        HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

        r = requests.get(url,headers=HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        product_name = soup.find(id='productTitle')
        product_price = soup.find('span', attrs={'id': 'price_inside_buybox'})
        product_available = soup.find('div', attrs={'id': 'availability'}).find('span', attrs={'class': 'a-color-success'})

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

