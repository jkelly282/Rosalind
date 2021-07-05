from constants import aa_weights
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', dest='protein', help='Protein string')
    args = parser.parse_args()
    return args


def calculate_weights(protein):
    total_weight = 0
    for aa in protein:
        weight = aa_weights.get(aa)
        total_weight += weight
    return round(total_weight, 3)


if __name__ == '__main__':
    args = parse_args()
    with open(args.protein) as f:
        protein = f.read().splitlines()
    protein = ''.join(protein)
    print(calculate_weights(protein))
