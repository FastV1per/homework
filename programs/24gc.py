# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

'''
dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
total = len(dna)
count = 0

for i in range(total): # this was a doozy 
    nt = dna[i] # needed to index it since dna is a string
    if nt == 'C' or nt == 'G':
        count = count + 1 # want to count G and C as a integer
gc_content = count/float(total) # making sure to float just in case
print(f'{gc_content:.2f}') # format for 2 decimal points
'''

"""
python3 24gc.py
0.42
"""
