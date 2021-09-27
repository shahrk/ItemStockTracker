from code import tracker

s = tracker.State()
powerSupply = "Power Supply"
url = "https://www.bestbuy.com/site/corsair-rmx-series-rm850x-80-plus-gold-fully-modular-atx-power-supply-black/6459244.p?skuId=6459244"


def test_readState():
    tracker.read_state('../data/testtracker.txt', s)
    assert len(s.item) == 4, "Should be 4 items"
    assert s.email == 'test@email.com', "Should be test@email.com"
    assert len(s.alert) == 1, "Should be only 1 alert"
    assert s.alert[0] == 'Email', "The alert should be email"
    assert s.setting == '5', "The setting interval should be 5"


def test_updateStatus():
    s.updateStatus(powerSupply, url, 'In Stock')
    assert s.getStatus(powerSupply, url).get('status') == 'In Stock', "Should be In Stock"


def test_deleteAlert():
    s.deleteAlert('Email')
    s.deleteEmail()
    assert len(s.alert) == 0, "Should be no alert"
    assert s.email == '', "Should be empty"


def test_saveState():
    tracker.save_state('../data/testsave.txt', s)

# if __name__ == "__main__":
#     test_readState()
#     test_updateStatus()
#     test_deleteAlert()
#     test_saveState()
