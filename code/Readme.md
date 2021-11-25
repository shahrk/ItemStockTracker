
# Functional Description: 


### Scraper.py:
Scraper.py chooses and decides which scraper to run.  'ChooseScraper' chooses the scraper.

ChooseScraper(self, url):    
Chooses the scraper based on product url
@param url: URL of the product
@return: the stock status information
       
### Tracker.py
The Tracker serves as the backend of our program. Supports the save and reload of state, modify to the item list and settings.
   

### updateSetting(self, setting):
        Update the setting with given setting
        @param setting: the given setting

### updateMinimize(self, Minimize):
         Update the Minimize with given setting
        @param Minimize: the given Minimize

### updateLaunchAtStartup(self, LaunchAtStartup):
        Update the Minimize with given setting
        @param LaunchAtStartup: the given LaunchAtStartup
  
### updateItem(self, iturl):
        Update the item list with given item dict
        @param iturl: the given item dict,contains the item name, url, status and previous status

### updateAlert(self, alert):
        Update the alert with given alert, add the new alert to the alert list
        @param alert: given alert

### updateEmail(self, email):
        Update the email with given email
        @param email: the given email
### deleteAlert(self, alert):
        Delete an alert
        @param alert: given the alert name which we want to delete
    
### updateStatus(self, item, url, status, cost):
        Update the item status
        @param item: given item name
        @param url: given item url
        @param status: new item status
        @param cost: given item cost


### getStatus(self, item, url):
        Get the item status for specific item
        @param item: given item name
        @param url: given item url
        @return: the item status for given item

### save_state(filename, s):
    Save the state to the file
    @param filename: the filename we want to save the state to
    @param s: is the state instance which stores the state data


### AmazonScraper.py
    This is the Scraper for Amazon. Takes in product url as input upon object creation.
    Method 'job' prints progress while method 'check_stock' obtains stock info and a string indicating cost of the product.
    Amazon pages can have stock info in different ways. Following are the possible cases,
    interpretations, and return values of each case.

        * "In Stock" - Product is in stock - return "In Stock"
        * "Only x left Order soon" - Product is in stock - return "In Stock"
        * "Currently unavailable" - product is out of Stock - return "Out of Stock"
        * "In stock soon" - Product is out of stock - return "Out of Stock"
        * No stock information on the page/Captcha page - No stock info - return "No Stock Info"



### BestBuyScraper.py
    This is the Scraper for BestBuy. Takes in product url as input upon object creation.
    Method 'job' prints progress while the method 'check_stock' obtains stock info and a string indicating cost of the product.


### WalmartScraper.py
    This is the Scraper for Walmart. Takes in product url as input upon object creation.
    Method 'job' prints progress while method 'check_stock' obtains stock info and a string indicating cost of the product.
    Walmart pages can have stock info in different ways. Following are the possible cases,
    interpretations, and return values of each case.

        * "Add to Cart" - Product is in stock - return "In Stock"
        * "Out of Stock" - product is out of Stock - return "Out of Stock"

### Inventory():
      "This application tracks the inventory of specified items offered by "
      "different digital retailers. \nTo add your own items,click the plus button in the upper right. You will be prompted to enter a name for the item you are tracking, along with a URL for a specific product page. "
       "You can also edit, add, or delete items by right-clicking on a selected item.\n"
       "\nIn the Settings tab, you can adjust the refresh interval (how often the program will poll the website to check the stock status of your items), and configure your email alert settings.\n\nCurrently, amazon.com, bestbuy.com and walmart.com product pages are supported."


### on_closing():
    Minimize the application to system tray if the the setting is enabled
    If the setting is not enabled the application will close
    Save the state of the settings to the tracker.txt when closing

### class ItemAlertDialogue(tk.simpledialog.Dialog):
     This class defines the popup that is used to alert a user of a restock.
    :param parent: the parent object for the popup
    :param title: the title of the new window
    :param name: the name of the item
    :param url: the url of the item

### GetItemURLDialogue(tk.simpledialog.Dialog):
    This is a popup for getting the name and url for a product.
    It is build off of the tkinter.simpledialog.Dialog class.
    Information can be retrieved by checking the name and url attributes after the popup has been closed.
    :param parent: the parent object for the popup
    :param title: the title of the new window
    :param name: the default name of the item
    :param url: the default url of the item

### alert_restock(self, name, url):
        Alerts the user that a particular product is back in stock by launching a popup and, if the email setting is
        active, sending an email.
        :param name: name of the item to be added
        :param url: URL of the product page

### TrackedItemsListbox(ttk.Treeview):
    This object is for holding and displaying the list of items that are being tracked by the program.
    It is built off of the ttk.Treeview class, and contains 3 columns (Name, URL, Stock Status).

### sendEmail(receiver, itemName, url):
    Sending the notification email to the giving user.
    Takes in the user's email, product name, and product url as input.
    In order to send the email, please prepare an email account and
    fill in the gmail_user for email address and gmail_password for password
    :param receiver: The email address of the receiver(User)
    :param itemName: The name of the the product
    :param url: URL of the product
    :return: 1 if the email sent successfully, 0 if not



