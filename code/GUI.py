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
from os import stat
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import SendEmail
import webbrowser
from Scraper import Scraper
import time
import threading
import plyer
import os
import Tracker
import pystray
from pystray import MenuItem as item, Menu as menu
from PIL import Image
import platform
from utils import become_persistent, remove_startup
import pandas as pd
from datetime import datetime

DATAFILE = os.path.join("data", "working_live_data.csv")

class Application(tk.Tk):
    """
    The main application class for the project.
    """

    def __init__(self):
        super().__init__()

        # Check if reloaded
        self.reload = False

        self.geometry("850x550")
        self.resizable(0, 0)

        self.title("Item Stock Tracker")

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=6, pad=5)

        self.is_minimize_to_system_tray = tk.IntVar()

        self.is_launch_at_start_up = tk.IntVar()
        welcome_message = "Welcome to Item Stock Tracker - A program designed to alert users when specific items from an online retailer are back in stock or there is a price drop."
        self.welcome_text = tk.Label(
            text=welcome_message, wraplength=790, justify="left", pady=8
        )

        self.welcome_text = tk.Label(
            text=welcome_message, wraplength=790, justify="left", pady=8
        )

        self.welcome_text.grid(row=0, sticky="NW")

        self.tabs = ttk.Notebook(self, height=450, width=790)

        # Create a frame for a list of items
        self.items = ttk.Frame(self.tabs)

        # Add a listbox to items
        self.items_list = TrackedItemsListbox(
            self.items, height=21, columns=(1, 2, 3, 4), show="headings"
        )
        self.items_list.pack()

        # Add a button for adding an item to track
        plus_image = os.path.join("data", "plus.gif")
        self.plus_image = tk.PhotoImage(file=plus_image).subsample(3)
        self.add_button = tk.Button(
            master=self, command=self.items_list.add_item_popup, image=self.plus_image
        )
        self.add_button.place(x=769, y=40)

        # Create a frame for program info
        ttk.Style().configure("BW.TFrame", background="white")

        self.info = ttk.Frame(self.tabs, style="BW.TFrame")

        info_message = (
            "This application tracks the inventory of specified items offered by "
            "different digital retailers. \nTo add your own items,click the plus button in the upper right. You will be prompted to enter a name for the item you are tracking, along with a URL for a specific product page. "
            "You can also edit, add, or delete items by right-clicking on a selected item.\n"
            "\nIn the Settings tab, you can adjust the refresh interval (how often the program will poll the website to check the stock status of your items), and configure your email alert settings.\n\nCurrently, amazon.com, bestbuy.com and walmart.com product pages are supported."
        )

        self.info_message = tk.Label(
            self.info, text=info_message, wraplength=790, justify="left", pady=8
        )

        # Create a frame for program settings
        ttk.Style().configure("BW.TFrame", background="white")

        self.settings = ttk.Frame(self.tabs, style="BW.TFrame")

        for i in range(6):
            self.settings.rowconfigure(i, pad=5)

        self.interval_label = tk.Label(
            self.settings, text="Refresh Interval (in seconds):  ", bg="white"
        )
        check_numeric = (self.register(self.__verify_numeric), "%d", "%P")
        self.interval_entry = tk.Entry(
            self.settings,
            validate="key",
            validatecommand=check_numeric,
            width=3,
            bg="white",
        )

        self.is_checked = tk.IntVar()
        self.email_alert_label = tk.Label(
            self.settings, text="Send Email Alerts:  ", bg="white"
        )
        self.email_alert_box = tk.Checkbutton(
            self.settings, variable=self.is_checked, bg="white"
        )

        self.email_addr_label = tk.Label(
            self.settings, text="User Email Address:  ", bg="white"
        )

        self.minimize_system_label = tk.Label(
            self.settings, text="Minimize to system tray:  ", bg="white"
        )
        self.minimize_to_system_tray = tk.Checkbutton(
            self.settings, variable=self.is_minimize_to_system_tray, bg="white"
        )

        self.launch_at_start_up_label = tk.Label(
            self.settings, text="Launch tracker at startup:  ", bg="white"
        )
        self.launch_at_start_up = tk.Checkbutton(
            self.settings, variable=self.is_launch_at_start_up, bg="white"
        )

        self.email_addr_entry = tk.Entry(
            self.settings, validate="focus", width=30, bg="white"
        )
        self.save_button = tk.Button(
            self.settings,
            command=self.save_setting,
            textvariable=tk.StringVar(value="Save"),
        )
        self.interval_label.grid(row=0, column=0, sticky="E")
        self.interval_entry.grid(row=0, column=1, sticky="W")
        self.email_alert_label.grid(row=1, column=0, sticky="E")
        self.email_alert_box.grid(row=1, column=1, sticky="W")
        self.email_addr_label.grid(row=2, column=0, sticky="E")
        self.email_addr_entry.grid(row=2, column=1, sticky="W")
        self.minimize_system_label.grid(row=3, column=0, sticky="E")
        self.minimize_to_system_tray.grid(row=3, column=1, sticky="W")
        self.launch_at_start_up_label.grid(row=4, column=0, sticky="E")
        self.launch_at_start_up.grid(row=4, column=1, sticky="W")
        self.save_button.grid(row=5, column=0, sticky="E")

        self.info_message.grid(row=4, column=2, sticky="W")

        # Add the settings and tracked item frames to the notebook
        self.tabs.add(self.items, text="Tracked Items")
        self.tabs.add(self.settings, text="Settings")
        self.tabs.add(self.info, text="Info")
        self.tabs.grid(row=1, sticky="NE", padx=5, pady=5)

        if not self.reload:
            self.reload_state()
            self.reload = True
        self.min_count = 0
        self.run_timer()

        # Scarper object that is used to choose which scraper to run
        self.scraper = Scraper()
        # A lock to keep scarping thread safe
        self.lock = threading.Lock()

    def reload_state(self):
        """
        Populates the listbox with saved values
        """
        if len(s.item) > 0:
            for item in s.item:
                self.items_list.insert(
                    "", "end", values=(item.get("item"), item.get("url"), " ")
                )
        # Update with saved settings
        # Update the refresh interval
        if s.setting != "":
            self.interval_entry.delete(0, "end")
            self.interval_entry.insert(0, s.setting)
        if s.LaunchAtStartup == "True":
            self.launch_at_start_up.select()
        else:
            self.launch_at_start_up.deselect()
        if s.Minimize == "True":
            self.minimize_to_system_tray.select()
        else:
            self.minimize_to_system_tray.deselect()
        # If the email alert is included in the state file
        if "Email" in s.alert:
            self.email_alert_box.select()
            # Display the email address
            emaddress = s.email
            self.email_addr_entry.insert(0, emaddress)

    def save_setting(self):
        """
        Saves the updated setting
        Checks email alert
        """
        if self.is_checked.get():
            if "Email" not in s.alert:
                s.updateAlert("Email")
            s.updateEmail(self.email_addr_entry.get())
        if not self.is_checked.get():
            if "Email" in s.alert:
                s.deleteAlert("Email")
                s.deleteEmail()
        # Check the refresh interval
        if self.is_minimize_to_system_tray.get():
            s.updateMinimize("True")
        else:
            s.updateMinimize("False")

        if self.is_launch_at_start_up.get():
            s.updateLaunchAtStartup("True")
            become_persistent(__file__)
        else:
            s.updateLaunchAtStartup("False")
            remove_startup()

        s.updateSetting(self.interval_entry.get())
        Tracker.save_state(Tracker.FILENAME, s)

    def scraper_data(self):
        """
        Obtains stock info from appropriate scrapers
        Threads run this method
        """
        self.lock.acquire()
        for item in s.item:
            item_name = item.get("item")
            item_url = item.get("url")
            item_stock, item_cost = self.scraper.ChooseScraper(item_url)
            s.updateStatus(item_name, item_url, item_stock, item_cost)
            time.sleep(1)

        self.lock.release()

    def update_stock_info(self, entry, item_name, item_url, item_stock, item_cost):
        """
        Updates the items in the GUI with the stock information
        :param entry: one of the items in the products list
        :param item_name: name of the product
        :param item_url: url of the product
        :param item_stock: stock info of the product
        :param item_cost: price info of the product
        """
        self.items_list.delete(entry)
        self.items_list.insert(
            "", "end", values=(item_name, item_url, item_stock, item_cost)
        )

    def run_timer(self):
        """
        After this function is called for the first time, it will be called again
        every second until the application is closed.
        Delegates GUI updating to update_stock_info and send an alert when item restock
        """
        self.min_count += 1
        print(self.min_count)
        if self.min_count % int(self.interval_entry.get()) == 0:
            self.min_count = 0
            # A separate thread to handle scraping
            thread = threading.Thread(target=self.scraper_data, args=())
            thread.setDaemon(True)
            thread.start()
            for entry in self.items_list.get_children():
                item_name = self.items_list.item(entry)["values"][0]
                item_url = self.items_list.item(entry)["values"][1]
                status = s.getStatus(item_name, item_url)
                item_stock = status.get("status")
                item_pstock = status.get("pstatus")
                item_pcost = status.get("pcost")
                item_cost = status.get("cost")
                print(item_stock, item_pstock, item_pcost, item_name)
                if item_stock == "In Stock":
                    with open(DATAFILE, 'w') as csvfile:
                        fields = ['Name', 'Cost', 'Date', 'Time']
                self.update_stock_info(
                    entry, item_name, item_url, item_stock, item_cost
                )
                if item_stock == "In Stock" and item_pstock != "In Stock":
                    app.update()
                    self.items_list.alert_restock(item_name, item_url)
                    self.interval_entry.focus_force()
                    self.email_addr_entry.focus_force()

                print(item_pcost.replace('$','').replace(',',''), item_cost.replace('$','').replace(',',''))
                # for Testing the working of trigger
                # if(item_pcost!="" and item_pcost!="NA" and (float)(item_pcost.replace('$','').replace(',','')) >=(float)(item_cost.replace('$','').replace(',',''))):
                if(item_pcost!="" and item_pcost!="NA" and (float)(item_pcost.replace('$','').replace(',','')) >(float)(item_cost.replace('$','').replace(',',''))):
                    app.update()
                    self.items_list.alert_price_drop(item_name, item_url, item_pcost, item_cost)
                    self.interval_entry.focus_force()
                    self.email_addr_entry.focus_force()

        self.after(1000, self.run_timer)

    def __verify_numeric(self, action, value):
        """
        This function is used in an entry object, to verify that the input is a number.
        To use it, specify this function as the "validatecommand" option when creating a
        tkinter entry object.
        :param action: Whether data is being inserted or deleted from the entry object, represented as an int
        :param value: The current text of the entry object
        """
        if action != "1":  # if the action is anything other than inserting:
            return True
        try:
            return value.isnumeric()
        except ValueError:
            return False


