import sys
import gzip
import re

allNetwork = sys.argv[1]
taxaID1 = sys.argv[2]
taxaID2 = sys.argv[3]
taxaID3 = sys.argv[4]
taxaID4 = sys.argv[5]
taxaID5 = sys.argv[6]

with gzip.open(allNetwork,'r') as f,open('geno1','w') as g1,open('geno2','w') as g2,open('geno3','w') as g3,open('geno4','w') as g4,open('geno5','w') as g5:
    for line in f:
        pair = line.decode('utf8')
        pair = pair.split()
        
        if (pair[0].startswith(taxaID1)):
            for i in pair:
               g1.write(i)
               g1.write(' ')
            g1.write('\n')

        if (pair[0].startswith(taxaID2)):
            for i in pair:
               g2.write(i)
               g2.write(' ')
            g2.write('\n')

        if (pair[0].startswith(taxaID3)):
            for i in pair:
               g3.write(i)
               g3.write(' ')
            g3.write('\n')

        if (pair[0].startswith(taxaID4)):
            for i in pair:
               g4.write(i)
               g4.write(' ')
            g4.write('\n')

        if (pair[0].startswith(taxaID5)):
            for i in pair:
               g5.write(i)
               g5.write(' ')
            g5.write('\n')

'''
taxaID = [taxaID1,taxaID2,taxaID3,taxaID4,taxaID5]
for i in range(len(taxaID)):
    if (pair[0].startswith(taxaID[i])):
        filename = 'geno'+str(i)
        with open(filename,'w') as g:
            g.write(pair)
'''



    
