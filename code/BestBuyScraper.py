import requests
from bs4 import BeautifulSoup


class BestbuyScraper:
    def __init__(self, url):
        self.url = url

    def CheckStock(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        page = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(page.text, 'lxml')  # parsing the content of the page
        try:
            button_add = soup.find('button', {'data-button-state': 'ADD_TO_CART'})
            button_soldout = soup.find('button', {'data-button-state': 'SOLD_OUT'})
            if button_add and not button_soldout:
                return "In Stock"
            if button_soldout and not button_add:
                return "No Stock Info"
        except:
            return "Error Occurred"

    def job(self):
        print("Tracking....")
        print("Processing: " + self.url)
        stock = self.CheckStock(self.url)
        print(stock)
        return stock
