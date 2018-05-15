# -*- coding: utf-8 -*-
"""
This file builds the metagene from a given directory

It requires two arguments, the input folder and the output filename
"""

import os

path = os.getcwd()+'\clusters_aligned'

genome09 = ''
genome17 = ''
genome49 = ''
genome51 = ''

def eachcluster(filename):
    seqAll = []
    f = open(path+'/'+filename,'r')
    content = f.readlines()
    # Add addtional sequence for later use
    content.append('>')
    
    # Getting the start point of each sequence
    seqStart = []
    for i,item in enumerate(content):
        if item.startswith('>'):
            seqStart.append(i)
          
    # Getting the line number of each sequence        
    for n in range(len(seqStart)-1):
        a = list(range(seqStart[n]+1,seqStart[n+1]))

        # Reading the multiple line sequence and write them into one line.
        seq =''
        for i, item in enumerate(content):
            if i in a:
                seq = seq+item.rstrip('\n')
        
        # Storing sequences in one cluster in one list
        seqAll.append(seq)   
    f.close()
    return seqAll

for filename in os.listdir(path):
    cluster = eachcluster(filename)
    genome09 = genome09 + cluster[0]
    genome17 = genome17 + cluster[1]
    genome49 = genome49 + cluster[2]
    genome51 = genome51 + cluster[3]

with open("metagene.fasta","w+") as g:
    g.write(">genome09\n")
    g.write(genome09)
    g.write('\n')
    g.write(">genome17\n")
    g.write(genome17)
    g.write('\n')
    g.write(">genome49\n")
    g.write(genome49)
    g.write('\n')
    g.write(">genome51\n")
    g.write(genome51)
    
    
    
    