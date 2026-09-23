#!/usr/bin/env python3

# 1. Build a dictionary: Codon column (key) -> Symbol column (value)
codon_table = {}

with open("CodonTable.tsv") as f:
    # Read the header row and split it at each tab
    header = f.readline().strip().split("\t")
    # Find which position holds each column
    codon_col = header.index("Codon")
    symbol_col = header.index("Symbol")

    # Go through every remaining row
    for line in f:
        if line.strip() == "":          # skip blank lines
            continue
        fields = line.strip().split("\t")
        codon_table[fields[codon_col]] = fields[symbol_col]

# 2. The input sequence, with spaces
dna = "CTA GGA GTG ATT TCG"

# 3. Split it into three-letter codons
codons = dna.split()

# 4. Look up each codon and save the amino acids in a list
aa_seq = []
for codon in codons:
    aa_seq.append(codon_table[codon])

# 5. Print the amino acid sequence
print(aa_seq)
