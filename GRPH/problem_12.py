sample_dataset = """
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
"""


class Fasta:
    def __init__(self, sequnece, k):
        identifier, dna = sequnece.split('/', 1)
        self.sequence = dna.rstrip('/')
        self.identifier = identifier
        self.prefix = self.sequence[:k]
        self.suffix = self.sequence[-k:]


def caculate_graphs(k):
    with open('test.txt') as f:
        fasta = f.read().splitlines()
    fasta = "/".join(fasta)
    fasta = fasta.split('>')
    fasta = list(filter(None, fasta))
    sequences = [Fasta(sequence, k) for sequence in fasta]
    for i in sequences:
        for j in sequences:
            if i != j:
                if i.prefix == j.suffix:
                    print(j.identifier, i.identifier)



if __name__ == '__main__':
    k = 3
    caculate_graphs(k)
