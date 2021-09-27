from code import tracker
import os

# Unit tests for tracker.py
# Tests the reload_state, modify the status, save_state
# @author qchen59


s = tracker.State()
powerSupply = "Power Supply"
url = "https://www.bestbuy.com/site/corsair-rmx-series-rm850x-80-plus-gold-fully-modular-atx-power-supply-black/6459244.p?skuId=6459244"

file = open('testtracker.txt', 'w')
file.write(
    'Item:\nGeForce RTX 3070,https://www.amazon.com/Gigabyte-Protection-WINDFORCE-DisplayPort-Mytrix_HDMI/dp/B09DR8C9B8/ref=sr_1_1_sspa?dchild=1&keywords=graphic+card&qid=1631860747&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyR1NMTjRET1ZHUU9CJmVuY3J5cHRlZElkPUEwNDIyMDMxM1A5T0VUWVE4OEtETiZlbmNyeXB0ZWRBZElkPUEwNzE5Nzg1MzlTTFBWVEw2RklLQyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=\nLunch Bag,https://www.amazon.com/adidas-Santiago-Lunch-Black-White/dp/B07KDSWWXK/ref=sr_1_3?crid=10JP8TVHSQW3E&dchild=1&keywords=limited+time+deal&qid=1631860841&s=apparel&sprefix=limited%2Cfashion%2C166&sr=1-3\nRTX 3080,https://www.bestbuy.com/site/evga-rtx-3080-xc3-ultra-gaming-10g-p5-3885-kh-pci-express-4-0-lhr/6471615.p?skuId=6471615\nPower Supply,https://www.bestbuy.com/site/corsair-rmx-series-rm850x-80-plus-gold-fully-modular-atx-power-supply-black/6459244.p?skuId=6459244\nAlert:\nEmail,test@email.com\nSetting:\n5')
file.close()
full_path = os.path.abspath('testtracker.txt')


def test_readState():
    tracker.read_state(full_path, s)
    assert len(s.item) == 4, "Should be 4 items"
    assert s.email == 'test@email.com', "Should be test@email.com"
    assert len(s.alert) == 1, "Should be only 1 alert"
    assert s.alert[0] == 'Email', "The alert should be email"
    assert s.setting == '5', "The setting interval should be 5"


def test_updateStatus():
    tracker.read_state(full_path, s)
    s.updateStatus(powerSupply, url, 'In Stock')
    assert s.getStatus(powerSupply, url).get('status') == 'In Stock', "Should be In Stock"


def test_deleteAlert():
    tracker.read_state(full_path, s)
    s.deleteAlert('Email')
    s.deleteEmail()
    assert len(s.alert) == 0, "Should be no alert"
    assert s.email == '', "Should be empty"


def test_saveState():
    tracker.save_state(full_path, s)

# if __name__ == "__main__":
#     test_readState()
#     test_updateStatus()
#     test_deleteAlert()
#     test_saveState()
