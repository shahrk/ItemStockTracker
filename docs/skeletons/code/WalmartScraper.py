class WalmartScraper:
    """
 | This is the Scraper for Walmart. Takes in product url as input upon object creation. Method 'job' prints progress while method 'check_stock' obtains stock info and a string indicating cost of the product.

 | Walmart pages can have stock info in different ways. Following are the possible cases, interpretations, and return values of each case.

  .. list-table::
     :header-rows: 1

     * - Case
       - Interpretation
       - Scraper return value
     * - Add to Cart
       - Product is in stock
       - In Stock
     * - Out of Stock
       - Product is out of stock
       - Out of Stock
 |
 """

    def __init__(self, url):
        """
        Initializes url upon object construction.
        :param url: URL of the product
        """

    def check_stock_price(self, url):
        """
        Obtains stock information from the given url.

        :param url: URL of the product
        :return: a string indicating the stock information and a string indicating cost of the product
        """

    def job(self):
        """
        Prints the progress, and delegates the task to 'check_stock'.

        :return: a string indicating the stock information and a string indicating cost of the product
        """
