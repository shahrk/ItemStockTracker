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


class WalmartScraper:
    """
    This is the Scraper for Walmart. Takes in product url as input upon object creation.
    Method 'job' prints progress while method 'check_stock' obtains stock info and a string indicating cost of the product.

    Walmart pages can have stock info in different ways. Following are the possible cases,
    interpretations, and return values of each case.

        * "Add to Cart" - Product is in stock - return "In Stock"
        * "Out of Stock" - product is out of Stock - return "Out of Stock"

    @author: gavinilakshmiswetha
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
        # Handles invalid URLs/timeouts
        except:
            return "Error Occurred", "NA"

        try:

            scraped_data = soup.find("div", {"data-testid": "add-to-cart-section"})

            cost = soup.find("span", {"itemprop": "price"})
            cost = cost.contents[0]
            # print("cost", cost)

            if "Add to cart" in str(scraped_data):
                return "In Stock", cost
            elif "Out of stock" in str(scraped_data):
                return "Out of Stock", "NA"
        except:
            return "Error Occurred", "NA"

    def job(self):
        """
        Prints the progress, and delegates the task to 'check_stock'.

        :return: a string indicating the stock information and a string indicating cost of the product
        """
        print("Tracking....")
        # print("Processing: " + self.url)
        stock, cost = self.check_stock_price(self.url)
        # print(stock, cost)
        return stock, cost
