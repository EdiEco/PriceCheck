


class Plugin:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def getValue(self, url):
        print("value")
    
    def formatProductName(self, text):
        return text.strip().ljust(60, " ")[:60]

    def formatProductPrice(self,text):
        return ("$" + text.strip().replace("$","").replace("CAD ", "")).strip().rjust(10, " ")