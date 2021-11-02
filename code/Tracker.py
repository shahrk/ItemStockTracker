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
import os.path

"""
The Tracker serves as the backend of our program.
Supports the save and reload of state, modify to the item list and settings.
# @author: qchen59
"""


FILENAME = '../data/tracker.txt'


class State:
    """
    The State class which holds all state data.
    Such as the alert setting and the item list.
    """

    def __init__(self):
        self.alert = []
        self.item = []
        self.setting = ''
        self.email = ''

    def updateSetting(self, setting):
        """
        Update the setting with given setting
        @param setting: the given setting
        """
        self.setting = setting

    def updateItem(self, iturl):
        """
        Update the item list with given item dict
        @param iturl: the given item dict,contains the item name, url, status and previous status
        """
        self.item.append(iturl)

    def updateAlert(self, alert):
        """
        Update the alert with given alert, add the new alert to the alert list
        @param alert: given alert
        """
        self.alert.append(alert)

    def updateEmail(self, email):
        """
        Update the email with given email
        @param email: the given email
        """
        self.email = email

    def deleteAlert(self, alert):
        """
        Delete an alert
        @param alert: given the alert name which we want to delete
        @return:
        """
        self.alert.remove(alert)

    def deleteEmail(self):
        """
        Clear the email address
        """
        self.email = ''

    def updateStatus(self, item, url, status, cost):
        """
        Update the item status
        @param item: given item name
        @param url: given item url
        @param status: new item status
        @param cost: given item cost
        """
        for it in self.item:
            if it.get('item') == item and it.get('url') == url:
                it['pstatus'] = it['status']
                it['status'] = status
                it['cost'] = cost

    def getStatus(self, item, url):
        """
        Get the item status for specific item
        @param item: given item name
        @param url: given item url
        @return: the item status for given item
        """
        for it in self.item:
            if it.get('item') == item and it.get('url') == url:
                return {'status': it.get('status'), 'pstatus': it.get('pstatus'), 'cost': it.get('cost')}


def read_state(filename, s):
    """
    Read in a state from file
    @param filename: given filename we want to read in
    @param s: is the sate we want add state data to
    """
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
            s.updateItem(
                {'item': iturl[0], 'url': iturl[1], 'status': '', 'pstatus': ''})
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


def save_state(filename, s):
    """
    Save the state to the file
    @param filename: the filename we want to save the state to
    @param s: is the state instance which stores the state data
    """
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
