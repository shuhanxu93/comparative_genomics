interactome = {}
with open('S.cerevisiae_subnetwork.tsv', 'r') as filehandle:
    text = filehandle.read().splitlines()
    for line in text[1:]:
        print(line.split('\t'))
        '''
        gene_1 = line.split('\t')[2]
        gene_2 = line.split('\t')[3]
        if gene_1 in interactome:
            interactome[gene_1] += 1
        else:
            interactome[gene_1] = 1
        if gene_2 in interactome:
            interactome[gene_2] += 1
        else:
            interactome[gene_2] = 1
print(interactome)
print(len(interactome))
'''
