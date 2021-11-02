class WalmartScraper:
    """
    This is the Scraper for Walmart. Takes in product url as input upon object creation.
    Method 'job' prints progress while method 'check_stock' obtains stock info.

    Walmart pages can have stock info in different ways. Following are the possible cases,
    interpretations, and return values of each case.

        * "In Stock" - Product is in stock - return "In Stock"
        * "Only x left Order soon" - Product is in stock - return "In Stock"
        * "Currently unavailable" - product is out of Stock - return "Out of Stock"
        * "In stock soon" - Product is out of stock - return "Out of Stock"
        * No stock information on the page/Captcha page - No stock info - return "No Stock Info"

    @author: gavinilakshmiswetha
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
