import sys

setsFile = sys.argv[1]
speciesFile = sys.argv[2]
outFile = sys.argv[3]

with open(setsFile) as f1, open(speciesFile) as f2,open(outFile,'w') as f3:
    geneList = f2.read().splitlines() 
    maxCount = 0
    maxSet = []

    # Find the max number of overlapping genes
    for line in f1:
        count = 0
        for item in line.split():
            if item in geneList:
                count = count+1
        if count >= maxCount:
           maxCount = count 
           maxSet = line
        
        # This could be improved
        # I went through the database and found maxCount =5 first
        if count ==5:
           f3.write(line)
    
    '''
    for line in f1:
        count = 0
        for item in line.split():
            if item in geneList:
                count = count+1
                print(count)
        if count == maxCount:
           print('yes')
           #maxCount = count 
           maxSet = line
           print(line)
     '''
           