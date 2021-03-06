import argparse
import re


class Fasta:
    def __init__(self, overall_info):
        self.overall_info = overall_info
        # self.id = ''.join(overall_info.split('|')[1])
        self.sequence = "".join(
            [line for line in overall_info.split("\n") if not ">" in line]
        )
        self.reverse_complemeent = self.generate_reverse_complement_sequence(
            self.sequence
        )
        self.sequence_length = len(self.sequence)

    def as_dict(self):
        return {i: j for i, j in enumerate(self.sequence)}

    def find_motifs(self):
        return [
            (str(m.start() + 1))
            for m in re.finditer("(?=[N][^P][S|T][^P])", self.sequence)
        ]

    def generate_reverse_complement_sequence(self, sequence):
        reverse_comp = []
        for i in sequence:
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
        return "".join(reverse_comp)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", dest="protein", help="Protein string")
    args = parser.parse_args()
    return args


def generate_sequences(fasta: Fasta):
    for i, j in enumerate(fasta.sequence):
        if i + 12 < fasta.sequence_length:
            start_len = 12
        else:
            start_len = fasta.sequence_length - i
        for k in range(start_len, 3, -1):
            forward_seq = fasta.sequence[i: i + k]
            reverse_seq = fasta.generate_reverse_complement_sequence(forward_seq)
            if forward_seq == reverse_seq:
                print(i + 1, k)


if __name__ == "__main__":
    args = parse_args()
    with open(args.protein) as f:
        protein = f.read()
    fasta = Fasta(protein)
    generate_sequences(fasta)
