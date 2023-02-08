# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

# Need containers and we need to shift the list to only read the values

l = sys.argv[1:]
count = 0
sum = 0
l.sort() # This is for the median 


# We need to convert our list of strings into a list of integers

for i in range(len(l)):
	l[i] = int(l[i])
	count += 1
	sum += l[i]

mean = sum/count # Equation for the mean

# We need to find the middle of the list

mid = (len(l) -1)//2

# Set up a comparison loop to get the middle of the list

if len(l) % 2 == 1:
	med = l[mid]
else:
	med = (l[mid] +l[mid + 1]) / 2
	
# Next, find the Std with another for loop (note: we could combine this loop to the previous loop, but for clarity sake, do it this way)

tophalf = 0

for i in range(len(l)):
	x = 0 # x equals to the count of the list in a std formula
	x = (mean - l[i]) ** 2
	tophalf += x 

# Euqation for std
std = ((tophalf/count) ** .5)

# Print out all values

print('Count:', count)
print('Minmimum', float(min(l)))
print('Maximum', float(max(l)))
print('Mean', f'{mean:.3f}')
print('Std. dev:', f'{std:.3f}')
print('Median', f'{med:.3f}') 

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
