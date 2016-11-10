#!usr/bin/env/python
# Ben Woodfield - An example of how to paste/duplicate a string of text.
# For Python 3 change 'Tkinter' to 'tkinter' next line down 
from Tkinter import *

def show_entry_fields():
    e2.insert(10,(e1.get()))

master = Tk()
master.minsize(width=250, height=20)
master.configure(bg='DarkGrey')

Label(master, fg='Blue',  bg='DarkGrey', text="Paste").grid(row=0)
Label(master, fg='Blue',  bg='DarkGrey',  text="Output").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


Button(master, text='Quit', fg='Red',  bg='Black', command=quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Convert',  fg='Red',  bg='Black', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)    

mainloop()
