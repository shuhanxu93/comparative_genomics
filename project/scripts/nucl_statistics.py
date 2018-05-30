import sys
import numpy as np
import collections
import pandas as pd

organisms = sys.argv[1:]

nucleotides = ['A', 'C', 'G', 'T']

dinucleotides = []
for nucleotide1 in nucleotides:
    for nucleotide2 in nucleotides:
        dinucleotides.append(nucleotide1 + nucleotide2)

gc_freq = np.zeros(len(organisms))
nucl_freq = np.zeros((len(organisms), len(nucleotides)))
dinucl_freq = np.zeros((len(organisms), len(dinucleotides)))
for org_index in range(len(organisms)):
    with open(organisms[org_index], 'r') as filehandle:
        genome = filehandle.read().splitlines()[1]
        cnt = collections.Counter(genome)

        gc_freq[org_index] = (cnt['G'] + cnt ['C']) / len(genome)

        for nucl_index in range(len(nucleotides)):
            nucl_freq[org_index, nucl_index] = cnt[nucleotides[nucl_index]] / len(genome)

        dinucl_list = []
        for gen_index in range(len(genome) - 1):
            dinucl_list.append(genome[gen_index : gen_index + 2])
        cnt = collections.Counter(dinucl_list)
        for dinucl_index in range(len(dinucleotides)):
            dinucl_freq[org_index, dinucl_index] = cnt[dinucleotides[dinucl_index]] / (len(genome) - 1)

df_gc_freq = pd.DataFrame(data=gc_freq, index=organisms, columns=['GC'])
df_nucl_freq = pd.DataFrame(data=nucl_freq, index=organisms, columns=nucleotides)
df_dinucl_freq = pd.DataFrame(data=dinucl_freq, index=organisms, columns=dinucleotides)

df_gc_freq.to_csv('gc_frequency.csv', sep=',', encoding='utf-8')
df_nucl_freq.to_csv('nucleotide_frequency.csv', sep=',', encoding='utf-8')
df_dinucl_freq.to_csv('dinucleotide_frequency.csv', sep=',', encoding='utf-8')
