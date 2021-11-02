from code.BestBuyScraper import BestBuyScraper

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
    assert bestBuyScraper is not None
    assert InStockUrl == bestBuyScraper.url


def test_InStock():
    bestBuyScraper = BestBuyScraper(InStockUrl)
    assert bestBuyScraper.job() == "In Stock", "Should be In Stock"


def test_OutOfStock():
    bestBuyScraper = BestBuyScraper(OutOfStockUrl)
    assert bestBuyScraper.job() == "Out of Stock", "Should be Out of Stock"


# if __name__ == "__main__":
#     test_init()
#     test_InStock()
#     test_OutOfStock()
