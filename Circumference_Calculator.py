# Ben Woodfield
# A simple Tkinter program for calculating circumferences
# Written in Python 2, to use on Python 3 change Tkinter to capitol T in the import line

#!/usr/bin/env python
from Tkinter import *


top = Tk()
top.minsize(400, 200)
top.title('((Raser Apps))')

raser = Label(top, text='Circumference Calculator')
raser.pack()

# was freezing up when trying to quit with Exit button (program not responding
# So I hashed it out. the user has to click the X to exit
#qt_btn = Button(top, text='Exit', command=quit)
#qt_btn.pack(side=BOTTOM)

cvt_from = StringVar()
cvt_to = StringVar()


def do_convert():
    radi_val = float(cvt_from.get())
    circum_val = radi_val * 6.2831
    
    cvt_to.set('%s Circumference' % circum_val)

from_lbl = Label(top, text='Enter the value of the Radius 'R' (in numbers)')
from_lbl.pack()

from_entry = Entry(top, textvariable=cvt_from)
from_entry.pack()

to_lbl = Label(top, text='Result:')
to_lbl.pack()

result_lbl = Label(top, textvariable=cvt_to, bg='lightYellow', fg='purple', font='12')
result_lbl.pack()

calculate_btn = Button(top, text='Calculate Circumference', command=do_convert)
calculate_btn.pack()

top.mainloop()
