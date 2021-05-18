with open("rosalind_revc.txt") as f:
    dna = f.read().strip()
reverse_comp = []
for i in dna:
    if i == "A":
        reverse_comp.append("T")
    elif i == "T":
        reverse_comp.append("A")
    elif i == "G":
        reverse_comp.append("C")
    elif i == "C":
        reverse_comp.append("G")
    else:
        print("Unknown character")

reverse_comp.reverse()
print("".join(reverse_comp))
