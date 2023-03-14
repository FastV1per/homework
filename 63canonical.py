# 63canonical.py

# You probably learned that ATG is the only start codon, but is it?
# Write a program that reports the start codons from the E. coli genome
# Your program must:
#    1. read GCF_000005845.2_ASM584v2_genomic.gbff.gz at the only input
#    2. use a regex to find CDS coordinates
#    3. count how many different start codons there are

# Note: the sequence is at the end of the file
# Note: genes on the negative strand are marked complement(a..b)

# Hint: you can read a file twice, first to get the DNA, then the CDS
# Hint: check your CDS by examining the source protein

# Sorry Korf, take a point off of this one, I can't figure it out


import re
import mcb185

def find_start_codons(filename):
	with open(filename, 'r') as f:
		lines = f.readlines()
	   
	sequences = []
	for i in range(0, len(lines), 2):
		sequence = lines[i+1].strip()
		sequences.append(sequence)
	  
	   
	# Find the start codons and CDS coordinates for each sequence
	start_codons = []
	cds_coordinates = []
	for seq in sequences:
	# Find the start codons
		start_codons_seq = re.findall(r'ATG', seq)
		start_codons.extend(start_codons_seq)
	       
		# Find the CDS coordinates
		cds_coords_seq = []
		
	    # Count the different start codons
	    start_codon_counts = {}
	    for codon in start_codons:
	    	if codon in start_codon_counts:
	    		start_codon_counts[codon] += 1
		else:
			start_codon_counts[codon] = 1
	   
	    # Print the results
	    print('Start codons:')
	    for codon, count in start_codon_counts.items():
	    	print(f'{codon}: {count}')
	   
	    print('CDS coordinates:')
	    for i, seq in enumerate(sequences):
	    	print(f'Sequence {i+1}:')
	    	for start, end in cds_coordinates[i]:
	    		print(f'{start+1}-{end}')
	

"""
python3 63canonical.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gbff.gz
ATG 3883
GTG 338
TTG 80
ATT 5
AGT 1
AAA 1
AGC 1
TTC 1
TAA 1
CGT 1
CTG 2
GAC 1
"""
