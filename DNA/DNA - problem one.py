from collections import Counter

dna_sequence = input("Enter your DNA sequence: ")
counter_sequence = Counter(dna_sequence)
print(counter_sequence.get('A'), counter_sequence.get('C'), counter_sequence.get('G'), counter_sequence.get('T'))
