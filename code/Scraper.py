import schedule
import time
from AmazonScraper import AmazonScraper


class Scraper:

    def ChooseScraper(self, url):

        if url.contains("amazon"):
            amazonscraper = AmazonScraper()
            schedule.every(5).seconds.do(amazonscraper.job)

        # TODO: Add logic for other retailers

while True:
    # running all pending jobs
    schedule.run_pending()
    time.sleep(1)