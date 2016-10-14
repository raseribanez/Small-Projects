# Magic 8 Ball Style Program - Bare Python Version
# Ben Woodfield 01/01/2016

import random
import time
import sys

list = ["Yes, Most Definately", "The Chances Are High!", "Not Likely!", "May The Odds Be Ever In Your Favour.",
                        "Is That Really Your Question?", "Try It Out And See!", "23% Chance", "99.9% Success Rate!",
                        "Congratulations - It looks good!", "Computer Says NO!", "Ask Again Later", "Better Not Tell You Now",
            "Cannot Predict Now", "Concentrate And Ask Again", "Dont Count On It!,", "No Chance!", "Only Smarties Have The Answer"]

def userInput():
        question = ('Enter Your Question:')
        print(question)
        stuff = raw_input ('>' ) # here the original code was just [stuff = input ('> ') - the user had to type question within quotes (without knowing) - by changing input to [raw_input] the user can now just type anything

        print('\nThinking..\n')
        time.sleep(3)
        print(random.choice(list))

        final()

def final():
        print('Would you like to ask another question? - Type yes if you do')
        user_reply = raw_input("> ") # here the same modification was made - changing [input] to [raw_input] allowing the user to freely type (without "quote marks") 
        while(raw_input("> ")):
                if user_reply == 'yes':
                        
                        userInput()
                else:
                        print('Thanks For Playing!')
                        sys.exit(0) # if user quits (by typing anything other than [yes]) an error is displayed (line 35, line 23, line 33, line35)
print('Welcome To The Magic 8 Ball!')
userInput()

        


