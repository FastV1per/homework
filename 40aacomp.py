# 40aacomp.py

# Make a program that reports the amino acid composition in a file of proteins

# Note: you are not allowed to import any libraries except gzip and sys

# Hint: gzip.open(sys.argv[1], 'rt')

# Variation: use 20 named variables
# Variation: use a list

import gzip
import sys


# One strategy is to write each aa out and have it count everyone and then find the composition
# Containers for all amino acids
A = 0
C = 0
D = 0
E = 0
F = 0
G = 0
H = 0
I = 0
K = 0
L = 0
M = 0
N = 0
O = 0
P = 0
Q = 0
R = 0
S = 0
T = 0
V = 0
W = 0
Y = 0
total = 0 # this also includes the total


with gzip.open(sys.argv[1], 'rt') as fp: #this opens the file 
	for line in fp.readlines():
		line = line.rstrip()
		if not line.startswith('>'):
			total += len(line)
			A += line.count('A')
			C += line.count('C')
			D += line.count('D')
			E += line.count('E')
			F += line.count('F')
			G += line.count('G')
			H += line.count('H')
			I += line.count('I')
			K += line.count('K')
			L += line.count('L')
			M += line.count('M')
			N += line.count('N')
			P += line.count('P')
			Q += line.count('Q')
			R += line.count('R')
			S += line.count('S')
			T += line.count('T')
			V += line.count('V')
			W += line.count('W')
			Y += line.count('Y')
print('A', A, A/total)
print('C', C, C/total)
print('D', D, D/total)
print('E', E, E/total)
print('F', F, F/total)
print('G', G, G/total)
print('H', H, H/total)
print('I', I, I/total)
print('K', K, K/total)
print('L', L, L/total)
print('M', M, M/total)
print('N', N, N/total)
print('P', P, P/total)
print('Q', Q, Q/total)
print('R', R, R/total)
print('S', S, S/total)
print('T', T, T/total)
print('V', V, V/total)
print('W', W, W/total)
print('Y', Y, Y/total)



"""
# Another strategy is to make the amino acid into a list and then assigning them values

total = 0
aas = 'ACDEFGHIKLMNPQRSTVWY'
caa = [0] * len(aas)

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			continue
		
		total += len(line)
		for i in range(len(aas)):
			aa = aas[i]
			caa[i] += line.count(aa)
			prob = caa/total

print(caa, prob)
"""



"""
python3 40aacomp.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
A 126893 0.0954
C 15468 0.0116
D 68213 0.0513
E 76890 0.0578
F 51796 0.0389
G 97830 0.0736
H 30144 0.0227
I 79950 0.0601
K 58574 0.0440
L 142379 0.1071
M 37657 0.0283
N 51896 0.0390
P 59034 0.0444
Q 59178 0.0445
R 73620 0.0554
S 76865 0.0578
T 71428 0.0537
V 94237 0.0709
W 20297 0.0153
Y 37628 0.0283
"""
