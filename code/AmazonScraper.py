import requests
from bs4 import BeautifulSoup

# Scraper for Amazon
# Takes in product url as input upon object creation
# 'job' prints progress while 'CheckStock' obtains stock info
# @author Arcane94


class AmazonScraper:
    def __init__(self, url):
        self.url = url

    # Obtains stock information from the given url
    # @param url URL of the product
    def CheckStock(self, url):
        headers = {
            'authority': 'www.amazon.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
        try:
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.text, "html.parser")  # parsing the content of the page
        # Handles invalid URLs/timeouts
        except:
            return "Error Occurred"

        try:
            sub_class_stock = soup.find("div", {"id": "availability"})  # finding the div containing stock info
            sub_class_no_stock = soup.find("div", {"id": "outOfStock"})  # finding the div containing out of stock info
            if sub_class_stock and not sub_class_no_stock:
                if "order soon" in str(sub_class_stock):
                    return "In Stock"
                elif "In stock soon" in str(sub_class_stock):
                    return "Out of Stock"
                return "In Stock"
            elif sub_class_no_stock:
                return "Out of Stock"
            # This handles the case of having no stock info
            else:
                return "No Stock Info"
        except:
            return "Error Occurred"

    # Prints the progress, and delegates the task to 'CheckStock'
    def job(self):
        print("Tracking....")
        print("Processing: " + self.url)
        stock = self.CheckStock(self.url)
        print(stock)
        return stock
