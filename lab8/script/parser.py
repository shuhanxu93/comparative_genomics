pred = set()
with open('../data/blastresults.txt', 'r') as filehandle:
    for line in filehandle:
        pred.add(line.split()[1].split('|')[2].split('_')[0])

experiments = []
with open('../data/experiments.txt', 'r') as filehandle:
    for line in filehandle:
        exp = set(line.split())
        if bool(exp):
            experiments.append(exp)

overlaps = []
for exp in experiments:
    overlaps.append(len(pred & exp))

top = sorted(range(len(overlaps)), key=lambda x: overlaps[x])[::-1]
for index in top[:2]:
    print(*experiments[index])
