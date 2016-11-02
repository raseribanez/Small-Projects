# Ben Woodfield
# A basic calenday display - lets the user choose the month/year
# unless the instruction comments are followed below

# import module
import calendar

# Uncomment these 2 lines and select specific values to remove user input and display chosen info
#yy = 2014
#mm = 11

# Ask what month and year from the user - comment these out to remove this feature
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))
