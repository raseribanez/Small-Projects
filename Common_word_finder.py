# Written and tested on Python 2.7 - then edited later using Python 3
# Ben Woodfield 27/01/2016

# This finds the most common word that appears in a file
# Asks for a filename, opens file, reads text,
# then finds and prints the most repeated word.
# And prints a word count for the word
# When I edited this using Python3 I removed raw_input() 
# -and added parentheses to the print statement

# 02/12/2016 I changed raw_input() to input()
name = input('Enter File:')
handle = open(name, 'r')
text = handle.read()
words = text.split()
counts = dict()

for word in words:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# For Python 3 I added the parentheses (brackets)        
print(bigword, bigcount)
