# Ben Woodiield
# This was aimed to display a scrolling message reading "HELLO" across the screen.
# Was intended to be run from a terminal, mixed results from IDLE and terminal - if you can help me with this, ideas are welcome

import os
import time

WIDTH = 79
message = "hello!".upper()
#this is a 7-line display, stored as 7 strings
printedMessage = [ "","","","","","","" ]

# a dictionary mapping letters to their 7-line banner display equivalents. #
# each letter in the dictionary is mapped to 7 strings, one for each line  #
# of the display.
characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " " ],

               "E" : [ "*****",
                       "*    ",
                       "*    ",
                       "*****",
                       "*    ",
                       "*    ",
                       "*****" ],
               
               "H" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "*   *" ], 

               "O" : [ "*****",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*****" ],

               "L" : [ "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*****" ],

               "!" : [ "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "     ",
                       "  *  " ]
               
               }

for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")

# The offset is how far to the right the message gets printed.
# Print the message just off the display.
offset = WIDTH
while True:
    os.system("cls")
    #print each line of the message, including the offset.
    for row in range(7):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
    #move the message a little to the left.
    offset -=1
    #if the entire message has moved 'through' the display then
    #start again from the right hand side.
    if offset <= ((len(message)+2)*6) * -1:
        offset = WIDTH
    #take out or change this line to speed up / slow down the display
    time.sleep(0.05) 
