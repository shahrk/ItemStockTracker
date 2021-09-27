from code.BestBuyScraper import BestBuyScraper


InStockUrl = 'https://www.bestbuy.com/site/dell-s2721dgf-27-gaming-ips-qhd-freesync-and-g-sync-compatible-monitor-with-hdr-displayport-hdmi/6421624.p?skuId=6421624'
OutOfStockUrl = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'


def test_InStock():
    BBScraper = BestBuyScraper(InStockUrl)
    assert BBScraper.job() == 'In Stock', "Should be In Stock"


def test_OutOfStock():
    BBScraper = BestBuyScraper(OutOfStockUrl)
    assert BBScraper.job() == 'No Stock Info', "Should be No Stock Info"

# if __name__ == "__main__":
#     test_InStock()
#     test_OutOfStock()