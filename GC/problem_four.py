from collections import Counter

with open("rosalind_gc.txt") as f:
    dna = f.read().strip()

fasta = dna.split('>')


def calculate_gc(line):
    fasta = line.split('\n')
    gc = 0
    check_gc = ''.join(fasta[1:])
    total = len(check_gc)
    nucleotides = Counter(check_gc)
    gc = (nucleotides.get('G') + nucleotides.get('C')) / total
    return gc * 100


gc = 0
for line in fasta[1:]:
    new_gc = calculate_gc(line)
    if new_gc > gc:
        name = line.split('\n')[0]
        gc = new_gc
print(f'{name} \n{gc}')
