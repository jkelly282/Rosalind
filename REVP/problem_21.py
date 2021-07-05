import argparse
import re


class Fasta:
    def __init__(self, overall_info):
        self.overall_info = overall_info
        # self.id = ''.join(overall_info.split('|')[1])
        self.sequence = ''.join([line for line in overall_info.split('\n') if not '>' in line])
        self.reverse_complemeent = self.generate_reverse_complement_sequence(self.sequence)

    def as_dict(self):
        return {i: j for i, j in enumerate(self.sequence)}

    def find_motifs(self):
        return [(str(m.start() + 1)) for m in re.finditer('(?=[N][^P][S|T][^P])', self.sequence)]

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
    parser.add_argument('-p', dest='protein', help='Protein string')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    with open(args.protein) as f:
        protein = f.read()
    fasta = Fasta(protein)
    for i in range(len(fasta.sequence)):
        for j in range(i + 1, i + 12):
            forward = fasta.sequence[i:j]
            reverse = fasta.generate_reverse_complement_sequence(forward)
            if forward == reverse:
                if len(forward) > 4:
                    print(forward)
                    print(i)
            else:
                break
