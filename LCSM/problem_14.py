import pandas as pd

sample_dataset = """
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""


class Fasta:
    def __init__(self, sequnece):
        identifier, dna = sequnece.split('/', 1)
        dna = dna.replace("/", "")
        self.sequence = dna
        self.identifier = identifier
        self.sequence_length = len(self.sequence)
        self.kmers = set()

    def as_dict(self):
        return {i: j for i, j in enumerate(self.sequence)}

    def generate_kmer(self, kmer):
        kmers = set()
        for i in range(self.sequence_length):
            nkmer = self.sequence[i:i + kmer]
            if len(nkmer) == kmer:
                kmers.add(nkmer)
            self.kmers = kmers


with open('test3.txt') as f:
    fasta = f.read().splitlines()
fasta = "/".join(fasta)
fasta = fasta.split('>')
fasta = list(filter(None, fasta))
sequences = [Fasta(sequence) for sequence in fasta]

check = False
kmer_length = int(min([sequence.sequence_length for sequence in sequences]))

common_kmers = set()
while check is False:
    while not common_kmers:
        sequences[0].generate_kmer(kmer_length)
        sequences[1].generate_kmer(kmer_length)
        common_kmers = sequences[0].kmers - (sequences[0].kmers - sequences[1].kmers)
        if common_kmers:
            for sequence in sequences[2:]:
                sequence.generate_kmer(kmer_length)
                common_kmers = common_kmers - (common_kmers - sequence.kmers)
                if not common_kmers:
                    kmer_length -= 1
                    break
                if common_kmers:
                    if sequence == sequences[-1]:
                        check = True
                        break
        else:
            kmer_length -= 1
print(common_kmers)

# #df = pd.DataFrame([x.as_dict() for x in sequences])
# matching_kmers = []
# new_kmers = []
# kmer_length = min([sequence.sequence_length for sequence in sequences])
# new_index = 2
# index = 0
# while not matching_kmers:
#     kmers = sequences[index].generate_kmer(kmer_length)
#     for kmer in kmers:
#         if kmer in sequences[index+1].generate_kmer(kmer_length):
#             matching_kmers.append(kmer)
#         if matching_kmers:
#             new_kmers = sequences[index+new_index].generate_kmer(kmer_length)
#             for match_index,mkmer in enumerate(matching_kmers[:]):
#                 if mkmer not in new_kmers:
#                     matching_kmers.remove(match_index)
#
#                 if matching_kmers:
#
#         else:
#             kmer_length -=1
# print(matching_kmers)
#
# def match_kmers(sequence_one, sequence_two):
#     pass
#
# for index,sequence in enumerate(sequences):
#     sequence.generate_kmer(kmer_length)
#     next_sequence = sequences[index+1]
#     next_sequence.generate_kmer(kmer_length)
#     for kmer in sequence.kmers:
#         if kmer in next_sequence:
#             matching_kmers.append(kmer)
#     if matching_kmers:
#         next_sequence = sequences[index + 2].generate_kmer()
#         for new_index, mker in enumerate(matching_kmers[:]):
#             if mker not in next_sequence
#                 mkmer.
#
#
#
#
#     else:
#         kmer_length -=1


# for kmer in sequences[0].generate_kmer(2):
#     if kmer in sequences[1].generate_kmer(2):
#         matching_kmers.append(kmer)
# for mkmer in matching_kmers:
#     if mkmer in sequences[2].generate_kmer(2):
#         print(mkmer)
