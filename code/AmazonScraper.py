import requests
from time import sleep
import time
import schedule
from bs4 import BeautifulSoup


class AmazonScraper:

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
        sleep(3)

        soup = BeautifulSoup(page.text, "html.parser")  # parsing the content of the page

        try:
            sub_class = soup.find("div", {"id": "availability"})  # finding the div containing stock info
            if sub_class:
                return "availability : {}".format(sub_class.find("span", {"class": "a-size-medium a-color-success"}).text.strip())
            else:
                return "Stock information is not available"
        except:
            return "An error occurred. Please make sure the link you entered is correct"




    def ReadURL(self):

        url = "https://www.amazon.com/Lays-Potato-Chips-Classic-Party/dp/B07ZD56WL3/ref=sr_1_4_0o_fs?dchild=1&keywords=lays&qid=1632007752&sr=8-4"
        print("Processing: "+url)

        ans = self.CheckStock(url)
        print(ans)


    def job(self):
        print("Tracking....")
        self.ReadURL()


# amazonScraper = AmazonScraper()
# schedule.every(5).seconds.do(amazonScraper.job)
#
# while True:
#     # running all pending jobs
#     schedule.run_pending()
#     time.sleep(1)
