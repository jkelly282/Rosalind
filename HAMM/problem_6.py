with open('rosalind_hamm.txt') as f:
    dna = f.read().strip()
strands = dna.split('\n')

difference = 0
for i, j in enumerate(strands[0]):
    if j != strands[1][i]:
        difference += 1
print(difference)
