class State:
    """
    | The State class that holds all state data. Holds alert settings and the item list.
    |    
    """    

    def updateSetting(self, setting):
        """
        Update the setting with given setting.
        
        :param setting: the given setting
        """
        

    def updateItem(self, iturl):
        """
        Update the item list with given item dict.
        
        :param iturl: the given item dict,contains the item name, url, status and previous status
        """
        

    def updateAlert(self, alert):
        """
        Update the alert with given alert, add the new aler to the alert list.
        
        :param alert: given alert
        """
        

    def updateEmail(self, email):
        """
        Update the email with given email.
        
        :param email: the given email
        """
        

    def deleteAlert(self, alert):
        """
        Delete an alert.
        
        :param alert: given the alert name which we want to delete
        :return:
        """
        

    def deleteEmail(self):
        """
        Clear the email address.
        """
        

    def updateStatus(self, item, url, status):
        """
        Update the item status.
        
        :param item: given item name
        :param url: given item url
        :param status: new item status
        """
        
    def getStatus(self, item, url):
        """
        Get the item status for specific item.
        
        :param item: given item name
        :param url: given item url
        :return: the item status for given item
        """        

    def read_state(filename, s):
        """
        Read in a state from file.
	
        :param filename: given filename we want to read in
        :param s: is the sate we want add state data to
        """	

    def save_state(filename, s):
        """
        Save the state to the file.

        @param filename: the filename we want to save the state to
        @param s: is the state instance which stores the state data
        """
    
