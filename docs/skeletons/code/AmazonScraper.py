class AmazonScraper:
    """
    | This is the Scraper for Amazon. Takes in product url as input upon object creation. Method 'job' prints progress while method 'check_stock' obtains stock info.

    | Amazon pages can have stock info in different ways. Following are the possible cases, interpretations, and return values of each case.

     .. list-table::
        :header-rows: 1

        * - Case
          - Interpretation
          - Scraper return value
        * - In Stock
          - Product is in stock
          - In Stock
        * - Only x left Order soon
          - Product is in stock
          - In Stock
        * - Currently unavailable
          - Product is out of stock
          - Out of Stock
        * - In stock soon
          - Product is out of stock
          - Out of Stock
        * - No stock info or captcha page
          - Stock information not available
          - No Stock Info

    |
    """

    def __init__(self, url):
        """
        Initializes url upon object construction.

        :param url: URL of the product
        """
        self.url = url

    def check_stock(self, url):
        """
        Obtains stock information from the given url.

        :param url: URL of the product
        :return: a string indicating the stock information
        """

    def job(self):
        """
        Prints the progress, and delegates the task to 'check_stock'.

        :return: a string indicating the stock information
        """
