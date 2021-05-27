import numpy as np
from collections import Counter, defaultdict
import pandas as pd

# with open('test.txt') as f:
with open('rosalind_cons.txt') as f:
    fasta = f.read().split('\n')

sequence_fasta = []
sequnce = ''
for line in fasta:
    if not line.startswith('>'):
        sequnce = sequnce + line
    else:
        if sequnce:
            sequence_fasta.append(list(sequnce))
            sequnce = ''
sequence_fasta.append(list(sequnce))

a = np.array(sequence_fasta, dtype=str)
num_rows, num_cols = a.shape
common_sequence = []
all_dict = []
for i in range(num_cols):
    common_sequence.append((Counter(a[:, i]).most_common(n=1))[0][0])
    counts = defaultdict(int)
    for j in a[:, i]:
        if j == 'A':
            counts[j] += 1
        if j == 'T':
            counts[j] += 1
        if j == 'G':
            counts[j] += 1
        if j == 'C':
            counts[j] += 1
    for key in ('A', 'G', 'C', 'T'):
        if key not in counts.keys():
            counts[key] = 0
    all_dict.append(counts)

df = pd.DataFrame.from_dict(all_dict)
with open('./output.txt', 'w') as fw:
    fw.write(''.join(common_sequence))
    fw.write('\n')
    fw.write(df.set_index('A').T.to_string())

print(''.join(common_sequence))
# df.drop(df.columns[[0]], axis=1, inplace=True)
print(df.set_index('A').T)

df.index.names = ['']
