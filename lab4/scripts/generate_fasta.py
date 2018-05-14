import sys

cluster_file = sys.argv[1]
line_index = int(sys.argv[2])

with open(cluster_file, 'r') as filehandle:
    text = filehandle.read().splitlines()[line_index]

items = text.split()

for item in items:
    print('>' + item)
    filename = '../database/' + item[2:11] + '.pfa'
    with open(filename, 'r') as filehandle:
        text = filehandle.read().splitlines()
        index = text.index('>' + item) + 1
        text = text[index:]
        sequence = ''
        for line in text:
            if not line.startswith('>'):
                sequence += line
            else:
                break
        print(sequence)
