# Week 4: Python Basics

## About you

**Script (`about_me.py`):**

```python
#!/usr/bin/env python3

# Store each piece of information in its own variable (all strings)
name = "Theo"
color = "green"
activity = "Soccer"
animal = "Chimps"

# print() can take several items separated by commas,
# and it puts a space between them automatically
print("My name:", name)
print("My favorite color:", color)
print("My favorite activity:", activity)
print("My favorite animal:", animal)
```

**Explanation:** The script defines four variables (name, favorite color, favorite activity, and favorite animal), each holding a string. It then uses `print()` with commas to display a label followed by the value of each variable, so the output uses the variables instead of hard-coded text. The comments in the script explain each step.

**Output:**

```
My name: Theo
My favorite color: green
My favorite activity: Soccer
My favorite animal: Chimps
```

## Codon to amino acid

**Script (`codon_to_aa.py`):**

```python
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
```

**Explanation:** The script first reads `CodonTable.tsv` and builds a dictionary in which each codon is a key and its amino acid symbol is the value. It finds the `Codon` and `Symbol` columns by name in the header row, then adds one entry per row. Next it stores the input sequence `"CTA GGA GTG ATT TCG"` in a string and uses `split()` to cut it at the spaces into a list of three-letter codons. It then loops over the codons, looks each one up in the dictionary, and appends the amino acid to a list. Finally it prints that list.

**Output:**

```
['L', 'G', 'V', 'I', 'S']
```

**Note:** `CodonTable.tsv` was located in `Unix/DataFiles/` of the course repository rather than `Python/DataFiles/`, so I copied it into this folder and the script reads it from here.
