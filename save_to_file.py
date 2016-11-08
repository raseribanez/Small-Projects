# Write to a text file
f = open( 'file.py', 'w' )
f.write( 'dict = ' + repr(dict) + '\n' )
f.close()
