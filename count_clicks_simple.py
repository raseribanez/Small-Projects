from Tkinter import *

top = Tk()
top.title('Title')
top.minsize(300,300)

presses = 0

def add_click():
    global presses
    # Add 1 to presses
    presses += 1
    lbl.configure(text=presses)#,fg='Blue', font='freesansbold,50')

lbl = Label(top, text='Total bags checked:')
lbl.pack()

btn = Button(top, text='Click', command=add_click)
btn.pack()

btn_2 = Button(top, text='Click', command=add_click)
btn_2.pack()

btn_3 = Button(top, text='Click', command=add_click)
btn_3.pack()

btn_4 = Button(top, text='Click', command=add_click)
btn_4.pack()

btn_5 = Button(top, text='Click', command=add_click)
btn_5.pack()

top.mainloop()
