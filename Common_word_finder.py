# PYTHON CODE FOR FINDING THE MOST COMMON WORD IN A TEXT FILE
# Ben Woodfield 27/01/2016

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

print bigword, bigcount
