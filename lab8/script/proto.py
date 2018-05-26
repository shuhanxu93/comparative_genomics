import sys

filename = sys.argv[1]

interactome = {}
evidence = {'neighborhood_on_chromosome': 0, 'gene_fusion': 0,
            'phylogenetic_cooccurrence': 0, 'homology': 0, 'coexpression': 0,
            'experimentally_determined_interaction': 0,
            'database_annotated': 0, 'automated_textmining': 0}
with open(filename, 'r') as filehandle:
    text = filehandle.read().splitlines()
    for line in text[1:]:
        alist = line.split()[6:-1]
        if float(alist[0]) >= 0.9:
            evidence['neighborhood_on_chromosome'] += 1
        if float(alist[1]) >= 0.9:
            evidence['gene_fusion'] += 1
        if float(alist[2]) >= 0.9:
            evidence['phylogenetic_cooccurrence'] += 1
        if float(alist[3]) >= 0.9:
            evidence['homology'] += 1
        if float(alist[4]) >= 0.9:
            evidence['coexpression'] += 1
        if float(alist[5]) >= 0.9:
            evidence['experimentally_determined_interaction'] += 1
        if float(alist[6]) >= 0.9:
            evidence['database_annotated'] += 1
        if float(alist[7]) >= 0.9:
            evidence['automated_textmining'] += 1

print(evidence)
'''
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
'''
