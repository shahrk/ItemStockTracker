"""
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from AmazonScraper import AmazonScraper
from BestBuyScraper import BestBuyScraper
from WalmartScraper import WalmartScraper


class Scraper:
    """
    Scraper chooses which scraper to run.
    'ChooseScraper' chooses the scraper.
    @author Arcane94
    """

    def ChooseScraper(self, url):
        """
        Chooses the scraper based on product url
        @param url: URL of the product
        @return: the stock status information
        """

        if "amazon" in url:
            amazonscraper = AmazonScraper(url)
            stock_info = amazonscraper.job()
            return stock_info

        if "bestbuy" in url:
            bestbuyscraper = BestBuyScraper(url)
            stock_info = bestbuyscraper.job()
            return stock_info

        if "walmart" in url:
            walmartscraper = WalmartScraper(url)
            stock_info = walmartscraper.job()
            return stock_info
