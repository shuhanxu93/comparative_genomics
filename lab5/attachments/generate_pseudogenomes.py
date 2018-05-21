#! /usr/bin/env python
"prints first argument aa sequences of length second argument to screen"
import random
import sys

files = sys.argv[2:]

number=sys.argv[1]
length=20
aas="ARNDCEQGHILKMFPSTWYV"

def r20():
    return random.randrange(20)

alist = []
for i in range(number):
    s=""
    for j in range(length):
        s+=aas[r20()]
    alist.append(s)

adict = {index: value for index, value in enumerate(alist)}

with open('multiFastafile', 'w') as filehandle:
    for afile in files:
        filehandle.write('>' + afile[:2] + '\n')
        long_sequence = []
        with open(afile, 'r') as filehandle2:
            text = filehandle2.read().split()
            long_sequence = [adict[int(number)] for number in text]
            filehandle.write(''.join(long_sequence) + '\n')
