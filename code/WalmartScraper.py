
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
    Method 'job' prints progress while method 'check_stock' obtains stock info.

    Walmart pages can have stock info in different ways. Following are the possible cases,
    interpretations, and return values of each case.

        * "In Stock" - Product is in stock - return "In Stock"
        * "Only x left Order soon" - Product is in stock - return "In Stock"
        * "Currently unavailable" - product is out of Stock - return "Out of Stock"
        * "In stock soon" - Product is out of stock - return "Out of Stock"
        * No stock information on the page/Captcha page - No stock info - return "No Stock Info"

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
        # parsing the content of the page
        soup = BeautifulSoup(page.text, 'lxml')
        try:
            button_add = soup.find('button', {'class': 'w_BS w_BU w_BZ'})

            cost = soup.find(
                "span", {"itemprop": "price"})
            cost = cost.contents[0]
            # print(cost)
            if button_add:
                return "In Stock", cost
            else:
                return "Out of Stock", "NA"
        except:
            return "Error Occurred", "NA"

    def job(self):
        """
        Prints the progress, and delegates the task to 'check_stock'.

        :return: a string indicating the stock information
        """
        print("Tracking....")
        print("Processing: " + self.url)
        stock, cost = self.check_stock_price(self.url)
        print(stock, cost)
        return stock, cost


# The lines below are just for testing purpose
# url = 'https://www.walmart.com/ip/KingSo-Bedside-Table-Nightstand-Tall-Wood-Accent-End-Tables-for-Bedroom-Living-Room-Brown/258766761'
# walmart_obj = WalmartScraper(url)
# stock_info = walmart_obj.job()
