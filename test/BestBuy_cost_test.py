from code.BestBuyScraper import BestBuyScraper
import re

# Unit tests for BestBuyScraper.py
# Tests the cost functionality
# @author rhnprabhune

InStockUrl = "https://www.bestbuy.com/site/dell-s2721dgf-27-gaming-ips-qhd-freesync-and-g-sync-compatible-monitor-with-hdr-displayport-hdmi/6421624.p?skuId=6421624"
OutOfStockUrl = (
    "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
)
bestBuyScraper = BestBuyScraper(InStockUrl)


def test_InStock_cost():
    bestBuyScraper = BestBuyScraper(InStockUrl)
    stock_info, cost = bestBuyScraper.job()
    cost_check = bool(re.search("^\$\d{0,3}(,\d{3})*\.\d{0,2}", cost))
    assert cost_check


def test_OutOfStock_cost():
    bestBuyScraper = BestBuyScraper(OutOfStockUrl)
    stock_info, cost = bestBuyScraper.job()
    assert cost == "NA"
