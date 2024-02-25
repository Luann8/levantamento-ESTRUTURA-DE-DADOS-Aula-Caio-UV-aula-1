dna_sequence = "ATCGATCGATCGATCG"

print("Primeiros três nucleotídeos:", dna_sequence[:3])
print("Últimos três nucleotídeos:", dna_sequence[-3:])

print("Número de 'A's na sequência:", dna_sequence.count('A'))

print("Comprimento da sequência:", len(dna_sequence))

dna_sequence += "ATCG"
print("Sequência após adição:", dna_sequence)

dna_sequence = dna_sequence[:-4]
print("Sequência após remoção:", dna_sequence)
