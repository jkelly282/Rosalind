genotype = {0: 1, 1: 1, 2: 1, 3: 0.75, 4: 0.5, 5: 0}

with open("test2.txt") as f:
    pop = f.read().split()

total = 0
for i, j in enumerate(pop):
    total += (genotype[i] * int(j)) * 2
print(total)
