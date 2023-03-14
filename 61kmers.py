# 61kmers.py

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

# Hint: use argparse
# Hint: use mcb185.read_fasta()

import argparse
import mcb185


# Using argparse to initalize, place required arguments, and finish setup
parser = argparse.ArgumentParser(description = 'Finding the kmer counts for a fasta file')

parser.add_argument('file', type = str, metavar = '<path>', help = 'Need nt fasta file')
parser.add_argument('Klen', type = int, metavar = '<path>', help = 'Need size of K')

arg = parser.parse_args()


# Create an empty dictionary as were going to put keys:values in
kmers = {}

# Reading the file
for line in mcb185.read_fasta(arg.file):

	# We only want to read the data, not the headers
	for seq in line[1:]:
		
		# Our Kmers window equation
		for pos in range(len(seq) - arg.Klen + 1):
			
			kmer = seq[pos:pos + arg.Klen]
			
			# Count kmers and put back into the list
			if kmer not in kmers:
				kmers[kmer] = 1
			else:
				kmers[kmer] += 1

# Sort and then print out the value and the count
for kmer in sorted(kmers):
	print(kmer, kmers[kmer])
	


"""
python3 61kmers.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 2
AA 338006
AC 256773
AG 238013
AT 309950
CA 325327
CC 271821
CG 346793
CT 236149
GA 267384
GC 384102
GG 270252
GT 255699
TA 212024
TC 267395
TG 322379
TT 339584
"""
