# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

# Need containers and we need to shift the list to only read the values

list_values = sys.argv[1:] # I was told that using descriptive functions makes me a good coder

count = 0
sum = 0

list_values.sort() # This is for the median 


# We need to convert our list of strings into a list of integers

for integers in range(len(list_values)):
	list_values[integers] = int(list_values[integers])
	count += 1
	sum += list_values[integers]

mean = sum/count # Equation for the mean

# We need to find the middle of the list

middle = (len(list_values) -1)//2

# Set up a comparison loop to get the middle of the list

if len(list_values) % 2 == 1:
	medium = list_values[middle]
else:
	medium = (list_values[middle] +list_values[middle + 1]) / 2
	
# Next, find the Std with another for loop (note: we could combine this loop to the previous loop, but for clarity sake,because my dumb butt is going to look back at this, do it this way)

tophalf = 0

for stdev in range(len(list_values)):
	tophalf_val = 0 # equals to the count of the list in a std formula
	tophalf_val = (mean - list_values[stdev]) ** 2
	tophalf += tophalf_val 

# Euqation for std
std = ((tophalf/count) ** .5)

# Print out all values

print('Count:', count)
print('Minmimum', float(min(list_values)))
print('Maximum', float(max(list_values)))
print('Mean', f'{mean:.3f}')
print('Std. dev:', f'{std:.3f}')
print('Median', f'{medium:.3f}') 

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
