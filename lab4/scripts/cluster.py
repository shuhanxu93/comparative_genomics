with open('17_parsed', 'r') as filehandle:
    list_17 = filehandle.read().splitlines()
    list_17_tags = [[line.split()[0], line.split()[2]] for line in list_17]

with open('49_parsed', 'r') as filehandle:
    list_49 = filehandle.read().splitlines()
    list_49_tags = [[line.split()[0], line.split()[2]] for line in list_49]

with open('51_parsed', 'r') as filehandle:
    list_51 = filehandle.read().splitlines()
    list_51_tags = [[line.split()[0], line.split()[2]] for line in list_51]

combined = list_17_tags[:]

for i in list_49_tags:
    for index, j in enumerate(combined):
        if i[0] == j[0]:
            combined[index].append(i[1])
            break
    else:
        combined.append(i)
            
for i in list_51_tags:
    for index, j in enumerate(combined):
        if i[0] == j[0]:
            combined[index].append(i[1])
            break
    else:
        combined.append(i)

with open('cluster', 'w') as filehandle:
    for item in combined:
        filehandle.write(' '.join(item) + '\n')
