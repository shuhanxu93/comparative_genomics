#! /usr/bin/env python
"prints first argument aa sequences of length second argument to screen"
import random
import sys

files = sys.argv[1:]


number=5322
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

for afile in files:
    with open(afile, 'r') as filehandle:
        text = filehandle.read().split()
        print(len(text))
