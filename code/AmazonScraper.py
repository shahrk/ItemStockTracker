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


class AmazonScraper:
    """
    This is the Scraper for Amazon. Takes in product url as input upon object creation.
    Method 'job' prints progress while method 'check_stock' obtains stock info and a string indicating cost of the product.

    Amazon pages can have stock info in different ways. Following are the possible cases,
    interpretations, and return values of each case.

        * "In Stock" - Product is in stock - return "In Stock"
        * "Only x left Order soon" - Product is in stock - return "In Stock"
        * "Currently unavailable" - product is out of Stock - return "Out of Stock"
        * "In stock soon" - Product is out of stock - return "Out of Stock"
        * No stock information on the page/Captcha page - No stock info - return "No Stock Info"

    @author: Arcane94
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
            "authority": "www.amazon.com",
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "dnt": "1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 "
            "(HTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,"
            "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-dest": "document",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        }
        try:
            page = requests.get(url, headers=headers)
            # parsing the content of the page
            soup = BeautifulSoup(page.text, "html.parser")
        # Handles invalid URLs/timeouts
        except:
            return "Error Occurred", "NA"

        try:
            # finding the div containing stock info
            sub_class_stock = soup.find("div", {"id": "availability"})
            # finding the div containing out of stock info
            sub_class_no_stock = soup.find("div", {"id": "outOfStock"})
            cost = soup.find_all('span', {'class' : 'a-price'})[0].contents[0].contents[0]
            # price = re.match("\$(\d*,)*\d*\.\d*", cost)
            # cost = cost.contents[0]
            # print(cost)

            if sub_class_stock and not sub_class_no_stock:
                if "success" in str(sub_class_stock) or "order soon" in str(sub_class_stock):
                    return "In Stock", cost
                return "Out of Stock", "NA"
            elif sub_class_no_stock:
                return "Out of Stock", "NA"
            # This handles the case of having no stock info on the page/captcha page
            else:
                return "No Stock Info", "NA"
        except:
            return "Error Occurred", "NA"

    def job(self):
        """
        Prints the progress, and delegates the task to 'check_stock'.

        :return: a string indicating the stock information and a string indicating cost of the product
        """
        # print("Tracking....")
        # print("Processing: " + self.url)
        stock, cost = self.check_stock_price(self.url)
        # print(stock, cost)
        return stock, cost
