import requests
from requests import HTTPError
import re


class Fasta:
    def __init__(self, overall_info):
        self.overall_info = overall_info
        self.id = ''.join(overall_info.split('|')[1])
        self.sequence = ''.join([line for line in overall_info.split('\n') if not '>' in line])

    def as_dict(self):
        return {i: j for i, j in enumerate(self.sequence)}

    def find_motifs(self):
        return [(str(m.start() + 1)) for m in re.finditer('(?=[N][^P][S|T][^P])', self.sequence)]


def parse_file(param):
    with open(param) as f:
        protein_ids = f.read()
    return protein_ids.split()


def get_sequence(protein_id):
    try:
        response = requests.get(f'https://www.uniprot.org/uniprot/{protein_id}.fasta')
        response.raise_for_status()
    except HTTPError as e:
        print(f'Could not find protein for {protein_id} - returned following error {e}')
    return response.text


if __name__ == '__main__':
    protein_ids = parse_file('test2.txt')
    for protein in protein_ids:
        sequence = get_sequence(protein)
        fasta_object = Fasta(sequence)
        matches = fasta_object.find_motifs()
        if matches:
            print(protein)
            print(' '.join(matches))
