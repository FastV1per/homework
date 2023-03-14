# 62orfs.py

# Make a program that finds open reading frames in the E. coli genome
# Your program should read a fasta file
# There should be an optional minimum ORF size with a default value of 300 nt
# The output should be a table showing 4 columns
#     1. parent sequence identifier
#     2. begin coordinate
#     3. end coordinate
#     4. strand
#     5. first 10 amino acids of the protein

# Hint: use argparse, mcb185.read_fasta(), and mcb185.translate()
# Hint: don't use the whole genome for testing

# Note: your genes should be similar to those in the real genome

import argparse
import mcb185 
import re 



# Initialize argument parser
parser = argparse.ArgumentParser(description='Find ORFS in genome that has optional ORF size')
	
# Take arguments: fasta file and min orf len
parser.add_argument('file', type=str, metavar='<path>', help='FASTA file')
parser.add_argument('-l', type=int, metavar='<int>', required=False,
	default=300, help='minimum ORF size [%(default)i]')

# Finish argument parser setup
arg = parser.parse_args()


# Finda all possible ORFS
def get_orfs(iden, strand, seq):

	# Initialize variables
	anti = {'A':'T', 'T':'A', 'G':'C', 'C':'G'} 
	
	# Make anti-sense strand
	if strand == '-':
		aseq = ''
		for nt in seq[::-1]: aseq += anti[nt]
		seq = aseq

	# Returing codons
	for i in range(len(seq)-3):
	
		# Making sure that the starting frame match the min ORFs
		if i >= len(seq)-arg.l: 
			break
		
		# Slide window
		cd = seq[i:i+3]
		
		# Get protein seq and translate
		if cd == 'ATG': 
		
			# use mcb185 translate
			pseq = mcb185.translate(seq[i:])
			
			
			if pseq == None:
				continue
			
		
			pseq = pseq.split('*')[0]
			start = i+len(pseq)*3+3 # start of the orf
			
			# Check for min len
			if len(pseq) < arg.l/3 or pseq == None:
				continue
			
			# Report ORF to its length
			elif strand == '+':
				yield(iden, i+1, start, '+', pseq[:10])
				continue
			elif strand == '-':
				yield(iden, len(seq)-start+1, len(seq)-i, '-', pseq[:10])
				continue


# Read fasta file and then get given results
for desc, seq in mcb185.read_fasta(arg.file):

	# Obtain the identifier for the sequence
	iden = re.search('\w+.\S+', desc)
	iden = iden.group()

	# Report the orf stats for each strand
	for iden, start, end, strand, pseq in get_orfs(iden, '+', seq):
		print(iden, start, end, strand, pseq)
	for iden, start, end, strand, pseq in get_orfs(iden, '-', seq):
		print(iden, start, end, strand, pseq)




"""
python3 62orfs.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz
NC_000913.3 108 500 - MVFSIIATRW
NC_000913.3 337 2799 + MRVLKFGGTS
NC_000913.3 2801 3733 + MVKVYAPASS
NC_000913.3 3512 4162 - MSHCRSGITG
NC_000913.3 3734 5020 + MKLYNLKDHN
NC_000913.3 3811 4119 - MVTGLSPAIW
NC_000913.3 5310 5738 - MKIPPAMANW
NC_000913.3 5683 6459 - MLILISPAKT
NC_000913.3 6529 7959 - MPDFFSFINS
NC_000913.3 7366 7773 + MKTASDCQQS
"""
