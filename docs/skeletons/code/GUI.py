class Application:
    """
    | The main application class for the project.
    |
    """

    def reload_state(self):
        """
        Populates the listbox with saved values.
        """

    def save_setting(self):
        """
        Saves the updated setting. Checks email alert.
        """

    def scraper_data(self):
        """
        Obtains stock info from appropriate scrapers.
        Threads run this method.
        """

    def update_stock_info(self, entry, item_name, item_url, item_stock):
        """
        Updates the items in the GUI with the stock information.

        :param entry: one of the items in the products list
        :param item_name: name of the product
        :param item_url: url of the product
        :param item_stock: stock info of the product
        """

    def run_timer(self):
        """
        After this function is called for the first time, it will be called again
        every second until the application is closed.
        Delegates GUI updating to 'update_stock_info' and send an alert when the item restocks.
        """

    def __verify_numeric(self, action, value):
        """
        This function is used in an entry object, to verify that the input is a number.
        To use it, specify this function as the "validatecommand" option when creating a
        tkinter entry object.

        :param action: Whether data is being inserted or deleted from the entry object, represented as an int
        :param value: The current text of the entry object
        """


class TrackedItemsListbox:
    """
    This object is for holding and displaying the list of items that are being tracked by the program.
    It is built off of the ttk.Treeview class, and contains 3 columns (Name, URL, Stock Status).
    """

    def menu_popup(self, event):
        """
        This function causes a menu with a list of commands to appear. It is intended to be used when the user right
        clicks on the item list.
        """

    def add_item(self, name, url):
        """
        Adds an item to the list to be tracked.

        :param name: name of the item to be added
        :param url: URL of the product page
        """

    def delete_item(self):
        """
        Deletes the currently selected item.
        """

    def edit_item(self):
        """
        Edits the currently selected item. To do this, it creates a popup to gather the new item information.
        """

    def add_item_popup(self):
        """
        Adds a new item to the list. It launches a popup to gather the name and url for the item from the user.
        """

    def alert(self, name, url):
        """
        Alerts the user that a particular product is back in stock by launching a popup and, if the email setting is
        active, sending an email.

        :param name: name of the item to be added
        :param url: URL of the product page
        """


class GetItemURLDialogue:
    """
    This is a popup for getting the name and url for a product.
    It is build off of the tkinter.simpledialog.Dialog class.
    Information can be retrieved by checking the name and url attributes after the popup has been closed.

    :param parent: the parent object for the popup
    :param title: the title of the new window
    :param name: the default name of the item
    :param url: the default url of the item
    """

    def body(self, frame):
        """
        This function is called automatically by the object. It controls what objects should be contained in the popup
        frame.

        :param frame:
        :return: the modified frame
        """

    def apply(self):
        """
        This function controls what values are applied to the object after the popup closes.
        """


class ItemAlertDialogue:
    """
    This class defines the popup that is used to alert a user of a restock.

    :param parent: the parent object for the popup
    :param title: the title of the new window
    :param name: the name of the item
    :param url: the url of the item
    """

    def followlink(self, event):
        """
        Opens the url displayed in the popup in a web browser.

        :param event: The popup event
        """
        webbrowser.open(self.url)

    def body(self, frame):
        """
        This function is called automatically by the object. It controls what objects should be contained in the popup
        frame.

        :param frame:
        :return: the modified frame
        """

    def buttonbox(self):
        """
        This function is called automatically by the object. It controls what buttons should be contained in the popup.
        """


def quit_window(icon, item):
    """
    When clicked on quit from system tray closes the application
    """

def show_window(icon, item):
    """
    Maximize the window from system tray
    """

def on_closing():
    """
    Minimize the application to system tray if the the setting is enabled
    If the setting is not enabled the application will close
    Save the state of the settings to the tracker.txt when closing
    """