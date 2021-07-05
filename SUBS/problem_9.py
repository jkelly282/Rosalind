sample_dataset = "GATATATGCATATACTT"
sample_motif = "ATAT"

problem_motif = "GGTTCGTGG"
with open("rosalind_subs.txt") as f:
    dna = f.read().strip()

answer = []

for i, j in enumerate(dna):
    if dna[i: i + len(problem_motif)] == problem_motif:
        answer.append(i + 1)

print(" ".join(str(x) for x in answer))
