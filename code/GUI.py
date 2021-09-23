import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from code import tracker
import webbrowser
from code import Scraper


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Check if reloaded
        self.reload = False

        self.geometry('800x500')
        self.resizable(0, 0)

        self.title('Item Stock Tracker')

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=6, pad=5)

        welcome_message = "Welcome to <Name TBD>. This application tracks the inventory of specified items offered by " \
                          "different digital retailers. \n Currently supported retailers include: <TODO: Add these>"

        self.welcome_text = tk.Label(text=welcome_message, wraplength=790, justify='left', pady=8)

        self.welcome_text.grid(row=0, sticky='NW')

        self.tabs = ttk.Notebook(self, height=450, width=790)

        # Create a frame for a list of items
        self.items = ttk.Frame(self.tabs)

        # Add a listbox to items
        self.items_list = TrackedItemsListbox(self.items, height=21, columns=(1, 2, 3), show='headings')
        self.items_list.pack()

        # Add a button for adding an item to track
        self.plus_image = tk.PhotoImage(file="../data/plus.png").subsample(3)

        self.add_button = tk.Button(master=self, command=self.items_list.add_item_popup, image=self.plus_image)
        self.add_button.place(x=769, y=52)

        # Create a frame for program settings
        self.settings = ttk.Frame(self.tabs)

        for i in range(3):
            self.settings.rowconfigure(i, pad=5)

        self.interval_label = tk.Label(self.settings, text="Refresh Interval (in minutes):  ", )
        check_numeric = (self.register(self.__verify_numeric), '%d', '%P')
        self.interval_entry = tk.Entry(self.settings, validate='key', validatecommand=check_numeric, width=3)
        self.interval_entry.insert(0, '10')

        self.is_checked = tk.IntVar()
        self.email_alert_label = tk.Label(self.settings, text="Send Email Alerts:  ")
        self.email_alert_box = tk.Checkbutton(self.settings, variable=self.is_checked)

        self.email_addr_label = tk.Label(self.settings, text="User Email Address:  ")
        self.email_addr_entry = tk.Entry(self.settings, validate='focus', width=30)

        self.interval_label.grid(row=0, column=0, sticky='E')
        self.interval_entry.grid(row=0, column=1, sticky='W')
        self.email_alert_label.grid(row=1, column=0, sticky='E')
        self.email_alert_box.grid(row=1, column=1, sticky='W')
        self.email_addr_label.grid(row=2, column=0, sticky='E')
        self.email_addr_entry.grid(row=2, column=1, sticky='W')

        # Add the settings and tracked item frames to the notebook
        self.tabs.add(self.items, text='Tracked Items')
        self.tabs.add(self.settings, text='Settings')
        self.tabs.grid(row=1, sticky='NE', padx=5, pady=5)

        if not self.reload:
            self.reload_state()
            self.reload = True
        self.min_count = 0
        self.run_timer()

    def reload_state(self):
        # Populate the listbox with saved values
        if len(s.item) > 0:
            for item in s.item:
                self.items_list.insert('', 'end', values=(item.get('item'), item.get('url'), ' '))
        # Update with saved settings
        # Update the refresh interval
        if s.setting != '':
            self.interval_entry.delete(0,'end')
            self.interval_entry.insert(0, s.setting)
        # If the email alert is included in the state file
        if 'Email' in s.alert:
            self.email_alert_box.select()
            # Display the email address
            emaddress = s.email
            self.email_addr_entry.insert(0, emaddress)

    def save_setting(self):
        # Save the updated setting
        # Check email alert
        if self.is_checked.get():
            if 'Email' not in s.alert:
                s.updateAlert('Email')
            s.updateEmail(self.email_addr_entry.get())
        if not self.is_checked.get():
            if 'Email' in s.alert:
                s.deleteAlert('Email')
                s.deleteEmail()
        # Check the refresh interval
        s.updateSetting(self.interval_entry.get())

    # After this function is called for the first time, it will be called again
    # every minute until the application is closed.
    def run_timer(self):
        self.min_count += 1

        if self.min_count % int(self.interval_entry.get()) == 0:
            self.min_count = 0
            # TODO: Add a function to check the stock status of each item

        self.after(60000, self.run_timer)

    # This function is used in an entry object, to verify that the input is a number
    def __verify_numeric(self, action, value):
        if action != '1':  # if the action is anything other than inserting:
            return True
        try:
            return value.isnumeric()
        except ValueError:
            return False


