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
import sys
import mcb185
import math
import random

# Here is the setup
parser = argparse.ArgumentParser(description ='Entropy Calculator')


# The positional argument that is always required 
parser.add_argument('file', type=str, metavar='<path>', help='fasta file')

# Adding to additional arugments
parser.add_argument('-w', required=False, type=int, default=11, metavar='<int>', help='requires a integer value [%(default)i]')
parser.add_argument('-t', required=False, type=float, default = 1.4, metavar='<float>', help= 'requires a float value [%(default).2f]')
parser.add_argument('-s', required=False, action = 'store_true', help = 'lower-based masking [off]')

# Make sure to finalize the arguments
arg = parser.parse_args()


# I've been told that my dust needs more spice 
# Calculate entropy of a sequence

def entroequ(window):
	
	# Create containers for the equation 
	nts = ['A','T','C','G'] # Identifying the nucleotides
	counts = [0]*4 # how many are in a DNA sequence
	prob = [] 
	H = 0
	
	for nt in window:
		if nt == nts: 
			counts[nts.index(nt)] += 1
			
	for count in counts:
		prob.append(count/len(window))
		
			
	# same equation as the previous python code
	for probnt in prob:
		if probnt != 0:
			H -= probnt * math.log2(probnt)
			
			
	return H


def sliding(sequ, winlen):

	win = sequ[:winlen].upper()

	file_seq = sequ
	
	
	for pos in range(len(seq)):
	
		if pos in range(len(sequ)-winlen +1):
			
			if pos != 0:
				win = (win[1:]+sequ[pos+winlen-1]).upper()
				
			H = entroequ(win)
			
		
			if H < arg.t and arg.s == True:
				file_seq = file_seq.replace(file_seq[pos:pos+winlen], file_seq[pos:pos + winlen].lower()) 

			elif H < arg.t and arg.s == False:
				file_seq = file_seq.replace(file_seq[pos:pos+winlen], 'N'*winlen)
				
		if (pos + 1) % 60 == 0:
			yield(file_seq[pos-59:pos+1])
		
		if len(sequ) % 60 != 0:
			yield(file_seq[len(sequ)-(len(sequ) % 60):])
	


# Separating files 

for line in mcb185.read_fasta(arg.file):
	print('>' + line[0])
	
	for seq in line[1:]:
		for line in sliding(seq,arg.w):
			print(line)
	
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
