import sys
import re

inFile = sys.argv[1]
outFile = sys.argv[2]

with open(inFile) as f1, open(outFile,'w') as f2:
    for line in f1:
        if line.startswith('#'):
            pass
        else:
           genes = line.split()[1].split('|')[2].split('_')[0]
           f2.write(genes)
           f2.write('\n')

