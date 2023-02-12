# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

import sys
import random

list = sys.argv[1:]

days = int(list[0])
people = int(list[1])

num_simulated = 10000
num_double = 0

birth = [0] * days

for friends in range(people):
	birthdays = friends % days
	birth[birthdays] +=1
	if birth[birthdays] > 1:
		return True
return False

for i in range(num_simulated):
	if birth == True:
		num_double +=1
prob = num_double/num_simulated

print(prob)


"""
python3 33birthday.py 365 23
0.571
"""

