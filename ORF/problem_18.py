from collections import Counter
import re


class Fasta:
    def __init__(self, overall_info):
        self.overall_info = overall_info
        # self.id = ''.join(overall_info.split('|')[1])
        self.sequence = ''.join([line for line in overall_info.split('\n') if not '>' in line])

    def as_dict(self):
        return {i: j for i, j in enumerate(self.sequence)}

    def find_motifs(self):
        return [(str(m.start() + 1)) for m in re.finditer('(?=[N][^P][S|T][^P])', self.sequence)]


def protein_finder(dna):
    protein = []
    return_proteins = []
    orf = False
    for i in range(0, len(dna), 3):
        aa = translate.get(dna[i:i + 3])
        if aa == 'M':
            orf = True
        elif aa == 'Stop':
            orf = False
            if protein:
                return_proteins.append("".join(protein))
            protein = []
        if orf == True:
            protein.append(aa)
    return return_proteins


def reverse_translate(dna):
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
    rdna = "".join(reverse_comp)
    return rdna


translate = {
    "TTC": "F",
    "CTC": "L",
    "ATC": "I",
    "GTC": "V",
    "TTA": "L",
    "CTA": "L",
    "ATA": "I",
    "GTA": "V",
    "TTG": "L",
    "CTG": "L",
    "ATG": "M",
    "GTG": "V",
    "TCT": "S",
    "CCT": "P",
    "ACT": "T",
    "GCT": "A",
    "TCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "TCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "TCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "TAT": "Y",
    "CAT": "H",
    "AAT": "N",
    "GAT": "D",
    "TAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "TAA": "Stop",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "TAG": "Stop",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "TGT": "C",
    "CGT": "R",
    "AGT": "S",
    "GGT": "G",
    "TGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "TGA": "Stop",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "TGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",
    "TTT": "F",
    "CTT": "L",
    "ATT": "I",
    "GTT": "V",
}

with open("test2.txt") as f:
    dna = f.read().strip()
    dna = Fasta(dna)
    dna = dna.sequence

rdna = reverse_translate(dna)

overall_proteints = set()
for i in range(3):
    foward = protein_finder(dna[i:])
    reverse = protein_finder(rdna[i:])
    for j in foward:
        counter_sequence = Counter(j)
        number_of_start = counter_sequence.get('M')
        if number_of_start > 1:
            for p, q in enumerate(j):
                if p != 0:
                    if q == 'M':
                        overall_proteints.add(j[p:])
        overall_proteints.add(j)

    for k in reverse:
        counter_sequence = Counter(k)
        number_of_start = counter_sequence.get('M')
        if number_of_start > 1:
            for p, q in enumerate(k):
                if p != 0:
                    if q == 'M':
                        overall_proteints.add(k[p:])
        overall_proteints.add(k)

for i in overall_proteints:
    print(i)
