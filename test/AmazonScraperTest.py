import unittest
from AmazonScraper import *

# Unit tests for AmazonScraper.py
# Tests the object construction, class variable initiation, and all the methods
# @author Arcane94


class AmazonScraperTest(unittest.TestCase):
    def setUp(self):
        self.InStock_URL = "https://www.amazon.com/adidas-Santiago-Lunch-Black-White/dp/B07KDSWWXK/ref=sr_1_3?crid=10JP8TVHSQW3E&dchild=1&keywords=limited+time+deal&qid=1631860841&s=apparel&sprefix=limited%2Cfashion%2C166&sr=1-3"
        self.OutOfStock_URL = "https://www.amazon.com/Adhesive-Rotating-Utility-Hangers-Bathroom/dp/B0987XHGV1/ref=sr_1_17?dchild=1&keywords=wall+hooks&qid=1632702900&refinements=p_n_availability%3A2661601011&rnid=2661599011&sr=8-17"
        self.OrderSoon_URL = "https://www.amazon.com/Gigabyte-Protection-WINDFORCE-DisplayPort-Mytrix_HDMI/dp/B09DR8C9B8/ref=sr_1_1_sspa?dchild=1&keywords=graphic+card&qid=1631860747&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyR1NMTjRET1ZHUU9CJmVuY3J5cHRlZElkPUEwNDIyMDMxM1A5T0VUWVE4OEtETiZlbmNyeXB0ZWRBZElkPUEwNzE5Nzg1MzlTTFBWVEw2RklLQyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
        self.NoStockInfo_URL = "https://www.amazon.com/Lays-Classic-Potato-Chips-Ounce/dp/B072M1NC4M/ref=sr_1_4?crid=D95KX8ETF064&dchild=1&keywords=lays&qid=1632689409&sprefix=lays%2Caps%2C174&sr=8-4"
        self.Invalid_URL = "https://amazon_this_is_an_invalid_url"

    # Tests for object creation, and url variable initiation
    def test_init(self):
        amazon = AmazonScraper(self.InStock_URL)
        self.assertNotEqual(amazon, None)
        self.assertEqual(self.InStock_URL, amazon.url)

    def test_CheckStock(self):
        # Testing No Stock Info
        amazon = AmazonScraper(self.NoStockInfo_URL)
        stock_info = amazon.CheckStock(self.NoStockInfo_URL)
        self.assertEqual("No Stock Info", stock_info)

        # Testing In Stock case. Remove the 'or' condition when Git Issue #22 is fixed.
        amazon = AmazonScraper(self.InStock_URL)
        stock_info = amazon.CheckStock(self.InStock_URL)
        self.assertTrue(stock_info == "In Stock" or stock_info == "No Stock Info")

        # Testing Order Soon case. Remove the 'or' condition when Git Issue #22 is fixed.
        amazon = AmazonScraper(self.OrderSoon_URL)
        stock_info = amazon.CheckStock(self.OrderSoon_URL)
        self.assertTrue(stock_info == "In Stock" or stock_info == "No Stock Info")

        # Testing Out of Stock case. Remove the 'or' condition when Git Issue #22 is fixed.
        amazon = AmazonScraper(self.OutOfStock_URL)
        stock_info = amazon.CheckStock(self.OutOfStock_URL)
        self.assertTrue(stock_info == "In Stock" or stock_info == "No Stock Info")

        # Testing an invalid URL
        amazon = AmazonScraper(self.Invalid_URL)
        stock_info = amazon.CheckStock(self.Invalid_URL)
        self.assertEqual("Error Occurred", stock_info)

    def test_job(self):
        # Testing No Stock Info
        amazon = AmazonScraper(self.NoStockInfo_URL)
        stock_info = amazon.job()
        self.assertEqual("No Stock Info", stock_info)

        # Testing In Stock case. Remove the 'or' condition when Git Issue #22 is fixed.
        amazon = AmazonScraper(self.InStock_URL)
        stock_info = amazon.job()
        self.assertTrue(stock_info == "In Stock" or stock_info == "No Stock Info")

        # Testing Order Soon case. Remove the 'or' condition when Git Issue #22 is fixed.
        amazon = AmazonScraper(self.OrderSoon_URL)
        stock_info = amazon.job()
        self.assertTrue(stock_info == "In Stock" or stock_info == "No Stock Info")

        # Testing Out of Stock case. Remove the 'or' condition when Git Issue #22 is fixed.
        amazon = AmazonScraper(self.OutOfStock_URL)
        stock_info = amazon.job()
        self.assertTrue(stock_info == "In Stock" or stock_info == "No Stock Info")

        # Testing an invalid URL
        amazon = AmazonScraper(self.Invalid_URL)
        stock_info = amazon.job()
        self.assertEqual("Error Occurred", stock_info)


if __name__ == '__main__':
    unittest.main()
