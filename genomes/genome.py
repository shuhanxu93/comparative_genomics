from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

with open('09.fa.txt') as filehandle:
    genome = filehandle.read().splitlines()[1]

def complement(sequence):
    sequence_com = sequence.replace('A', 't').replace('C', 'g').replace('G', 'c').replace('T', 'a').upper()
    return sequence_com

test = genome[:]
f1_met = []
f2_met = []
f3_met = []
r1_met = []
r2_met = []
r3_met = []

f1_stop = [-3]
f2_stop = [-3]
f3_stop = [-3]
r1_stop = []
r2_stop = []
r3_stop = []

for coordinate in range(0, len(test), 3):
    codon = test[coordinate : coordinate + 3]
    if codon == 'ATG':
        f1_met.append(coordinate)
    if codon == 'CAT':
        r1_met.append(coordinate + 2)
    if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
        f1_stop.append(coordinate)
    if codon == 'TTA' or codon == 'CTA' or codon == 'TCA':
        r1_stop.append(coordinate + 2)

for coordinate in range(1, len(test), 3):
    codon = test[coordinate : coordinate + 3]
    if codon == 'ATG':
        f2_met.append(coordinate)
    if codon == 'CAT':
        r2_met.append(coordinate + 2)
    if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
        f2_stop.append(coordinate)
    if codon == 'TTA' or codon == 'CTA' or codon == 'TCA':
        r2_stop.append(coordinate + 2)

for coordinate in range(2, len(test), 3):
    codon = test[coordinate : coordinate + 3]
    if codon == 'ATG':
        f3_met.append(coordinate)
    if codon == 'CAT':
        r3_met.append(coordinate + 2)
    if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
        f3_stop.append(coordinate)
    if codon == 'TTA' or codon == 'CTA' or codon == 'TCA':
        r3_stop.append(coordinate + 2)

gene_list = []
for index in range(1, len(f1_stop)):
    stop_coord = f1_stop[index]
    prev_stop_coord = f1_stop[index - 1]
    if stop_coord - prev_stop_coord >= 113:
        for start_coord in f1_met:
            if start_coord > prev_stop_coord:
                if stop_coord - start_coord >= 110:
                    gene_list.append([start_coord, stop_coord + 2, 1])
                break

for index in range(1, len(f2_stop)):
    stop_coord = f2_stop[index]
    prev_stop_coord = f2_stop[index - 1]
    if stop_coord - prev_stop_coord >= 113:
        for start_coord in f2_met:
            if start_coord > prev_stop_coord:
                if stop_coord - start_coord >= 110:
                    gene_list.append([start_coord, stop_coord + 2, 2])
                break

for index in range(1, len(f3_stop)):
    stop_coord = f3_stop[index]
    prev_stop_coord = f3_stop[index - 1]
    if stop_coord - prev_stop_coord >= 113:
        for start_coord in f3_met:
            if start_coord > prev_stop_coord:
                if stop_coord - start_coord >= 110:
                    gene_list.append([start_coord, stop_coord + 2, 3])
                break

r1_stop.append(len(test) + 2)
for index in range(len(r1_stop) - 1):
    stop_coord = r1_stop[index]
    prev_stop_coord = r1_stop[index + 1]
    if prev_stop_coord - stop_coord >= 113:
        for start_coord in r1_met[::-1]:
            if start_coord < prev_stop_coord:
                if start_coord - stop_coord >= 110:
                    gene_list.append([stop_coord - 2, start_coord, -1])
                break

r2_stop.append(len(test) + 2)
for index in range(len(r2_stop) - 1):
    stop_coord = r2_stop[index]
    prev_stop_coord = r2_stop[index + 1]
    if prev_stop_coord - stop_coord >= 113:
        for start_coord in r2_met[::-1]:
            if start_coord < prev_stop_coord:
                if start_coord - stop_coord >= 110:
                    gene_list.append([stop_coord - 2, start_coord, -2])
                break

r3_stop.append(len(test) + 2)
for index in range(len(r3_stop) - 1):
    stop_coord = r3_stop[index]
    prev_stop_coord = r3_stop[index + 1]
    if prev_stop_coord - stop_coord >= 113:
        for start_coord in r3_met[::-1]:
            if start_coord < prev_stop_coord:
                if start_coord - stop_coord >= 110:
                    gene_list.append([stop_coord - 2, start_coord, -3])
                break

gene_list.sort()

new_gene_list = []
new_gene_list.append(gene_list[0])
for orf in gene_list[1:]:
    if new_gene_list[-1][1] - orf[0] + 1 <= 50:
        new_gene_list.append(orf)
    else:
        if orf[1] - orf[0] > new_gene_list[-1][1] -new_gene_list[-1][0]:
            del new_gene_list[-1]
            new_gene_list.append(orf)

print(len(new_gene_list))
    

'''
seq_record = SeqIO.parse('09.fa.txt', 'fasta').next()

outseqrecords = []
for index, orf in enumerate(gene_list):
    sbegin, send, rf = orf
    newseq = seq_record.seq[sbegin : send + 1]
    if rf < 0:
        newseq = newseq.reverse_complement()
    newseq = newseq.translate(stop_symbol='')
    name = '09.fa.txt_orf' + str(index + 1)
    if rf < 0:
        name = name + '_rev'
    outseqrecords.append(SeqRecord(newseq,
                                   id=name,
                                   description=''))    

SeqIO.write(outseqrecords, open('09_pred_prot', 'w'), 'fasta')
'''














