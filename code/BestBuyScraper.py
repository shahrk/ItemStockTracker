import requests
from bs4 import BeautifulSoup


# Scraper for BestBuy
# Takes in product url as input upon object creation
# 'job' prints progress while 'CheckStock' obtains stock info
# @author qchen59

class BestBuyScraper:
    def __init__(self, url):
        self.url = url

    # Obtains stock information from the given url
    # @param url URL of the product
    def CheckStock(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:92.0) Gecko/20100101 Firefox/92.0',
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
            if button_add:
                return "In Stock"
            if button_soldout:
                return "Out of Stock"
        except:
            return "Error Occurred"

    # Prints the progress, and delegates the task to 'CheckStock'
    def job(self):
        print("Tracking....")
        print("Processing: " + self.url)
        stock = self.CheckStock(self.url)
        print(stock)
        return stock
