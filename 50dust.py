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

def entroequ(seq, w):
	A = 0
	T = 0
	G = 0
	C = 0
			
	for nt in seq:
		if nt == 'A':
			A += 1			
		elif nt == 'T':
			T += 1
		elif nt == 'G':
			G += 1
		elif nt == 'C':
			C += 1
					
	probA = A / w
	probT = T / w
	probG = G / w
	probC = C / w
			
	probnts = [probA, probT, probG, probC]
			
	# same equation as the previous python code
	H =  0
	for probnt in probnts:
		if probnt != 0:
			H += -(probnt * math.log2(probnt))
			
	return H

window = arg.w // 2


# unpacking in for loop
for defline, seq in mcb185.read_fasta(arg.file):
	seq = seq.upper()
	seq2 = list(seq)
	for line in range(len(seq) -arg.w + 1):
		wseq = seq[line:line + arg.w]
		H = entroequ(wseq, arg.w)
		if H < arg.t:
			for win in range(arg.w):
				if arg.lower: 
					seq2[line + win] = seq2[line + win].lower()
				else:
					seq2[line + win] = 'N'
	
	seq2 = ''.join(seq2)
	print('>',defline)
	for pos in range(0,len(seq2), 60):
		print(seq2[pos: pos + 60])
	

'''
for line in mcb185.read_fasta(arg.file):
	print('>' + line[0])
	
	for seq in line[1:]:
		for line in sliding(seq,arg.w):
			print(line)
'''

	
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
