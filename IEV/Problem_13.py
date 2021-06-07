genotype = {0: 1, 1: 1, 2: 1, 3: .75, 4: .5, 5: 0}

with open('test.txt') as f:
    pop = f.read().split()

total = 0
for i, j in enumerate(pop):
    total += ((genotype[i] * int(j)) * 2)
print(total)
