import tkinter as tk
from tkinter import ttk
import tracker
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
                          "different digital retailers. To begin, right click the empty box below."
        self.welcome_text = tk.Label(text=welcome_message, wraplength=790, justify='left', pady=8)

        self.welcome_text.grid(row=0, sticky='NW')

        self.tabs = ttk.Notebook(self, height=450, width=790)

        self.items = ttk.Frame(self.tabs)

        # Add a listbox to items

        self.items_list = TrackedItemsListbox(self.items, height=21, columns=(1, 2, 3), show='headings')
        self.items_list.pack()
        for item in s.item:
            self.items_list.insert('', 'end', values=(item.get('item'), item.get('url'), ' '))

        self.settings = ttk.Frame(self.tabs)

        self.tabs.add(self.items, text='Tracked Items')
        self.tabs.add(self.settings, text='Settings')

        self.tabs.grid(row=1, sticky='NE', padx=5, pady=5)

        # Add a button for adding an item to track

        self.plus_image = tk.PhotoImage(file="../data/plus.png").subsample(3)

        self.add_button = tk.Button(master=self, command=self.items_list.add_item, image=self.plus_image)
        self.add_button.place(x=769, y=52)

        # TODO: Add settings




class TrackedItemsListbox(ttk.Treeview):
    def __init__(self, parent, **kwargs):
        ttk.Treeview.__init__(self, parent, **kwargs)

        self.none_selected_menu = tk.Menu(self, tearoff=0)
        self.none_selected_menu.add_command(label="Add New Page...",
                                            command=self.add_item)

        # Add a second menu with more options for when an item is selected
        self.selected_menu = tk.Menu(self, tearoff=0)
        self.selected_menu.add_command(label="Add New Page...",
                                       command=self.add_item)
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

    def add_item(self):
        # TODO: Add a popup to actually get a real page URL

        self.insert('', 'end', values=("TODO:", "Add a", "Pop-up"))
        self.selection_clear()

    def delete_item(self):
        for item in self.selection():
            self.delete(item)

if __name__ == "__main__":
    s = tracker.State()
    tracker.read_state(tracker.FILENAME, s)
    app = Application()
    app.mainloop()
    tracker.save_state('../data/testsave.txt',s)

