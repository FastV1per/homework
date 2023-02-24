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

# BRAINSTORMING not finished 
import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description='Line, word, and byte counts.')
parser.add_argument('file', type=str, metavar='<path>', help='some file')
parser.add_argument('-c', '--bytes', action='store_true', help='byte count')
parser.add_argument('-l', '--lines', action='store_true', help='line count')
parser.add_argument('-w', '--words', action='store_true', help='word count')
arg = parser.parse_args()

if arg.file == '-': fp = sys.stdin
else:               fp = open(arg.file)

bc = 0
lc = 0
wc = 0
while True:
	line = fp.readline()
	if line == '': break
	bc += len(line)
	lc += 1
	wc += len(line.split())

print(lc, wc, bc)


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
