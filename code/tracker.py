import os.path
FILENAME = '../data/tracker.txt'


class State:
    def __init__(self):
        self.alert = []
        self.item = []
        self.setting = ''
        self.email = ''

    def updateSetting(self, setting):
        self.setting = setting

    def updateItem(self, iturl):
        self.item.append(iturl)

    def updateAlert(self, alert):
        self.alert.append(alert)

    def updateEmail(self,email):
        self.email = email

    def deleteAlert(self,alert):
        self.alert.remove(alert)

    def deleteEmail(self):
        email = ''


def read_state(filename, s):
    if os.path.exists(filename):
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
        # porceed the alert
        for i in range(aidx + 1, sidx):
            alt = lines[i]
            if 'Email' in alt:
                em = alt.split(',')
                s.updateAlert(em[0])
                s.updateEmail(em[1])
            else:
                s.updateAlert(alt)
            # proceed the setting
        s.updateSetting(lines[sidx + 1])


def save_state(filename,s):
    # write the current state to the file
    with open(filename, 'w') as file:
        file.writelines('Item:\n')
        for i in s.item:
            file.write(i.get('item'))
            file.write(',')
            file.write(i.get('url'))
            file.write('\n')
        file.writelines('Alert:\n')
        for a in s.alert:
            file.write(a)
            if a == 'Email':
                file.write(',')
                file.write(s.email)
            file.write('\n')
        file.writelines('Setting:\n')
        file.write(s.setting)
    file.close()
