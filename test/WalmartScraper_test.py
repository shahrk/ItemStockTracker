from code.WalmartScraper import WalmartScraper

# Unit tests for WalmartScraper.py
# Tests the object construction, In stock and out stock cases
# @author gavinilakshmiswetha

InStockUrl = 'https://www.walmart.com/ip/KingSo-Bedside-Table-Nightstand-Tall-Wood-Accent-End-Tables-for-Bedroom-Living-Room-Brown/258766761'
OutStockUrl = 'https://www.walmart.com/ip/Maybelline-SuperStay-24hr-2-Step-Lipcolor-Always-Blazing/126088124'
walmartScraper = WalmartScraper(InStockUrl)

# Tests for object creation, and url variable initiation
def test_init():
    assert walmartScraper is not None
    assert InStockUrl == walmartScraper.url

def test_InStock():
    walmartScraper = WalmartScraper(InStockUrl)
    assert walmartScraper.job() == 'In Stock', "Should be In Stock"

def test_OutOfStock():
    walmartScraper = WalmartScraper(OutStockUrl)
    assert walmartScraper.job() == 'Out of Stock', "Should be Out of Stock"

# if __name__ == "__main__":
#     test_init()
#     test_InStock()
#     test_OutOfStock()
