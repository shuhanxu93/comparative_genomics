gene_list = [[1, 100], [2,200], [101,400], [210, 600], [500, 1000]]
#gene_list = [[1, 101], [2,200], [101,400]]

def keep_longest(old_list):
    """keep longest non-overlapping orfs"""

    new_list = []
    temp_list = []
    new_list.append(old_list[0])
    for orf in old_list[1:]:
        if new_list[-1][1] - orf[0] + 1 <= 50:
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
                if temp_orf[1] - new_orf[0] + 1 <= 50:
                    new_temp_list.append(temp_orf)
                break
            else:
                pass

    return new_temp_list

new_gene_list, temp_gene_list = keep_longest(gene_list)
print('new_gene_list', new_gene_list)
print('temp_gene_list', temp_gene_list)
temp_gene_list = remove_overlap(new_gene_list, temp_gene_list)
print('temp_gene_list', temp_gene_list)
while len(temp_gene_list) > 0:
    old_gene_list = new_gene_list + temp_gene_list
    old_gene_list.sort()
    new_gene_list, temp_gene_list = keep_longest(old_gene_list)
    temp_gene_list = remove_overlap(new_gene_list, temp_gene_list)

print('new_gene_list', new_gene_list)
