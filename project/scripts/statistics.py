import sys
import numpy as np
import collections

organisms = sys.argv[1:]

gc_freq = np.zeros(len(organisms))
for org_index in range(len(organisms)):
    with open(organisms[org_index], 'r') as filehandle:
        genome = filehandle.read().splitlines()[1]
        cnt = collections.Counter(genome)
        gc_freq[org_index] = (cnt['G'] + cnt ['C']) / len(genome)

nucleotides = ['A', 'C', 'G', 'T']
dinucleotides = []
for nucleotide1 in nucleotides:
    for nucleotide2 in nucleotides:
        dinucleotides.append(nucleotide1 + nucleotide2)

dinucl_freq = np.zeros((len(organisms), len(dinucleotides)))
for org_index in range(len(organisms)):
    with open(organisms[org_index], 'r') as filehandle:
        genome = filehandle.read().splitlines()[1]
        dinucl_list = []
        for gen_index in range(len(genome) - 1):
            dinucl_list.append(genome[gen_index : gen_index + 2])
        cnt = collections.Counter(dinucl_list)
        for dinucl_index in range(len(dinucleotides)):
            dinucl_freq[org_index, dinucl_index] = cnt[dinucleotides[dinucl_index]] / (len(genome) - 1)
