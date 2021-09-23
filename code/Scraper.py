from AmazonScraper import AmazonScraper


class Scraper:
    def __init__(self, interval):
        self.TIME = interval  # How often stock info is checked.

    # Chooses which scraper to run
    def ChooseScraper(self, url):

        if "amazon" in url:
            amazonscraper = AmazonScraper()
            amazonscraper.SetURL(url)
            amazonscraper.job()

        # TODO: Add logic for other retailers
