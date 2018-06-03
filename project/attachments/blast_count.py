import sys

inFile1 = sys.argv[1]
inFile2 = sys.argv[2]

#threshold = 10**-3
with open(inFile1) as f1:
    pairs = []
    hits = f1.readlines()
    for lines in hits:
            pairs.append([lines.split()[0],lines.split()[1]])

with open(inFile2) as f2:
    pairs_rev = []
    hits2 = f2.readlines()
    for lines in hits2:
            pairs_rev.append([lines.split()[1],lines.split()[0]])

count = 0    
for i in pairs:
    if i in pairs_rev:
        count = count+1

print("size of intersection of " + str(inFile1) +'\n'+str(count))

