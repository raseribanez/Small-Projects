#!usr/bin/env/python
# Ben Woodfield
# A basic demonstration of a loop
# This was from a guide I was following - I am not sure what the output
# is actually doing, theres no obvious pattern, it starts off by increasing
# at an 'increase + 1' type rate (increase by 5, then by 6, then by 7....)
# But that stops when it reaches 45 and it goes off. I just wanted some 
# basic examples to use as a reference if I geet stuck.

sum = 0
i = 0
while i < 10:
	sum = sum + i
	print sum
	i = i + 1
	
for i in range(10):
	sum = sum + i
	print sum
