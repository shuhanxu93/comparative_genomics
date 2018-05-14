# -*- coding: utf-8 -*-
"""
This file searches for the shared sequence in all genomes

and returns multiple files, each containing one ortholog in all genomes in FASTA format

"""
import sys

genome1result = sys.argv [1]
genome2result = sys.argv [2]
genome3result = sys.argv [3]

with open(genome1result) as f1:
    with open(genome2result) as f2:   
        with open(genome3result) as f3:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
            lines3 = f3.readlines()
            hits1,hits2,hits3 = [],[],[]
            for x in lines1:
                hits1.append(x.split(' '))
            for x in lines2:
                hits2.append(x.split(' '))
            for x in lines3:
                hits3.append(x.split(' '))

for i in range(len(hits1)):
    search = hits1[i][0]
    for j in range(len(hits2)):
        if search == hits2[j][0]:
           for k in range(len(hits3)):
               if search == hits3[k][0]: 
                   filename = "cluster"+str(i)
                   with open(filename,'w+') as f:
                       f.write(hits1[i][0]+'\n'+hits1[i][1]+'\n'+hits1[i][2]+
                               '\n'+hits1[i][3]+'\n'+hits2[j][2]+'\n'+hits2[j][3]+
                               '\n'+hits3[k][2]+'\n'+hits3[k][3])
    