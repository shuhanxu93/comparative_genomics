
with open('09.fa.txt') as filehandle:
    genome = filehandle.read().splitlines()[1]

def complement(sequence):
    sequence_com = sequence.replace('A', 't').replace('C', 'g').replace('G', 'c').replace('T', 'a').upper()
    return sequence_com

test = genome[:10000]
f1_met = []
f2_met = []
f3_met = []
r1_met = []
r2_met = []
r3_met = []

f1_stop = []
f2_stop = []
f3_stop = []
r1_stop = []
r2_stop = []
r3_stop = []

for index in range(0, len(test), 3):
    codon = test[index : index + 3]
    if codon == 'ATG':
        f1_met.append(index)
    if codon == 'TAC':
        r1_met.append(index + 2)
    if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
        f1_stop.append(index)
    if codon == 'ATT' or codon == 'ATC' or codon == 'ACT':
        r1_stop.append(index + 2)

for index in range(1, len(test), 3):
    codon = test[index : index + 3]
    if codon == 'ATG':
        f2_met.append(index)
    if codon == 'TAC':
        r2_met.append(index + 2)
    if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
        f2_stop.append(index)
    if codon == 'ATT' or codon == 'ATC' or codon == 'ACT':
        r2_stop.append(index + 2)

for index in range(2, len(test), 3):
    codon = test[index : index + 3]
    if codon == 'ATG':
        f3_met.append(index)
    if codon == 'TAC':
        r3_met.append(index + 2)
    if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
        f3_stop.append(index)
    if codon == 'ATT' or codon == 'ATC' or codon == 'ACT':
        r3_stop.append(index + 2)

glist_1 = []
for index in range(len(f1_stop) - 1):
    if f1_stop[index + 1] - f1_stop[index] >= 113:
        for coordinate in f1_met:
            if coordinate > f1_stop[index] and coordinate < f1_stop[index + 1]:
                if f1_stop[index + 1] - coordinate >= 113:
                    glist_1.append([coordinate, f1_stop[index + 1]])
                    break
                if coordinate > f1_stop[index + 1]:
                    break
print(glist_1)
