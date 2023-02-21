# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

import sys
import mcb185
import math

# create a function for entropy

def entroequ(file, w, threshold):
	
	for defline, seq in mcb185.read_fasta(file):
	
		newseq = ''
		
		for pos in range(len(seq) - w + 1):
			smseq = seq[pos:pos + w]
			
			A = 0
			T = 0
			G = 0
			C = 0
			
			for nt in smseq:
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
			
			if H < threshold:
				newseq += 'N'
			else:
				newseq += smseq[0]
	return defline, newseq


# spearate the file 
file = sys.argv[1]
w = int(sys.argv[2])
threshold = float(sys.argv[3])

defline, newseq = entroequ(file, w, threshold)


print(defline)
for pos in range(0, len(newseq), 60):
	print(newseq[pos:pos + 60])		
		
			


"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
