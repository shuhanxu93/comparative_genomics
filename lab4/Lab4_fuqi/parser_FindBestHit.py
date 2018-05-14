# -*- coding: utf-8 -*-
"""
Spyder Editor

This file searches for the best hit in parsed blast.xml file

The name of the output file is "best_hits_inputfile"
"""
import sys
parsedBlastResult = sys.argv [1]

with open(parsedBlastResult) as f1:
    lines = f1.readlines()
    hits = []
    for x in lines:
        hits.append(x.split())
    bestHits = []
    bestHits.append(hits[0])
    for i in range(len(hits)-1):
        temp = hits[i]
        if hits[i+1][0]!=temp[0]:
            bestHits.append(hits[i+1])
            
bestHitFile = "best_hits_"+str(parsedBlastResult)
with open(bestHitFile,'w+') as f2:
    for i in range(len(bestHits)): 
        for j in range(len(bestHits[i])):
            f2.write(str(bestHits[i][j]))
            f2.write(" ")
        f2.write('\n')
        
        