from code.AmazonScraper import AmazonScraper
import re

# Unit tests for AmazonScraper.py
# Tests cost funcitonality
# @author rhnprabhune

InStock_URL = "https://www.amazon.com/adidas-Santiago-Lunch-Black-White/dp/B07KDSWWXK/ref=sr_1_3?crid=10JP8TVHSQW3E&dchild=1&keywords=limited+time+deal&qid=1631860841&s=apparel&sprefix=limited%2Cfashion%2C166&sr=1-3"
OutOfStock_URL = "https://www.amazon.com/Adhesive-Rotating-Utility-Hangers-Bathroom/dp/B0987XHGV1/ref=sr_1_17?dchild=1&keywords=wall+hooks&qid=1632702900&refinements=p_n_availability%3A2661601011&rnid=2661599011&sr=8-17"
OrderSoon_URL = "https://www.amazon.com/Gigabyte-Protection-WINDFORCE-DisplayPort-Mytrix_HDMI/dp/B09DR8C9B8/ref=sr_1_1_sspa?dchild=1&keywords=graphic+card&qid=1631860747&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyR1NMTjRET1ZHUU9CJmVuY3J5cHRlZElkPUEwNDIyMDMxM1A5T0VUWVE4OEtETiZlbmNyeXB0ZWRBZElkPUEwNzE5Nzg1MzlTTFBWVEw2RklLQyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
InStockSoon_URL = "https://www.amazon.com/Ruffles-Potato-Chips-Variety-Count/dp/B07DQ9852M/ref=sr_1_33?dchild=1&keywords=potato+chips&qid=1632760193&refinements=p_n_availability%3A2661601011&rnid=2661599011&sr=8-33"
Invalid_URL = "https://amazon_this_is_an_invalid_url"
amazon = AmazonScraper(InStock_URL)


def test_check_cost():
    """
    Tests if the cost value is received correctly for each of the 5 stock
    status conditions (In Stock, Order Soon, Out of Stock, In Stock Soon,
    Invalid URL) on www.amazon.com.
    """
    # Testing In Stock case. Remove the 'or' condition when Git Issue #22 is fixed.
    amazon = AmazonScraper(InStock_URL)
    stock_info, cost = amazon.check_stock_price(InStock_URL)
    cost_check = bool(re.search("^\$\d{0,3}(,\d{3})*\.\d{0,2}", cost))
    assert cost_check or cost == "NA"

    # Testing Order Soon case. Remove the 'or' condition when Git Issue #22 is fixed.
    amazon = AmazonScraper(OrderSoon_URL)
    stock_info, cost = amazon.check_stock_price(OrderSoon_URL)
    cost_check = bool(re.search("^\$\d{0,3}(,\d{3})*\.\d{0,2}", cost))
    assert cost_check or cost == "NA"

    # Testing Out of Stock(currently unavailable) case. Remove the 'or' condition when Git Issue #22 is fixed.
    amazon = AmazonScraper(OutOfStock_URL)
    stock_info, cost = amazon.check_stock_price(OutOfStock_URL)
    assert cost == "NA"

    # Testing In Stock Soon case. Remove the 'or' condition when Git Issue #22 is fixed.
    amazon = AmazonScraper(InStockSoon_URL)
    stock_info, cost = amazon.check_stock_price(InStockSoon_URL)
    assert cost == "NA"

    # Testing an invalid URL
    amazon = AmazonScraper(Invalid_URL)
    stock_info = amazon.check_stock_price(Invalid_URL)
    assert cost == "NA"
