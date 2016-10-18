# Turtle-Module Drawing App (Turtle is usually built-in to Python)
# Runs fine on Python 2.7 - Uses keyboard (no mouse detection)
# Ben Woodfield / Original code found online, I made a few edits and also added comments with code descriptions

######### INSTRUCTIONS FOR USING THE APP ###########################################
# The physics to this is very much like Etch-a-Sketch, turn and draw.              #
# UP ARROW KEY    = move the line forward (draw)                                   # 
# DOWN ARROW KEY  = move the pointer backwards (to previous position)              #
# LEFT ARROW KEY  = turn the pointer 45 degrees left (anti-clockwise) each press   #
# RIGHT ARROW KEY = turn the pointer 45 degrees right (clockwise)                  #
# H KEY           = (lower or upper case) move the pointer back to start position  #
# C KEY           = (lower or upper case) clear the screen / delete drawing        #
# Q KEY           = (lower or upper case) quit / exit the App cleanly              #
####################################################################################

import turtle

# Create and set up screen and turtle.
t = turtle
# May need to tweak dimensions below for your screen - This should be fine though.
t.setup(600, 600)
t.Screen()
t.title("Turtle Drawing Program")
t.showturtle()

# Set movement step and turning angle.
step = 160
angle = 45

# Here we create the functions for the app (movement,turning,home point,clear)
# Forward movement function
def forward():
    '''Move forward step positions.'''
    print "forward", step
    t.forward(step)

# Backwards movement function
def back():
    '''Move back step positions.'''
    print "back", step
    t.back(step)

# Turn left function
def left():
    '''Turn left by angle degrees.'''
    print "left", angle
    t.left(angle)

# Turn right function 
def right():
    '''Turn right by angle degrees.'''
    print "right", angle
    t.right(angle)

# Move pointer back to the start function
def home():
    '''Go to turtle home.'''
    print "home"
    t.home()

# Clear the drawing area (delete drawing) function
def clear():
    '''Clear drawing.'''
    print "clear"
    t.clear()

# Exit the App function
def quit():
    print "quit"
    t.bye()

t.onkey(forward, "Up")
t.onkey(left, "Left")
t.onkey(right, "Right")
t.onkey(back, "Down")
t.onkey(home, "h")
t.onkey(home, "H")
t.onkey(clear, "c")
t.onkey(clear, "C")
t.onkey(quit, "q")
t.onkey(quit, "Q")

# Make the program 'listen' for key activity from user (detect button pressing)
t.listen()

# Set the loop that runs the program - to display it on screen
t.mainloop()
