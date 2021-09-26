from AmazonScraper import AmazonScraper


class Scraper:
    def __init__(self, interval):
        self.TIME = interval  # How often stock info is checked.

    # Chooses which scraper to run
    def ChooseScraper(self, url):

        if "amazon" in url:
            amazonscraper = AmazonScraper(url)
            stock_info = amazonscraper.job()
            return stock_info

        # TODO: Add logic for other retailers