class TrackedItemsListbox(ttk.Treeview):
    """
    This object is for holding and displaying the list of items that are being tracked by the program.
    It is built off of the ttk.Treeview class, and contains 3 columns (Name, URL, Stock Status).
    """

    def __init__(self, parent, **kwargs):
        ttk.Treeview.__init__(self, parent, **kwargs)

        self.none_selected_menu = tk.Menu(self, tearoff=0)
        self.none_selected_menu.add_command(
            label="Add New Page...", command=self.add_item_popup
        )

        # Add a second menu with more options for when an item is selected
        self.selected_menu = tk.Menu(self, tearoff=0)
        self.selected_menu.add_command(
            label="Add New Page...", command=self.add_item_popup
        )
        self.selected_menu.add_separator()
        self.selected_menu.add_command(label="Delete", command=self.delete_item)
        self.selected_menu.add_command(label="Edit", command=self.edit_item)

        # TODO: Remove these command before release. They are for debugging only
        self.selected_menu.add_separator()
        self.selected_menu.add_command(
            label="Trigger Restock",
            command=lambda: self.alert_restock(
                self.set(self.selection()[0])["1"], self.set(self.selection()[0])["2"]
            ),
        )

        # Make the columns
        self.heading(1, text="Name")
        self.column(1, width="120")
        self.heading(2, text="URL")
        self.column(2, width="400")
        self.heading(3, text="Stock Status")
        self.column(3, width="150")
        self.heading(4, text="Price")
        self.column(4, width="110")
        if platform.system() == "Windows":
            self.bind("<Button-3>", self.menu_popup)
        else:
            self.bind("<Button-2>", self.menu_popup)

    def menu_popup(self, event):
        """
        This function causes a menu with a list of commands to appear. It is intended to be used when the user right
        clicks on the item list.
        """
        if not self.selection():
            try:
                self.none_selected_menu.tk_popup(event.x_root, event.y_root)
            finally:
                self.none_selected_menu.grab_release()
        else:
            try:
                self.selected_menu.tk_popup(event.x_root, event.y_root)
            finally:
                self.selected_menu.grab_release()

    def add_item(self, name, url):
        """
        Adds an item to the list to be tracked.
        :param name: name of the item to be added
        :param url: URL of the product page
        """
        self.insert("", "end", values=(name, url, ""))
        # Add the item - backend
        s.updateItem({"item": name, "url": url, "status": "", "pstatus": "", "pcost":"", "cost":"",})

        self.selection_clear()

    def delete_item(self):
        """
        Deletes the currently selected item.
        """
        for item in self.selection():
            origin_name = self.set(item)["1"]
            origin_url = self.set(item)["2"]
            for row in s.item:
                if row["item"] == origin_name and row["url"] == origin_url:
                    s.item.remove(row)
            self.delete(item)

    def edit_item(self):
        """
        Edits the currently selected item. To do this, it creates a popup to gather the new item information.
        """
        for item in self.selection():
            origin_name = self.set(item)["1"]
            origin_url = self.set(item)["2"]
            popup = GetItemURLDialogue(self, "Edit Item", origin_name, origin_url)

            self.item(item, values=(popup.name, popup.url, self.set(item)["3"]))
            self.set(item)["2"] = popup.url

            # Edit the item - backend
            for row in s.item:
                if row["item"] == origin_name and row["url"] == origin_url:
                    s.item.remove(row)
            s.updateItem({"item": popup.name, "url": popup.url})

    def add_item_popup(self):
        """
        Adds a new item to the list. It launches a popup to gather the name and url for the item from the user.
        """
        popup = GetItemURLDialogue(self, "Add Item", "", "")
        if not popup.cancelled:
            self.add_item(popup.name, popup.url)

    def alert_restock(self, name, url):
        """
        Alerts the user that a particular product is back in stock by launching a popup and, if the email setting is
        active, sending an email.
        :param name: name of the item to be added
        :param url: URL of the product page
        """
        email = ""
        if app.is_checked.get():
            email = app.email_addr_entry.get()
            SendEmail.sendEmail(email, name, url)

        # tempWin = tk.Tk() # Temporary, invisible window to use as a popup's root
        #                   # This way the root will always be in the same thread as the popup
        # tempWin.withdraw()
        # popup = ItemAlertDialogue(tempWin, "Item Restocked!", name, url)

        kwargs = {
            "title": "Item Stock Tracker",
            "ticker": "~Item Stock Tracker~",
            "app_name": "Item Stock Tracker",
            "timeout": 1,
            "message": name + " is restocked! ",
        }
        try:
            plyer.notification.notify(**kwargs)
        except:
            print("unexpected error while notifying")

        popup = ItemAlertDialogue(self, "Item Restocked!", name, url)

    def alert_price_drop(self, name, url, pcost, cost):
        """
        Alerts the user that a particular product is back in stock by launching a popup and, if the email setting is
        active, sending an email.
        :param name: name of the item to be added
        :param url: URL of the product page
        """
        email = ""
        if app.is_checked.get():
            email = app.email_addr_entry.get()
            SendEmail.sendEmail(email, name, url)

        kwargs = {
            "title": "Item Stock Tracker",
            "ticker": "~Item Stock Tracker~",
            "app_name": "Item Stock Tracker",
            "timeout": 1,
            "message": name + " price dropped! ",
        }
        try:
            plyer.notification.notify(**kwargs)
        except:
            print("unexpected error while notifying")

        popup = ItemAlertDialogue(self, "Price Dropped!", name, url,pcost,cost)

