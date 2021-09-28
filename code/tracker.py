import os.path

# save state, reload state and other related functions
# @author qchen59

FILENAME = '../data/tracker.txt'


class State:
    def __init__(self):
        self.alert = []
        self.item = []
        self.setting = ''
        self.email = ''

    # Update the setting with given setting
    # param setting given setting
    def updateSetting(self, setting):
        self.setting = setting

    # Update the item list with given item dict
    # param iturl given item dict
    def updateItem(self, iturl):
        self.item.append(iturl)

    # Update the alert with given alert
    # param alert given alert
    def updateAlert(self, alert):
        self.alert.append(alert)

    # Update the email with given email
    # param email given email address
    def updateEmail(self, email):
        self.email = email

    # Delete an alert
    # param alert the alert which we want to delete
    def deleteAlert(self, alert):
        self.alert.remove(alert)

    # Clear the email address
    def deleteEmail(self):
        self.email = ''

    # Update the item status
    # param item is the given item
    # param url is the item's url
    # param status is the item new status
    def updateStatus(self, item, url, status):
        for it in self.item:
            if it.get('item') == item and it.get('url') == url:
                it['pstatus'] = it['status']
                it['status'] = status

    # Get the item status
    # param item is the given item
    # param url is the item's url
    def getStatus(self, item, url):
        for it in self.item:
            if it.get('item') == item and it.get('url') == url:
                return {'status': it.get('status'), 'pstatus': it.get('pstatus')}


# Read in a state from file
# param filename is the filename
# param s is the state
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
            s.updateItem({'item': iturl[0], 'url': iturl[1], 'status': '', 'pstatus': ''})
        # proceed the alert
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


# Save the state to the file
# param filename is the filename
# param s is the state
def save_state(filename, s):
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
