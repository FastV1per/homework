#!/usr/bin/env python3

# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. has option and default value for window size
# 2. has option and default value for entropy threshold
# 3. has a switch for N-based or lowercase (soft) masking
# 4. works with uppercase or lowercase input files
# 5. works as an executable

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

# BRAINSTORMING DON'T GRADE

# import packages  
import argparse
import mcb185
import math
import random

# Here is the setup
parser = argparse.ArgumentParser(description ='Entropy Calculator')


# The positional argument that is always required 
parser.add_argument('file', type=str, metavar='<path>', help='fasta file')

# Adding to additonal arugments
parser.add_argument('-w', required=False, type=int, default=11, metavar='<int>', help='requires a integer value [%(default)i]')
parser.add_argument('-t', required=False, type=float, default = 1.4, metavar='<float>', help= 'requires a float value [%(default).3f]')
parser.add_argument('-s', action = 'store_true', help = 'lower-based masking')

# Make sure to finalize the arguments
arg = parser.parse_args()


# I've been told that my dust needs more spice 
# Calculate entropy of a sequence

def entroequ(window):
	
	# Create containers for the equation 
	nts = 'ATCG' # Identifying the nucleotides
	counts = [0]*4 # how many are in a DNA sequence
	prob = [] 
	
	for remain in window:
		for nt in nts:
			if remain == nt: counts[nts.index(nt)] += 1
			
	for count in counts:
		prob.append(count/len(window))
		
			
	# same equation as the previous python code
	H =  0
	for probnt in prob:
		if probnt != 0:
			H += -(probnt * math.log2(probnt))
			
			
	return H


def sliding(sequ, winlen, threshold):

	file_seq = []
	
	for pos in range(len(sequ)-winlen +1):
	
		window = sequ[pos:pos + winlen]
		H = scal(window)
		
		if H >= threshold: 
			file_seq.append(sequ[pos])
		else:
			file_seq.append('N')
		
		if len(file_seq) >= 60:
			yield(''.join(file_seq))
			file_seq = []
	
	for nt in range(len(sequ)-winlen + 1, len(sequ)):
		file_seq.append(sequ[nt])
		
		if len(file_seq) >= 60:
			yeild(''.join(file_seq))
			file_seq = []


# Separating files 
sequ = sys.argv[1]
winlen = int(sys.argv[2])
threshold = float(sys.argv[3])

for seq in mcb185.read.fasta(sequ):
	print('>' + sequ[0])
	for line in sequ[1:]:
		for nts in sliding(line, winlen, threshold):
			print(nts)
	
"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGcttttcattctGACTGCAACGGGCAATATGTCTCTGTGTggattaaaaaaagagtgTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGagtaaattaaaattttattgaCTTAGG
TCACtaaatactttaaCCAATATAGGCATAGCGCACAGacagataaaaattacaGAGTac
acaacatccaTGAAACGCATTAGCACCACCATtaccaccaccatcaccaTTACCACAGGT
AACggtgcgggctgACGCGTACAGgaaacacagaaaaaagccCGCACCTGACAGTGCggg
ctttttttttcgaCCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AggcaggggcaggtggCCAccgtcctctctgcccccgccaaaatcaccaaccacctGGTG
GCGATgattgaaaaaaccattaGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
"""
