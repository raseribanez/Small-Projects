# Ben Woodfield 26/12/2015

# Example 2: A Python program from the Raspberry Pi User Guide - Basic Calculator
#!/usr/bin/env python

userName = input("What is your name? ")
print ("Welcome to the program,"), userName
goAgain = 1
while goAgain ==1:
    firstNumber = int(input("Type the first number: "))
    secondNumber = int(input("Type the second number: "))
    print (firstNumber, "added to", secondNumber, "equals", firstNumber + secondNumber)
    print (firstNumber, "minus", secondNumber, "equals", firstNumber - secondNumber)
    print (firstNumber, "multiplied by", secondNumber, "equals", firstNumber * secondNumber)
    goAgain = int(input("Type 1 to enter more numbers, or any other number to quit: "))

    
    
