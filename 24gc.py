# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

'''
dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
total = len(dna)
count = 0

for i in range(total):
    nt = dna[i]
    if nt == 'C' or nt == 'G':
        count = count + 1
gc_content = count/float(total)
print(f'{gc_content:.2f}')
'''

"""
python3 24gc.py
0.42
"""
