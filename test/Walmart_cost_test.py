from code.WalmartScraper import WalmartScraper
import re

# Unit tests for WalmartScraper.py
# Tests the object construction, cost returned
# @author rhnprabhune

InStockUrl = "https://www.walmart.com/ip/KingSo-Bedside-Table-Nightstand-Tall-Wood-Accent-End-Tables-for-Bedroom-Living-Room-Brown/258766761"
OutStockUrl = "https://www.walmart.com/ip/Maybelline-SuperStay-24hr-2-Step-Lipcolor-Always-Blazing/126088124"
walmartScraper = WalmartScraper(InStockUrl)

# Tests for object creation, and url variable initiation


def test_InStock_cost():
    """
    Tests if cost value is received correctly
    when condition is In Stock on www.beswalmarttbuy.com.
    """
    walmartScraper = WalmartScraper(InStockUrl)
    stock_info, cost = walmartScraper.job()
    cost_check = bool(re.search("^\$\d{0,3}(,\d{3})*\.\d{0,2}", cost))
    assert cost_check


def test_OutOfStock_cost():
    """
    Tests if cost value is received correctly
    when condition is Out of Stock on www.walmart.com.
    """
    walmartScraper = WalmartScraper(OutStockUrl)
    stock_info, cost = walmartScraper.job()
    assert cost == "NA"


# if __name__ == "__main__":
#     test_init()
#     test_InStock()
#     test_OutOfStock()
