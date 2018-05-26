import sys

filename = sys.argv[1]

interactome = {}
with open(filename, 'r') as filehandle:
    text = filehandle.read().splitlines()
    for line in text[1:]:
        gene_1 = line.split('\t')[0]
        gene_2 = line.split('\t')[1]
        if gene_1 in interactome:
            interactome[gene_1] += 1
        else:
            interactome[gene_1] = 1
        if gene_2 in interactome:
            interactome[gene_2] += 1
        else:
            interactome[gene_2] = 1
print(interactome)
print(sorted(list(interactome.values())))
