with open("rosalind_rna.txt") as f:
    dna = f.read()
rna = dna.replace("T", "U")
print(rna)
