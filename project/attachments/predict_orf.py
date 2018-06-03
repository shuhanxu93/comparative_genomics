import sys

filename = sys.argv[1]
min_len = int(sys.argv[2])
max_overlap = int(sys.argv[3])

with open(filename) as filehandle:
    text = filehandle.read().splitlines()
    genome_name = text[0]
    genome = text[1]

genome_len = len(genome)

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

for coordinate in range(0, genome_len, 3):
    codon = genome[coordinate : coordinate + 3]
    if codon == 'ATG':
        f1_met.append(coordinate)
    if codon == 'CAT':
        r1_met.append(coordinate + 2)
    if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
        f1_stop.append(coordinate)
    if codon == 'TTA' or codon == 'CTA' or codon == 'TCA':
        r1_stop.append(coordinate + 2)

for coordinate in range(1, genome_len, 3):
    codon = genome[coordinate : coordinate + 3]
    if codon == 'ATG':
        f2_met.append(coordinate)
    if codon == 'CAT':
        r2_met.append(coordinate + 2)
    if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
        f2_stop.append(coordinate)
    if codon == 'TTA' or codon == 'CTA' or codon == 'TCA':
        r2_stop.append(coordinate + 2)

for coordinate in range(2, genome_len, 3):
    codon = genome[coordinate : coordinate + 3]
    if codon == 'ATG':
        f3_met.append(coordinate)
    if codon == 'CAT':
        r3_met.append(coordinate + 2)
    if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
        f3_stop.append(coordinate)
    if codon == 'TTA' or codon == 'CTA' or codon == 'TCA':
        r3_stop.append(coordinate + 2)

gene_list = []

f1_stop = [-3] + f1_stop#to consider beginning cases
for index in range(1, len(f1_stop)):
    stop_coord = f1_stop[index]
    prev_stop_coord = f1_stop[index - 1]
    if stop_coord - prev_stop_coord >= min_len + 3:
        for start_coord in f1_met:
            if start_coord > prev_stop_coord:
                if stop_coord - start_coord >= min_len:
                    gene_list.append([start_coord, stop_coord + 2, 1])
                break

f2_stop = [-3] + f2_stop#to consider beginning cases
for index in range(1, len(f2_stop)):
    stop_coord = f2_stop[index]
    prev_stop_coord = f2_stop[index - 1]
    if stop_coord - prev_stop_coord >= min_len + 3:
        for start_coord in f2_met:
            if start_coord > prev_stop_coord:
                if stop_coord - start_coord >= min_len:
                    gene_list.append([start_coord, stop_coord + 2, 2])
                break

f3_stop = [-3] + f3_stop#to consider beginning cases
for index in range(1, len(f3_stop)):
    stop_coord = f3_stop[index]
    prev_stop_coord = f3_stop[index - 1]
    if stop_coord - prev_stop_coord >= min_len + 3:
        for start_coord in f3_met:
            if start_coord > prev_stop_coord:
                if stop_coord - start_coord >= min_len:
                    gene_list.append([start_coord, stop_coord + 2, 3])
                break

r1_stop = r1_stop + [genome_len + 2]#to consider end cases
for index in range(len(r1_stop) - 1):
    stop_coord = r1_stop[index]
    prev_stop_coord = r1_stop[index + 1]
    if prev_stop_coord - stop_coord >= min_len + 3:
        for start_coord in r1_met[::-1]:
            if start_coord < prev_stop_coord:
                if start_coord - stop_coord >= min_len:
                    gene_list.append([stop_coord - 2, start_coord, -1])
                break

r2_stop = r2_stop + [genome_len + 2]#to consider end cases
for index in range(len(r2_stop) - 1):
    stop_coord = r2_stop[index]
    prev_stop_coord = r2_stop[index + 1]
    if prev_stop_coord - stop_coord >= min_len + 3:
        for start_coord in r2_met[::-1]:
            if start_coord < prev_stop_coord:
                if start_coord - stop_coord >= min_len:
                    gene_list.append([stop_coord - 2, start_coord, -2])
                break

r3_stop = r3_stop + [genome_len + 2]#to consider end cases
for index in range(len(r3_stop) - 1):
    stop_coord = r3_stop[index]
    prev_stop_coord = r3_stop[index + 1]
    if prev_stop_coord - stop_coord >= min_len + 3:
        for start_coord in r3_met[::-1]:
            if start_coord < prev_stop_coord:
                if start_coord - stop_coord >= min_len:
                    gene_list.append([stop_coord - 2, start_coord, -3])
                break

gene_list.sort()

def keep_longest(old_list):
    """keep longest non-overlapping orfs"""

    new_list = []
    temp_list = []
    new_list.append(old_list[0])
    for orf in old_list[1:]:
        if new_list[-1][1] - orf[0] + 1 <= max_overlap:
            new_list.append(orf)
        else:
            if orf[1] - orf[0] > new_list[-1][1] - new_list[-1][0]:
                temp_list.append(new_list[-1])
                del new_list[-1]
                new_list.append(orf)

    return new_list, temp_list

def remove_overlap(new_list, temp_list):
    """remove any orf from temp_list which overlaps with any orf from new_list"""

    new_temp_list = []
    for temp_orf in temp_list:
        for new_orf in new_list:
            if temp_orf[1] < new_orf[0]:
                new_temp_list.append(temp_orf)
                break
            elif temp_orf[0] <= new_orf[1]:
                if temp_orf[1] - new_orf[0] + 1 <= max_overlap:
                    new_temp_list.append(temp_orf)
                break
            else:
                pass

    return new_temp_list

new_gene_list, temp_gene_list = keep_longest(gene_list)#if gene_A overlaps gene_B which overlaps gene_C and len(gene_A) < len(gene_B) < len(gene_C), only gene_C is kept
temp_gene_list = remove_overlap(new_gene_list, temp_gene_list)#this step and the while loop below ensures that gene_A is also kept if gene_A does not overlap with gene_C
while len(temp_gene_list) > 0:
    old_gene_list = new_gene_list + temp_gene_list
    old_gene_list.sort()
    new_gene_list, temp_gene_list = keep_longest(old_gene_list)
    temp_gene_list = remove_overlap(new_gene_list, temp_gene_list)

with open(filename + '.predict', 'w') as filehandle:
    filehandle.write(genome_name + '\n')
    for number, orf in enumerate(new_gene_list, 1):
        if orf[2] > 0:
            filehandle.write('orf' + str(number) + ' ' + str(orf[0] + 1) + ' ' +
                             str(orf[1] + 1) + ' ' + '+' + str(orf[2]) + ' ' +
                             str(0) + '\n')
        else:
            filehandle.write('orf' + str(number) + ' ' + str(orf[1] + 1) + ' ' +
                             str(orf[0] + 1) + ' ' + str(orf[2]) + ' ' + str(0)
                             + '\n')
