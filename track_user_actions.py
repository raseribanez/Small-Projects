# Ben Woodfield
# Uses Poll to track users action - in this case a Listbox selection
# NOTE The original example was from an OLD book I was reading, using Python 2.4
# I rewrote this for Python 2.7.11 - but may have a syntax problem during my conversion
# Let me know if you look at this and manage to sort it (raserppsprograms@gmail.com)

from Tkinter import *
import Tkinter

top = Tk()

F1 = Frame(top)
s = Scrollbar(F1)
L = Listbox(F1)
s.pack(side=RIGHT, fill=Y)
L.pack(side=LEFT, fill=Y, yscrollcommand=s.set) # This may throw an error - I believe it is just a syntax issue from my conversion
s['command'] = L.yview
for i in range(30): L.insert(END, str(i))
F1.pack(side=TOP)

F2 = Frame(top)
lab = Label(F2)
def poll():
    lab.after(200, poll)
    sel = L.curselection()
    lab.config(text=str(sel))
lab.pack()
F2.pack(side=TOP)

poll()
top.mainloop
