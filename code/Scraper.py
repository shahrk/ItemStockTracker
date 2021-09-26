from AmazonScraper import AmazonScraper
from BestBuyScraper import BestbuyScraper


class Scraper:

    # Chooses which scraper to run
    # @param url URL of the product
    def ChooseScraper(self, url):

        if "amazon" in url:
            amazonscraper = AmazonScraper(url)
            stock_info = amazonscraper.job()
            return stock_info

        if "bestbuy" in url:
            bestbuyscraper = BestbuyScraper(url)
            stock_info = bestbuyscraper.job()
            return stock_info
