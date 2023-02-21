# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane

import sys
import mcb185

# create a KD calculation:

def KD_equ(smseq):

	KD = 0 
	
	for aa in smseq:
		if aa =='I':
			KD += 4.5
		elif aa == 'V':
			KD += 4.2
		elif aa == 'L':
			KD += 3.8
		elif aa == 'F':
			KD += 2.8
		elif aa == 'C':
			KD += 2.5
		elif aa == 'M':
			KD += 1.9
		elif aa == 'A':
			KD += 1.8
		elif aa == 'G':
			KD += -0.4
		elif aa == 'T':
			KD += -0.7
		elif aa == 'S':
			KD += -0.8
		elif aa == 'W':
			KD += -0.9
		elif aa == 'Y':
			KD += -1.3
		elif aa == 'P':
			KD += -1.6
		elif aa == 'H':
			KD += -3.2
		elif aa == 'E':
			KD += -3.5
		elif aa == 'Q':
			KD += -3.5
		elif aa == 'D':
			KD += -3.5
		elif aa == 'N':
			KD += -3.5
		elif aa == 'K':
			KD += -3.9
		elif aa == 'R':
			KD = -4.5
		else:
			continue
	return KD


# create an hydrophobic alpha-helix function

def alpha_h(smseq):
	
	proline = 0
	for aa in smseq:
		if aa == 'P':
			proline += 1
		else:
			continue
	return proline
	

# copy and match function with signal peptide and transmembrane 

proteome = sys.argv[1]

for name_def, seq in mcb185.read_fasta(proteome):

	peptide = 0
	transmem = 0 
	
	sigpep = 8
	for pos in range(0, 30 - sigpep + 1):
		smseq = seq[pos:pos + sigpep]
		KD = KD_equ(smseq)
		proline = alpha_h(smseq)
		if KD / sigpep > 2.5 and proline == 0:
			peptide += 1
	
	hydro_reg = 11
	for pos in range(31, len(seq) - hydro_reg + 1):
		smseq = seq[pos:pos + hydro_reg]
		KD = KD_equ(smseq)
		proline = alpha_h(smseq)
		if KD / hydro_reg > 2.0 and proline == 0:
			transmem += 1
	
	if peptide != 0 and transmem != 0:
		print(name_def)

"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
