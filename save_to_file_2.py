# Ben Woodfield
# Write variable to a text file
# This will save data into a text file called bens_file.txt
# Problem....if I run the program twice it overwrites the data - not adds to it

var_one = ("Text inside file")

f = open( 'created_file.txt', 'w' )
f.write(var_one)
f.close()
