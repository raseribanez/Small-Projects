# Ben Woodfield / Python 2.7 / Learning exercise in Tkinter
# For Python 3, change 'Tkinter' to 'tkinter'
import Tkinter
from Tkinter import *
import random

# Set up the main (top) window's settings
top = Tk()
top.minsize(270,300)
top.title('Magic 8 Ball')
top.configure(bg='Black')

# Put all the answers in one variable [in a tuple]
answers = ["Yes, Most Definately!",
           "The Chances Are High!",
           "Not Likely!",
           "The Odds Look Good!",
           "Is That Your Question?",
           "You Have To Wait And See!",
           "23% Chance!",
           "99.9% Success Rate!",
           "It looks good!",
           "Computer Says NO!",
           "Unable to Decide!"
           "Ask Again Later!",
           "Better Not Tell You Now!",
           "Cannot Predict Result!",
           "Concentrate & Ask Again!",
           "Dont Count On It!",
           "No Chance!",
           "Only Smarties Have The Answer!"]

# Write a new function to either print out a random choice from above
# -or display an error if the user doesn't enter any text
def get_answer():
        msg = "ERROR: Your question must be TEXT"
        i = userentry.get() # gets the text from the entrybox
        y = i.isdigit()
        l = len(userentry.get())

        if y == True or 1 == 0:
               userentry.insert(0,(msg))

        else:
                x = random.choice(answers)
                userentry2.delete(0, END)   # Clear previous output
                userentry2.insert(0,str(x)) # Insert response

# An event handler to delete the text in the entry boxes
# When the Reset button is clicked the text should clear in both entry boxes
def entry_clear():
  userentry.delete(0,END)
  userentry2.delete(0,END)


# Make the buttons and entry boxes (but not packing them yet)
# These are the labels (to display text)
lbl1 = Label(top, text='Enter Your Question', bg='Black', fg='Red', font='freesansbold, 16')
lbl2 = Label(top, text='Answer', bg='Black', fg='Red', font='freesansbold, 16')
lbl3 = Label(top, text='0\n0', bg='Black', fg='Black')

# These are the two buttons (quit and get-answer)
btn1 = Button(top, text='Get Answer', bg='darkBlue', fg='Red', font='freesansbold', command=get_answer)
btn3 = Button(top, text='Reset', bg='darkBlue', fg='Red', font='freesansbold', command=entry_clear)
#btn2 = Button(top, text='Exit', bg='Red', fg='Black', font='freesansbold', command=quit)

# This allows a string-variable to be added to the window
circleVar = StringVar()
userentry = Entry(top, textvariable=circleVar)

circleVar2 = StringVar()
userentry2 = Entry(top, bg='Black', fg='Red', font='freesansbold, 12', justify=CENTER)

# Pack everything into the window (in order of appearance unless told otherwise)
lbl1.pack()
userentry.pack()
btn1.pack()
lbl3.pack()
lbl2.pack()
userentry2.pack(fill=X,expand = True)
btn3.pack()
#btn2.pack(side=BOTTOM)

# This loop is needed to actually display the program, and keep it on-screen
top.mainloop()