class GetItemURLDialogue(tk.simpledialog.Dialog):
    """
    This is a popup for getting the name and url for a product.
    It is build off of the tkinter.simpledialog.Dialog class.
    Information can be retrieved by checking the name and url attributes after the popup has been closed.
    :param parent: the parent object for the popup
    :param title: the title of the new window
    :param name: the default name of the item
    :param url: the default url of the item
    """

    def __init__(self, parent, title, name, url):
        self.name = name
        self.url = url
        self.cancelled = True

        super().__init__(parent, title)

    def body(self, frame):
        """
        This function is called automatically by the object. It controls what objects should be contained in the popup
        frame.
        :param frame:
        :return: the modified frame
        """
        frame.rowconfigure(0, weight=0, pad=5)
        frame.rowconfigure(1, weight=0)
        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(1, weight=0)

        self.name_label = tk.Label(frame, width=6, text="Name: ")
        self.name_label.grid(column=0, row=0)

        self.name_box = tk.Entry(frame, width=30)
        if self.name != "":
            self.name_box.insert(0, self.name)
        self.name_box.grid(column=1, row=0)

        self.url_label = tk.Label(frame, width=6, text="URL: ")
        self.url_label.grid(column=0, row=1)
        self.url_box = tk.Entry(frame, width=30)
        if self.url != "":
            self.url_box.insert(0, self.url)
        self.url_box.grid(column=1, row=1)
        return frame

    def apply(self):
        """
        This function controls what values are applied to the object after the popup closes.
        """
        self.name = self.name_box.get()
        self.url = self.url_box.get()
        self.cancelled = False


