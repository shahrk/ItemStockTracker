import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('800x500')
        #self.resizable(0, 0)

        self.title('Item Stock Tracker')

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=6, pad=5)

        welcome_message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt " \
                          "ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation " \
                          "ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in " \
                          "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur " \
                          "sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id " \
                          "est laborum. "
        self.welcome_text = tk.Label(text=welcome_message, wraplength=790, justify='left', pady=8)

        self.welcome_text.grid(row=0, sticky='NW')

        self.tabs = ttk.Notebook(self, height=450, width = 790)
        self.items = ttk.Frame(self.tabs)
        self.settings = ttk.Frame(self.tabs)

        self.tabs.add(self.items, text='Tracked Items')
        self.tabs.add(self.settings, text='Settings')

        self.tabs.grid(row=1, sticky='NE', padx=5, pady=5)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
