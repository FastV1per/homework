# 27frame.py

# Write a program that prints out the position, frame, and letter of the DNA

# Variation: try coding this with a single loop and nested loops

# Note: use 0-based indexing for position and frame (biology uses 1-based)

dna = 'ATGGCCTTT'

"""
dna = 'ATGGCCTTT'
pos = 0

for i in range(0,len(dna),3): # most difficult thing 
    for frame in range(3): # for in with range, you want a frame that is within range of each nt
        print(pos, frame, dna[pos]) 
        pos += 1 # move on to the next
"""

"""
python3 27frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 CS
6 0 T
7 1 T
8 2 T
"""
