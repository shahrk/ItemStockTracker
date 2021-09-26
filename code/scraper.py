from bs4 import BeautifulSoup as soup
import urllib.parse
import re
import time
import requests
import lxml

'''
Bestbuy scraper
'''
def get_inventory(product_page):
    product_soup = soup(product_page, 'lxml')
    buy_button = product_soup.find('div', {'class': 'fulfillment-add-to-cart-button'})
    if buy_button.find(text=re.compile('Add to Cart')) is not None \
            and buy_button.find(text=re.compile('Sold Out')) is None:
        in_stock = True
    else:
        in_stock = False
    return in_stock


def get_page(url):
    global ptime
    try:
        # control frequency
        duration = time.time() - ptime
        time.sleep(max(1 / frequency - duration, 0))
        ptime = time.time()
        # get page from request
        req = requests.get(url, headers=headers, timeout=5)
        page = req.text
        return page
    except Exception as e:
        # keep refreshing until a successful connection is established
        return get_page(url)


if __name__ == "__main__":
    url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium' \
          '-and-black/6429440.p?skuId=6429440 '
    ptime = time.time()
    frequency = 0.2
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    page = get_page(url)
    print(get_inventory(page))
