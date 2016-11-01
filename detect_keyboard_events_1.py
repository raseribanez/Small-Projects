# Ben Woodfield
# A simple GUI program that detects Keyboard activity and returns to the user
# uses bind_all
# UnHash to add mouse activity

import Tkinter
from Tkinter import *

top = Tk()
top.minsize(300,100)
top.title('Detect Key Press')
prompt = 'Press any Key, Number or Symbol'
L = Label(top, text=prompt, width=len(prompt))
L.pack()
B = Button(top, text='Exit', command=quit)
B.pack(side=BOTTOM, fill=X)

def key(event):
    if event.char == event.keysym:
        msg = 'Normal Key %r' % event.char
    elif len(event.char)==1:
        msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)
    else:
        msg = 'Special Key %r' % event.keysym
    L.config(text=msg)
L.bind_all('<Key>', key)

#def do_mouse(event_name):
#    def mouse_binding(event):
#        L.config(text='Mouse event %s' % eventname)
#    L.bind_all('<%s>' %eventname, mouse_binding)
#for i in range(1,4):
#    do_mouse('Button-%s'%i)
#    do_mouse('ButtonRelease-%s'%i)
#    do_mouse('Double-Button-%s'%i)

top.mainloop()
