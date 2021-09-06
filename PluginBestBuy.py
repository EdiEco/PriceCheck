import re
import requests
import io
from bs4 import BeautifulSoup
from Plugin import Plugin

class PluginBestBuy(Plugin):
    """Plugin class"""
    def __init__(self):
        self.name = "BestBuy"
        self.url = "bestbuy.ca"

    def getValue(self, url):
        text_name = "N\A"
        text_price = "N\A"
        text_available = "N\A"
        HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

        r = requests.get(url,headers=HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        product_name = soup.find('div', attrs={'class': 'x-product-detail-page'}).find('h1', attrs={'class':'productName_3nyxM'})
        product_price = soup.find('div', attrs={'class': 'x-product-detail-page'}).find('span', attrs={'class': 'screenReaderOnly_3anTj'})
        product_available = soup.find('span', attrs={'class': 'availabilityMessage_ig-s5'})

        if product_name != None:
            text_name = self.formatProductName(product_name.text)
        else:
            text_name = ""

        if product_price != None:
            text_price = self.formatProductPrice(product_price.text)
        else:
            text_price = ""

        if product_available != None:
            text_available = product_available.get_text()
            if text_available == "Available to ship":
                text_available = "Available"
            else:
                text_available = "Not Available"   
        else:
            text_available = "Not Available"   

        print(self.name + " | " + text_name + " | " + text_price + " | " + text_available)
