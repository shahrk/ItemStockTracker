from AmazonScraper import AmazonScraper
from BestBuyScraper import BestbuyScraper

# Scraper chooses which scraper to run
# 'ChooseScraper' chooses the scraper
# @author Arcane94


class Scraper:

    # Chooses the scraper based on product url
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
