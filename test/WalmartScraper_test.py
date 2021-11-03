from code.WalmartScraper import WalmartScraper
import re

# Unit tests for WalmartScraper.py
# Tests the object construction, In stock and out stock cases
# @author gavinilakshmiswetha

InStockUrl = "https://www.walmart.com/ip/KingSo-Bedside-Table-Nightstand-Tall-Wood-Accent-End-Tables-for-Bedroom-Living-Room-Brown/258766761"
OutStockUrl = "https://www.walmart.com/ip/Maybelline-SuperStay-24hr-2-Step-Lipcolor-Always-Blazing/126088124"
walmartScraper = WalmartScraper(InStockUrl)

# Tests for object creation, and url variable initiation


def test_init():
    assert walmartScraper is not None
    assert InStockUrl == walmartScraper.url


def test_InStock():
    walmartScraper = WalmartScraper(InStockUrl)
    stock_info, cost = walmartScraper.job()
    assert stock_info == "In Stock", "Should be In Stock"


def test_InStock_cost():
    walmartScraper = WalmartScraper(InStockUrl)
    stock_info, cost = walmartScraper.job()
    cost_check = bool(re.search("^\$\d{0,3}(,\d{3})*\.\d{0,2}", cost))
    assert cost_check or cost == "NA"


def test_OutOfStock():
    walmartScraper = WalmartScraper(OutStockUrl)
    stock_info, cost = walmartScraper.job()
    assert stock_info == "Out of Stock", "Should be Out of Stock"


def test_OutOfStock_cost():
    walmartScraper = WalmartScraper(OutStockUrl)
    stock_info, cost = walmartScraper.job()
    assert cost == "NA"

# if __name__ == "__main__":
#     test_init()
#     test_InStock()
#     test_OutOfStock()
