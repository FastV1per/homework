# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below

import sys
import random

# we create a list that doesn't have the title 
list = sys.argv[1:]

# separate each item with the following variables 
gen_size = int(list[0])
read_num = int(list[1])
read_len = int(list[2])

# create an emtpy container for genome size
gen = []
gen = [0] * gen_size

# position the genome according to read number
for pos in range(read_num):
	begin = random.randint(0, gen_size - read_len)
	
	#add one to the position in the genome where hits overlap
	for h in range(begin, begin + read_len):
		gen[h] += 1
	
# find minimum, maximum and sum
mini = gen[read_len - 1]
maxi = gen[read_len - 1]
sum = 0

# the genome at the read positions
for c in gen[read_len - 1:-read_len]:
	if mini > c: 
		mini = c
	if maxi < c:
		maxi = c
	sum += c

# average coverage, ignoring the ends
average = sum / (gen_size - 2 * read_len)
	
print(mini, maxi, f'{average:.5}')
	

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
