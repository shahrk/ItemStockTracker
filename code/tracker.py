FILENAME = '../data/tracker.txt'


class State:
    def __init__(self):
        self.alert = []
        self.item = []
        self.setting = ''

    def updateSetting(self, setting):
        self.setting = setting

    def updateItem(self, iturl):
        self.item.append(iturl)

    def updateAlert(self, alert):
        self.alert.append(alert)


def read_state(filename, s):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    file.close()
    iidx = lines.index('Item:')
    aidx = lines.index('Alert:')
    sidx = lines.index('Setting:')
    # proceed the item
    for i in range(iidx + 1, aidx):
        iturl = lines[i].split(',')
        s.updateItem({'item': iturl[0], 'url': iturl[1]})
    print(s.item)
    # porceed the alert
    for i in range(aidx + 1, sidx):
        alt = lines[i]
        s.updateAlert(alt)
        # proceed the setting
        s.updateSetting(lines[sidx + 1])


