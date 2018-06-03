import sys
import matplotlib.pyplot as plt

inFile = sys.argv[1]
inFile2 = sys.argv[2]

with open(inFile) as f1:
    lengths = []
    lines = f1.readlines()[1:]
    for line in lines:
        length = abs(int(line.split()[1])-int(line.split()[2]))
        lengths.append(length)

with open(inFile2) as f2:
    lengths2 = []
    lines2 = f2.readlines()[1:]
    for line2 in lines2:
        length2 = abs(int(line2.split()[1])-int(line2.split()[2]))
        lengths2.append(length2)

    #size = plt.hist()
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.hist(lengths,bins=50)
ax1.set_title(str(inFile))
ax1.set_xlabel('size')
ax1.set_ylabel('frequency')
ax1.set_xlim([0, 5000])
ax2.hist(lengths2,bins=50)
ax2.set_title(str(inFile2))
ax2.set_xlabel('size')
ax2.set_ylabel('frequency')
ax2.set_xlim([0, 5000])
plt.show()
    
    