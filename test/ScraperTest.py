import unittest
from Scraper import Scraper

class ScraperTest(unittest.TestCase):
    def setUp(self):
        self.amazon_URL = "https://www.amazon.com/Lays-Classic-Potato-Chips-Ounce/dp/B072M1NC4M/ref=sr_1_4?crid=D95KX8ETF064&dchild=1&keywords=lays&qid=1632689409&sprefix=lays%2Caps%2C174&sr=8-4"
        self.bestBuy_URL = "https://www.bestbuy.com/site/corsair-rmx-series-rm850x-80-plus-gold-fully-modular-atx-power-supply-black/6459244.p?skuId=6459244"

    def test_ChooseScraper(self):
        # Testing Amazon case
        scraper = Scraper()
        stock_info = scraper.ChooseScraper(self.amazon_URL)
        self.assertEqual("No Stock Info", stock_info)

        # Testing BestBuy case
        scraper = Scraper()
        stock_info = scraper.ChooseScraper(self.bestBuy_URL)
        self.assertEqual("In Stock", stock_info)


if __name__ == '__main__':
    unittest.main()
