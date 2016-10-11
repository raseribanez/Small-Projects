# Ben Woodfield 08/02/2016
# Feet_2_Meters calculator. My second version

#!/usr/bin/env python   
from Tkinter import *  

top = Tk()
top.minsize(400, 200)
top.title('((Raser Apps))')

raser = Label(top, text='FEET to METERS Conversion Calculator', fg='purple', font='freesansBold, 14')
raser.pack()

q = Button(top, text='Exit', command=quit, fg='red') 
q.pack(side=BOTTOM, fill=X) 

cvt_from = StringVar()
cvt_to = StringVar() 

def do_convert():
    feet_val = float(cvt_from.get())
    meters_val = feet_val * 0.3048
    cvt_to.set('%s meters' % meters_val)

from_lbl = Label(top, text='Enter FEET (numbers only):', fg='blue', font='12') 
from_lbl.pack() 

from_entry = Entry(top, textvariable=cvt_from) 
from_entry.pack() 

to_lbl = Label(top, text='Result:', fg='purple', font='12') 
to_lbl.pack()

result_lbl = Label(top, textvariable=cvt_to, bg='yellow', font='freesansBold, 12')
result_lbl.pack()

convert_btn = Button(top, text='Convert to Meters', fg='blue', command=do_convert)
convert_btn.pack()

top.mainloop()
