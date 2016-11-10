# Ben Woodfield - Star Triangle Pyramid Generator - Using while loops
# Python 3
userInput = int(input("Please enter the amount of rows: "))

row = 0
while(row < userInput):
    row += 1
    spaces = userInput - row

    spaces_counter = 0
    while(spaces_counter < spaces):
        print(" ", end ='')
        spaces_counter += 1

    num_stars = 2*row-1
    while(num_stars > 0):
        print("*", end ='')
        num_stars -= 1

    print()
