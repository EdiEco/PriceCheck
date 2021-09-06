from Plugin import Plugin
import json
from io import StringIO
from PluginDell import PluginDell
from PluginCanadaComputers import PluginCanadaComputers
from PluginAmazon import PluginAmazon
from PluginBestBuy import PluginBestBuy

cDell = PluginDell()
cCanadaComputers = PluginCanadaComputers()
cAmazon = PluginAmazon()
cBestBuy = PluginBestBuy()

plugins = [cDell, cCanadaComputers, cAmazon, cBestBuy]

with open('list.json') as f:
  data = json.load(f)

for i in data['URLs']:
    url = i['url']
    for plugin in plugins: 
        if url.find(plugin.url) != -1:
            plugin.getValue(url)
