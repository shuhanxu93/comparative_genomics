import sys
import numpy as np
import collections
import pandas as pd

organisms = sys.argv[1:]

amino_acids = ['A', 'R', 'N', 'D', 'C', 'Q', 'E' ,'G', 'H', 'I', 'L', 'K', 'M',
               'F', 'P', 'S', 'T', 'W', 'Y', 'V']

diamino_acids = []
for amino_acid1 in amino_acids:
    for amino_acid2 in amino_acids:
        diamino_acids.append(amino_acid1 + amino_acid2)

amino_freq = np.zeros((len(organisms), len(amino_acids)))
diamino_freq = np.zeros((len(organisms), len(diamino_acids)))

for org_index in range(len(organisms)):
    with open(organisms[org_index], 'r') as filehandle:

        text = filehandle.read().splitlines()
        proteome = []
        for index, line in enumerate(text):
            if not line.startswith('>'):
                if text[index - 1].startswith('>'):
                    proteome.append(line)
                else:
                    proteome[-1] = proteome[-1] + line

        cat_sequence = ''.join(proteome)
        cnt = collections.Counter(cat_sequence)
        for amino_index in range(len(amino_acids)):
            amino_freq[org_index, amino_index] = cnt[amino_acids[amino_index]] / len(cat_sequence)

        diamino_list = []
        for sequence in proteome:
            for seq_index in range(len(sequence) - 1):
                diamino_list.append(sequence[seq_index : seq_index + 2])
        cnt = collections.Counter(diamino_list)
        for diamino_index in range(len(diamino_acids)):
            diamino_freq[org_index, diamino_index] = cnt[diamino_acids[diamino_index]] / (len(cat_sequence) - len(proteome))

df_amino_freq = pd.DataFrame(data=amino_freq, index=organisms, columns=amino_acids)
df_diamino_freq = pd.DataFrame(data=diamino_freq, index=organisms, columns=diamino_acids)

df_amino_freq.to_csv('amino_freq.csv', sep=',', encoding='utf-8')
df_diamino_freq.to_csv('diamino_freq.csv', sep=',', encoding='utf-8')
