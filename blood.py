# Defining a DNA sequence
dna_sequence = "ATCGATCGATCGATCG"

# Accessing parts of the sequence
print("First three nucleotides:", dna_sequence[:3])
print("Last three nucleotides:", dna_sequence[-3:])

# Counting occurrences of a specific nucleotide
print("Number of 'A's in the sequence:", dna_sequence.count('A'))

# Length of the sequence
print("Length of the sequence:", len(dna_sequence))

# Adding new nucleotides
dna_sequence += "ATCG"
print("Sequence after addition:", dna_sequence)

# Removing nucleotides
dna_sequence = dna_sequence[:-4]
print("Sequence after removal:", dna_sequence)
