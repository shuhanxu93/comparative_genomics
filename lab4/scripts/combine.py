concatenated_alignment = ['>','','>','','>','','>','']
for i in range(1,11):
    filename = 'cluster_' + str(i) + '_aligned'
    with open(filename, 'r') as filehandle:
        text = filehandle.read().splitlines()
        alignment = []
        for index, line in enumerate(text):
            if line.startswith('>'):
                alignment.append(line[1:] + '_')
            else:
                if text[index - 1].startswith('>'):
                    alignment.append(line)
                else:
                    alignment[-1] = alignment[-1] + line
        for index in range(len(concatenated_alignment[:])):
            concatenated_alignment[index] = concatenated_alignment[index] + alignment[index]

with open('metagene_aligned', 'w') as filehandle:
    for line in concatenated_alignment:
        filehandle.write(line + '\n')
