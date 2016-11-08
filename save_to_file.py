# Ben Woodfield
# A basic script that writes data to a text file
# Text example shown...uncomment line 7 to use this in a different context 

f = open( 'file.py', 'w' )
f.write('Heres your saved text!')
#f.write( 'dict = ' + repr(dict) + '\n' )
f.close()
