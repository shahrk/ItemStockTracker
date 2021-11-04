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
    """
    Tests if Walmart Scraper initializes properly.
    """
    assert walmartScraper is not None
    assert InStockUrl == walmartScraper.url


def test_InStock():
    """
    Tests if the stock status value is received correctly
    for two stock status conditions (In Stock, Error Occurred)
    on www.walmart.com.
    """
    walmartScraper = WalmartScraper(InStockUrl)
    stock_info, cost = walmartScraper.job()
    assert stock_info == "In Stock" or stock_info == "Error Occurred"


def test_OutOfStock():
    """
    Tests if the stock status value is received correctly
    for two stock status conditions (Out of Stock, Error Occurred)
    on www.walmart.com.
    """
    walmartScraper = WalmartScraper(OutStockUrl)
    stock_info, cost = walmartScraper.job()
    assert stock_info == "Out of Stock" or stock_info == "Error Occurred"


# if __name__ == "__main__":
#     test_init()
#     test_InStock()
#     test_OutOfStock()
