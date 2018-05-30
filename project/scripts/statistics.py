import sys
import numpy as np
import collections

organisms = sys.argv[1:]

gc_freq = np.zeros(len(organisms))
for index in range(len(organisms)):
    with open(organisms[index], 'r') as filehandle:
        genome = filehandle.read().splitlines()[1]
        cnt = collections.Counter(genome)
        gc_freq[index] = (cnt['G'] + cnt ['C']) / sum(cnt.values())

nucleotides = ['A', 'C', 'G', 'T']
dinucleotides = []
for nucleotide1 in nucleotides:
    for nucleotide2 in nucleotides:
        dinucleotides.append(nucleotide1 + nucleotide2)

dinucl_freq = np.zeros((len(organisms), len(dinucleotides)))
print(dinucl_freq)
