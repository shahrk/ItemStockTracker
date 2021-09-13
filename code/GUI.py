import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('600x500')
        self.resizable(0, 0)

        self.title('Item Stock Tracker')

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4, pad=5)

        self.tabs = ttk.Notebook(self)
        self.items = ttk.Frame(self.tabs)
        self.settings = ttk.Frame(self.tabs)

        self.tabs.add(self.items, text='Tracked Items')
        self.tabs.add(self.settings, text='Settings')

        self.tabs.grid(row=1, column=0, sticky='NE', padx=5, pady=5)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