class TrackedItemsListbox(ttk.Treeview):
    def __init__(self, parent, **kwargs):
        ttk.Treeview.__init__(self, parent, **kwargs)

        self.none_selected_menu = tk.Menu(self, tearoff=0)
        self.none_selected_menu.add_command(label="Add New Page...",
                                            command=self.add_item_popup)

        # Add a second menu with more options for when an item is selected
        self.selected_menu = tk.Menu(self, tearoff=0)
        self.selected_menu.add_command(label="Add New Page...",
                                       command=self.add_item_popup)
        self.selected_menu.add_separator()
        self.selected_menu.add_command(label="Delete",
                                       command=self.delete_item)

        # TODO: Remove these command before realease. They are for debugging only
        self.selected_menu.add_separator()
        self.selected_menu.add_command(label="Trigger Restock",
                                       command=lambda: self.alert(self.set(self.selection()[0])['1'],
                                                                  self.set(self.selection()[0])['2']))

        # Make the columns
        self.heading(1, text='Name')
        self.column(1, width='190')
        self.heading(2, text='URL')
        self.column(2, width='490')
        self.heading(3, text='Stock Status')
        self.column(3, width='100')

        self.bind("<Button-3>", self.popup)

    def popup(self, event):
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
        self.insert('', 'end', values=(name, url, "?"))
        # Add the item - backend
        s.updateItem({'item': name, 'url': url})
        # TODO: Add a method for checking if an item is in stock
        scraper = Scraper()
        scraper.ChooseScraper(url)

        self.selection_clear()

    def delete_item(self):
        for item in self.selection():
            self.delete(item)

    def add_item_popup(self):
        popup = GetItemURLDialogue(self, "Add Item", "", "")
        if not popup.cancelled:
            self.add_item(popup.name, popup.url)

    def alert(self, name, url):
        popup = ItemAlertDialogue(self, "Item Restocked!", name, url)


class GetItemURLDialogue(tk.simpledialog.Dialog):
    def __init__(self, parent, title, name, url):
        self.name = name
        self.url = url
        self.cancelled = True

        super().__init__(parent, title)

    def body(self, frame):
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
        self.name = self.name_box.get()
        self.url = self.url_box.get()
        self.cancelled = False


class ItemAlertDialogue(tk.simpledialog.Dialog):
    def __init__(self, parent, title, name, url):
        self.name = name
        self.url = url
        super().__init__(parent, title)

    def followlink(self, event):
        webbrowser.open(self.url)

    def body(self, frame):
        frame.rowconfigure(0, weight=0, pad=10)
        frame.rowconfigure(1, weight=0)

        popup_text = "Your item '" + self.name + "' is back in stock!"
        self.text = tk.Label(frame, text=popup_text, wraplength=300, justify=tk.LEFT)
        self.text.grid(row=0)

        self.link = tk.Label(frame, text=self.url, fg="blue", cursor="hand2", wraplength=300, justify=tk.LEFT)
        self.link.grid(row=1)
        self.link.bind("<Button-1>", self.followlink)

        return frame

    def buttonbox(self):
        self.ok_button = tk.Button(self, text='OK', width=5, command=lambda: self.destroy())
        self.ok_button.pack(pady=10)

def on_closing():
    # Save the setting when closing
    app.save_setting()
    app.destroy()

if __name__ == "__main__":
    s = tracker.State()
    tracker.read_state(tracker.FILENAME, s)
    app = Application()
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()
    tracker.save_state('../data/testsave.txt', s)
