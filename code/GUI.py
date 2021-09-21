import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from PIL import Image
from PIL import ImageTk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

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

        

        # Add the settings and tracked item frames to the notebook
        self.tabs.add(self.items, text='Tracked Items')
        self.tabs.add(self.settings, text='Settings')
        self.tabs.grid(row=1, sticky='NE', padx=5, pady=5)

        # TODO: Add settings


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

        # TODO: Add a method for checking if an item is in stock

        self.selection_clear()

    def delete_item(self):
        for item in self.selection():
            self.delete(item)

    def add_item_popup(self):
        popup = GetItemURLDialogue(self, "Add Item", "", "")
        if not popup.cancelled:
            self.add_item(popup.name, popup.url)


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

if __name__ == "__main__":
    app = Application()
    app.mainloop()
