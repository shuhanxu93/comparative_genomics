import sys

inFile1 = sys.argv[1]
inFile2 = sys.argv[2]

#threshold = 10**-3
with open(inFile1) as f:
    pairs = []
    hits = f.readlines()
    for lines in hits:
            pairs.append([lines.split()[0],lines.split()[1]])
    
    forward = set()
    for i in pairs:
        forward.add((i[0],i[1]))
    print("size of " + str(inFile1) +'\n'+str(len(set(forward))))

with open(inFile2) as f:
    pairs_rev = []
    hits = f.readlines()
    for lines in hits:
            pairs_rev.append([lines.split()[1],lines.split()[0]])
    
    rev = set()
    for i in pairs:
        rev.add((i[0],i[1]))
    print("size of " + str(inFile2) +'\n'+str(len(set(forward))))
    
print("size of intersection of " + str(inFile1) +'\n'+str(len(set(forward).intersection(rev))))

