import re
import requests
import io
from bs4 import BeautifulSoup
from Plugin import Plugin

class PluginCanadaComputers(Plugin):
    """Plugin class"""
    def __init__(self):
        self.name = "Canada Computers"
        self.url = "canadacomputers.com"

    def getValue(self, url):
        text_name = "N\A"
        text_price = "N\A"
        text_available = "N\A"

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
    
        product_name = soup.find('h1', attrs={'class': 'h3 mb-0'})
        product_price = soup.find('div', attrs={'class': 'row price-show-panel'}).find('span').find('strong')
        product_available = soup.find('div', attrs={'pi-prod-availability'}).find('i', attrs={'class': 'fas fa-ban red text-danger'})

        if product_name != None:
            text_name = self.formatProductName(product_name.text)
        else:
            text_name = ""

        if product_price != None:
            text_price = self.formatProductPrice(product_price.text)
        else:
            text_price = ""

        if product_available != None:
            text_available = "Not Available"
        else:
            text_available = "Available"   

        print(self.name + " | " + text_name + " | " + text_price + " | " + text_available)

