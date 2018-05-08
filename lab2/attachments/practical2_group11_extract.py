def separate(filename, protein_file, nucleotide_file):

    filehandle = open(filename, 'r')

    text = filehandle.read().splitlines()
    text = list(filter(None, text))

    filehandle.close()

    start_index = text.index('Predicted coding sequence(s):') + 1

    text = text[start_index:]

    protein = []
    nucleotide = []
    for line in text:
        if line.startswith('>'):
            if line.endswith('aa'):
                protein.append(line)
            else:
                nucleotide.append(line)
        elif line.isupper():
            protein.append(line)
        else:
            nucleotide.append(line)

    with open(protein_file, 'w') as protein_filehandle:
        for line in protein:
            protein_filehandle.write(line + '\n')

    with open(nucleotide_file, 'w') as nucleotide_filehandle:
        for line in nucleotide:
            nucleotide_filehandle.write(line + '\n')

if __name__ == '__main__':
    separate('24.out', 'predicted_protein_sequences.fasta', 'predicted_nucleotide_sequences.fasta')
