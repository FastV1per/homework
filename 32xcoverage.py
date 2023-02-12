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

#import sys for command line arguments
import sys
import random

#create a list from command line without leading title
list = sys.argv[1:]

#list should have a length of 3, with the following variables
genome_size = int(list[0])
read_num = int(list[1])
read_length = int(list[2])

#make the genome list with 0s
genome = []
genome = [0] * genome_size

#make positions in the genome according to read number
for pos in range(read_num):
	begin = random.randint(0, genome_size - read_length)
	
	#add one to the position in the genome where hits overlap
	for hit in range(begin, begin + read_length):
		genome[hit] += 1
	
#intialize minimum, maximum and sum
mini = genome[read_length - 1]
maxi = genome[read_length - 1]
sum = 0

#go thru the genome at the read positions
for count in genome[read_length - 1:-read_length]:
	if mini > count: 
		mini = count
	if maxi < count:
		maxi = count
	sum += count

#find the average coverage, ignoring the ends
average = sum / (genome_size - 2 * read_length)
	
print(mini, maxi, f'{average:.5}')
	

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
