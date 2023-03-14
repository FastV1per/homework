# 70gff.py

# Write a program that converts genes in gff into JSON
# Use the E. coli genome gff
# Your code should mimic the output below

import json

def converter(filename):
	
	with open('GCF_000005845.2_ASM584v2_genomic.gff.gz' , 'r') as f:
		lines = f.readlines()
	
	genes = []
	for line in lines:
		if not line.startswith('#'):
			fields = line.strip().split('\t')
			if fields[2] == 'genes':
				genes = {
					'gene': fields[0],
					'beg': fields[1],
					'end': fields[2],
					'strand': fields[3]
					}
				
				at_fields = fields[8].split(';')
				for at_field in at_fields:
					at_parts = at_field.split('=')
					at_name = at_parts[0]
					at_value = at_parts[1]
					gene['convert'][at_name] = at_value
				
				genes.append(gene)


json_string = json.dumps(genes, indent = 4)
print(json_string)


"""
python3 70gff.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gff.gz
[
    {
        "gene": "thrL",
        "beg": 190,
        "end": 255,
        "strand": "+"
    },
    {
        "gene": "thrA",
        "beg": 337,
        "end": 2799,
        "strand": "+"
    },
...
"""
