import sys
import numpy as np
import pandas as pd

filename = sys.argv[1]

df = pd.read_csv(filename, sep=',', encoding='utf-8')

organisms = df.values[:,0]
data = df.values[:,1:]

distances = np.zeros((len(organisms), len(organisms)))
for i in range(len(organisms)):
    for j in range(len(organisms)):
        distances[i, j] = np.sqrt(np.sum((data[i] - data[j]) ** 2))

print(' '.join(map(str, organisms)))
for row in distances:
    print(' '.join(map(str, row)))
