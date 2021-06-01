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


def caculate_graphs():
    with open('test.txt') as f:
        fasta = f.read()
    fasta = fasta.split('>')
    sequences = {}
    for i in fasta:
        identifier, value = i
        sequences[identifier] = value
    print(sequences)


if __name__ == '__main__':
    caculate_graphs()
