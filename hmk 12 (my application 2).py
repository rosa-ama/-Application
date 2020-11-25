import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title("My Application 2")

win.configure(background="blue")
ttk.Label(win,text="Enter Your Name").grid(column=0,row=0)


def click_me():
    button.configure(text="Hello " + name.get() + " The season you've chosen is "
                     + season_chosen.get()) 




name = tk.StringVar()
name_entered = ttk.Entry(win, width="15", textvariable=name)
name_entered.grid(column=0,row=1)


ttk.Label(win, text="Pick your favourite season").grid(column=1,row=0)

season = tk.StringVar()
season_chosen = ttk.Combobox(win, width=15, state="readonly")
season_chosen["values"] = ("Spring","Summer","Winter","Autumn")
season_chosen.grid(column=1,row=1)

button = ttk.Button(win, text="Click Me!!!", command=click_me)
button.grid(column=2,row=1)
