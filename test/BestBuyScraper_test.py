from code.BestBuyScraper import BestBuyScraper
import re

# Unit tests for BestBuyScraper.py
# Tests the object construction, In stock and out stock cases
# @author qchen59

InStockUrl = "https://www.bestbuy.com/site/dell-s2721dgf-27-gaming-ips-qhd-freesync-and-g-sync-compatible-monitor-with-hdr-displayport-hdmi/6421624.p?skuId=6421624"
OutOfStockUrl = (
    "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
)
bestBuyScraper = BestBuyScraper(InStockUrl)


# Tests for object creation, and url variable initiation
def test_init():
    """
    Tests if Bestbuy Scraper initializes properly.
    """
    assert bestBuyScraper is not None
    assert InStockUrl == bestBuyScraper.url


def test_InStock():
    """
    Tests if the stock status value is received correctly
    for two stock status conditions (In Stock, Should be In Stock)
    on www.bestbuy.com.
    """
    bestBuyScraper = BestBuyScraper(InStockUrl)
    stock_info, cost = bestBuyScraper.job()
    assert stock_info == "In Stock", "Should be In Stock"


def test_OutOfStock():
    """
    Tests if the stock status value is received correctly
    for two stock status conditions (Out of Stock, Should be Out of Stock)
    on www.bestbuy.com.
    """
    bestBuyScraper = BestBuyScraper(OutOfStockUrl)
    stock_info, cost = bestBuyScraper.job()
    assert stock_info == "Out of Stock", "Should be Out of Stock"

# if __name__ == "__main__":
#     test_init()
#     test_InStock()
#     test_OutOfStock()
