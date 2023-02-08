# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input

import sys
import math

#
l = sys.argv[1:]
tot = 0

# Want to float the numbers but also the total count for the equation
for i in range(len(l)):
	l[i] = float(l[i])
	tot += l[i]
	
#Create a test to make sure the sum is euqal to 1.0
if math.isclose(tot, 1.0, abs_tol=.01) == False:
	print('False')
else:
	H = 0
	for i in range(len(l)):
		H = H + -(l[i] * math.log(l[i],2))
	print(f'{H:.4}') # If the test passed it will output the results




	



"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
