import requests
from bs4 import BeautifulSoup


class BestBuyScraper:
    """
    This is the Scraper for BestBuy. Takes in product url as input upon object creation.
    Method 'job' prints progress while the method 'check_stock' obtains stock info.

    @author: qchen59
    """

    def __init__(self, url):
        """
        Initializes url upon object construction.
        :param url: URL of the product
        """
        self.url = url

    def check_stock(self, url):
        """
        Obtains stock information from the given url.

        :param url: URL of the product
        :return: a string indicating the stock information
        """
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
            button_sold_out = soup.find('button', {'data-button-state': 'SOLD_OUT'})
            if button_add and not button_sold_out:
                return "In Stock"
            if button_sold_out:
                return "Out of Stock"
        except:
            return "Error Occurred"

    def job(self):
        """
        Prints the progress, and delegates the task to 'check_stock'.
        
        :return: a string indicating the stock information
        """
        print("Tracking....")
        print("Processing: " + self.url)
        stock = self.check_stock(self.url)
        print(stock)
        return stock
