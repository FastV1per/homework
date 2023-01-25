# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'

'''
dna = 'ACTGAAAAAAAAAAA'[::-1]

for i in dna:
    if i == 'A':
        print('T',end = '')
    elif i == 'T':
        print('A',end = '')
    elif i == 'G':
        print('C',end = '')
    else:
        print('G',end = '')
print()
'''

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
