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

# I like to dedicate this to steph who has had to explained to me the millionth time why we should reassigned the window and not just be the variable itself.  


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

def entroequ(window):

	# Setting up variables
	# List of all the nts 
	nts = ['A', 'T', 'G', 'C']
	# the count of those nts in a sequence
	nt_counts = [0]*4 
	# prob of thpse nts in the sequence
	nt_probs = []
	# entropy container 
	H = 0 # Shannon entropy
	
	
	# Count and index nts
	for nt in window: 
		if nt in nts: 
			nt_counts[nts.index(nt)] += 1
	
	# align probs with counts
	for count in nt_counts: 
		nt_probs.append(count/len(window))
	
	# Entropy equation with probs
	for prob in nt_probs:
		if prob != 0: H -= prob * math.log2(prob)
		
	return H
	
	
	
# Filtering for window size
def shiftwin(seq, winlen):
	 
	
	# Window has sequences now
	window = seq[:winlen].upper()
	# Need to copy entire sequence to make it all uppercase
	fil_seq = seq.upper()
	
	# We're going to replace the original sequence with the filtered one
	for pos in range(len(seq)):
	
		# The start is determined by the window's sequence
		if pos in range(len(seq)-winlen+1):
	

			if pos != 0: 
				window = (window[1:]+seq[pos+winlen-1]).upper()
		
			H = entroequ(window)

			
			# The unmask arguments will convert to lowercase
			if H < arg.t and arg.s == True:
				fil_seq = fil_seq.replace(
					fil_seq[pos:pos+winlen], fil_seq[pos:pos+winlen].lower())
			
			# The rest are left alone and are the masked argument
			elif H < arg.t and arg.s == False:
				fil_seq = fil_seq.replace(
					fil_seq[pos:pos+winlen], 'N'*winlen)
		
		# Print sequence 60 nts per row
		if (pos+1) % 60 == 0:
			yield(fil_seq[pos-59:pos+1])
		
	# Remaining sequence is printed
	if len(seq) % 60 != 0: 
		yield(fil_seq[len(seq)-(len(seq)%60):])
		

# Open the file
for line in mcb185.read_fasta(arg.file):

	# Print genome description
	print('>'+line[0]) 
	
	# Print the filtered sequence
	for seq in line[1:]: 
		for line in shiftwin(seq, arg.w): print(line)
		
# Note to self: if you find yourself wanting to test this code again in the future, make sure the e.coli.fna data is in the right directory-- hint hint

	
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
