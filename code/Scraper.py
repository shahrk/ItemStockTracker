import schedule
import time
from AmazonScraper import AmazonScraper


class Scraper:
    def __init__(self):
        self.TIME = 5  # How often stock info is checked.

    # Chooses which scraper to run
    def ChooseScraper(self, url):

        if "amazon" in url:
            amazonscraper = AmazonScraper()
            amazonscraper.SetURL(url)
            schedule.every(self.TIME).seconds.do(amazonscraper.job)
            while True:
                # running all pending jobs
                schedule.run_pending()
                time.sleep(1)

        # TODO: Add logic for other retailers