class ItemAlertDialogue(tk.simpledialog.Dialog):
    """
    This class defines the popup that is used to alert a user of a restock.
    :param parent: the parent object for the popup
    :param title: the title of the new window
    :param name: the name of the item
    :param url: the url of the item
    """

    def __init__(self, parent, title, name, url, pcost=0, cost=0):
        self.name = name
        self.url = url
        self.pcost = pcost
        self.cost = cost
        super().__init__(parent, title)

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
        frame.rowconfigure(0, weight=0, pad=10)
        frame.rowconfigure(1, weight=0)
        if(self.pcost == 0):
            popup_text = "Your item '" + self.name + "' is back in stock!"
        else:
            popup_text="Price Dropped for item " + self.name + "!\n From "+self.pcost+" to "+self.cost
        self.text = tk.Label(frame, text=popup_text, wraplength=300, justify=tk.LEFT)
        self.text.grid(row=0)

        # self.link = tk.Label(
        #     frame,
        #     text=self.url,
        #     fg="blue",
        #     cursor="hand2",
        #     wraplength=300,
        #     justify=tk.LEFT,
        # )
        # self.link.grid(row=1)
        # self.link.bind("<Button-1>", self.followlink)

        return frame

    def buttonbox(self):
        """
        This function is called automatically by the object. It controls what buttons should be contained in the popup.
        """
        # self.ok_button = tk.Button(
        #     self, text="OK", width=5, command=lambda: self.destroy()
        # )
        # self.ok_button.pack(pady=10)
        self.follow_button = tk.Button(
            self, text="Open in Web Browser", width=20, command=lambda : self.followlink(None)
        )
        self.follow_button.pack(pady=10)


def quit_window(icon, item):
    """
    When clicked on quit from system tray closes the application
    """
    icon.stop()
    app.destroy()


def show_window(icon, item):
    """
    Maximize the window from system tray
    """
    icon.stop()
    app.after(0, app.deiconify())


def on_closing():
    """
    Minimize the application to system tray if the the setting is enabled
    If the setting is not enabled the application will close
    Save the state of the settings to the tracker.txt when closing
    """
    if not app.is_minimize_to_system_tray.get():
        app.save_setting()
        app.destroy()
    else:
        app.withdraw()
        plus_image = os.path.join("data", "plus.gif")
        image = Image.open(plus_image)
        menus = menu(item("Quit", quit_window), item("Show", show_window, default=True))
        icon = pystray.Icon("name", image, "My System Tray Icon", menus)
        icon.run()


if __name__ == "__main__":
    s = Tracker.State()
    Tracker.read_state(Tracker.FILENAME, s)
    app = Application()
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()
    Tracker.save_state(Tracker.FILENAME, s)
