# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

# Dear Lilith, if you're reading this, I'm sorry. My vm destroyed itself while I was playing around with it and I didn't save our work. Thankfully I have a blank slate and can do this another, easier way. 

# From your student, Sam

import sys
import random

list = sys.argv[1:]

# split this into two list
days = int(list[0])
people = int(list[1])

prob = 0 

# We want to try this multiple times by doing multiple trials
trials = 1000

# we must create a list of random days to put into trial 
for days_assigned in range(trials):
	doubles = 0
	birthdays = []
	
	for i in range(days):
		birthdays.append(0) 

# Assign people with birthdays
	for birthday in range(people):
		birth_day = random.randint(0,days-1)
		birthdays[birth_day] = birthdays[birth_day] + 1

# Going to see who's got the same birthday
	for twins in birthdays:
		if twins > 1:
			doubles += 1
		if doubles > 0:
			prob += 1
			match = 0
			break

# Calculating probability
birth_paradox = prob/ trials

print(f'{birth_paradox:.3}')
	  


"""
python3 33birthday.py 365 23
0.571
"""

