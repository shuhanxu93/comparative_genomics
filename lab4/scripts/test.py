with open('17_parsed', 'r') as filehandle:
    list_17 = filehandle.read().splitlines()
    list_17_tags = [line.split()[2] for line in list_17]

with open('49_parsed', 'r') as filehandle:
    list_49 = filehandle.read().splitlines()
    list_49_tags = [line.split()[2] for line in list_49]

with open('51_parsed', 'r') as filehandle:
    list_51 = filehandle.read().splitlines()
    list_51_tags = [line.split()[2] for line in list_51]

print(len(list_17_tags), len(list_49_tags), len(list_51_tags))
print(len(set(list_17_tags)), len(set(list_49_tags)), len(set(list_51_tags)))
