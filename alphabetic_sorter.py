# Ben Woodfield
# Sort results into alphabetic order

# change this value for a different result
my_str = "highlighter flipping alphabet critical becomes during elephant green "

# Use input from the user - uncomment - plan is to use this for word-lists
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
