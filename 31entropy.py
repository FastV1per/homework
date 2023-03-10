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

# making sure it is put into a list
inputted_list = sys.argv[1:]
total_value = 0

# Want to float the numbers but also the total count for the equation

for list_value in range(len(inputted_list)):
	try:
		inputted_list[list_value] = float(inputted_list[list_value])
		total_value += inputted_list[list_value]
	except:
		print("This is not it")
	
#Create a test to make sure the sum is euqal to 1.0

if math.isclose(total_value, 1.0, abs_tol=.01) == False:
	print('Does not sum up to 1')
else:
	H = 0
	for entropy in range(len(inputted_list)):
		H = H + -(inputted_list[list_value] * math.log(inputted_list[list_value],2))
	print(f'{H:.4}') # If the test passed it will output the results


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
