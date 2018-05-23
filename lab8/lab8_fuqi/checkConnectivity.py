import sys
import re
import math 
import numpy as np
import matplotlib.pyplot as plt

inFile = sys.argv[1]

interNum = 0 
with open(inFile,'r') as f:
    uniqueGenes = set()
    allGenes = []
    allInter = []

    for line in f:
        gene = re.match(r'\d+.(\w+)',line)
        # Storing all interactions
        allGenes.append(gene.group(1))

        # Storing the unique proteins
        uniqueGenes.add(gene.group(1))

        # Count how many lines to calculate average connectivity
        if line !='\n':
            interNum = interNum + 1
    
    # Calculating the average connectivity
    geneNum = len(uniqueGenes)
    averConnect = interNum/geneNum
    print(averConnect)

    # For each protein, count the iteractions it has.
    for i in uniqueGenes:
        perInter= allGenes.count(i)
        allInter.append(perInter)

    # Count the frequency of one node degree appears
    allFreq = []
    # The x-axis
    nodes = list(set(allInter))
    # The y-axis
    for i in nodes:
        frequency = allInter.count(i) 
        allFreq.append(frequency)
    for i in allFreq:
        i = math.log10(i)

    # Plotting
    fig = plt.scatter(nodes, allFreq,color='c')
    plt.xlim(xmin=-5)
    # Mark the average connectivity
    plt.axvline(x=averConnect,color='k', linestyle='--',label='average connectivity')
    #plt.text(averConnect,30,label='average connectivity',rotation=90,color='k')
    plt.title('degree distribution_'+str(inFile))
    plt.xlabel('node degree')
    plt.ylabel('frequency_log10')
    plt.show()


    

