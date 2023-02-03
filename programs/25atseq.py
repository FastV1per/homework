# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

'''
import random # import the random function

length = 30
total = length
count = 0 # gotta love containers


for i in range(length):
    r = random.random() # oddly looks like the one in the tutorial 
    if r < 0.66:
        count += 1
        print('A', end = '')
    elif r < 0.66:
        count += 1
        print('T', end = '')
    elif r < 0.44:
        print('C', end = '')
    else:
        print('G', end = '')
at_content = count/total # i was told that commenting would look nice here
print(length, at_content)
'''

"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
