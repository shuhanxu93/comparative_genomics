# -*- coding: utf-8 -*-
"""
This file builds the metagene from a given directory

It requires two arguments, the input folder and the output filename
"""

import os

path = os.getcwd()+'\clusters_aligned'

genome09 = []
genome17 = ''
genome49 = ''
genome51 = ''


for filename in os.listdir(path):
    print(filename)
    
    f = open(path+'/'+filename,'r')
    content = f.readlines()
    seqlist = []
    
    count = 0
    # Store multiple line sequences into one line.
    for line in content:
        if (line[0]=='>'):
            count += 1
            seq = ''
            print(count)
        else:
            line = line.rstrip('\n')
        if (line[0]!='>'):
            seq = seq + line  
        if (count%4 == 1):
            genome09.append(seq)
        if (count%4 == 2):
            genome17 = genome17+seq
        if (count%4 == 3):
            genome49 = genome49+seq
        if (count%4 == 0):
            genome51 = genome51+seq
        
    #genome09.extend(seqlist[0])
    #genome17.extend(seqlist[1])
    #genome49.extend(seqlist[2])
    #genome51.extend(seqlist[3])
