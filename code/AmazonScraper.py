import requests
from bs4 import BeautifulSoup


class AmazonScraper:
    def __init__(self, url):
        self.url = url

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

        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")  # parsing the content of the page

        try:
            sub_class = soup.find("div", {"id": "availability"})  # finding the div containing stock info
            if sub_class:
                # Handling 'order soon' and 'Out of Stock' options
                if "soon" in str(sub_class) or "Out of Stock" in str(sub_class):
                    return "Out of Stock"
                return "In Stock"
            else:
                return "No Stock Info"
        except:
            return "Error Occurred"

    def job(self):
        print("Tracking....")
        print("Processing: " + self.url)
        stock = self.CheckStock(self.url)
        print(stock)
        return stock
