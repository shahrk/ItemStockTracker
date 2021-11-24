"""
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import requests
from bs4 import BeautifulSoup
import re


class BestBuyScraper:
    """
    This is the Scraper for BestBuy. Takes in product url as input upon object creation.
    Method 'job' prints progress while the method 'check_stock' obtains stock info and a string indicating cost of the product.

    @author: qchen59
    """

    def __init__(self, url):
        """
        Initializes url upon object construction.
        :param url: URL of the product
        """
        self.url = url

    def check_stock_price(self, url):
        """
        Obtains stock information from the given url.

        :param url: URL of the product
        :return: a string indicating the stock information and a string indicating cost of the product
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:92.0) Gecko/20100101 Firefox/92.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }
        try:
            page = requests.get(url, headers=headers, timeout=5)
            # parsing the content of the page
            soup = BeautifulSoup(page.text, "html.parser")
        except:
            return "Error Occurred", "NA"

        cost = soup.find(
            "div", {"class": "priceView-hero-price priceView-customer-price"}
        )
        cost = str(cost.contents[0])
        # price = re.match("\$(\d*,)*\d*\.\d*", cost)
        price = "$" + cost.split("$")[1].split("<")[0]
        # print(price)

        try:

            button_add = soup.find("button", {"data-button-state": "ADD_TO_CART"})
            button_sold_out = soup.find("button", {"data-button-state": "SOLD_OUT"})

            if button_add and not button_sold_out:
                return "In Stock", price
            if button_sold_out:
                return "Out of Stock", "NA"
        except:
            return "Error Occurred", "NA"

    def job(self):
        """
        Prints the progress, and delegates the task to 'check_stock'.

        :return: a string indicating the stock information and a string indicating cost of the product
        """
        print("Tracking....")
        print("Processing: " + self.url)
        stock, cost = self.check_stock_price(self.url)
        print(stock, cost)
        return stock, cost
