import sys

sys.path.insert(0, "./code/")
from code.Scraper import Scraper


# Unit tests for Scraper.py
# Testing object creation, and the method
# @author Arcane94


amazon_URL = "https://www.amazon.com/Lays-Classic-Potato-Chips-Ounce/dp/B072M1NC4M/ref=sr_1_4?crid=D95KX8ETF064&dchild=1&keywords=lays&qid=1632689409&sprefix=lays%2Caps%2C174&sr=8-4"
bestBuy_URL = "https://www.bestbuy.com/site/corsair-rmx-series-rm850x-80-plus-gold-fully-modular-atx-power-supply-black/6459244.p?skuId=6459244"


# Testing object creation
def test_init():
    scraper = Scraper()
    assert scraper is not None


def test_ChooseScraper():
    # Testing Amazon case
    scraper = Scraper()
    stock_info, cost = scraper.ChooseScraper(amazon_URL)
    assert stock_info == "Error Occurred" or stock_info == "In Stock"

    # Testing BestBuy case
    scraper = Scraper()
    stock_info, cost = scraper.ChooseScraper(bestBuy_URL)
    assert stock_info == "In Stock"


# if __name__ == '__main__':
#     test_init()
#     test_ChooseScraper()
