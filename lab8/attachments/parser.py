import sys

blastresults_file = sys.argv[1]
experiments_file = sys.argv[2]

pred = set()
with open(blastresults_file, 'r') as filehandle:
    for line in filehandle:
        pred.add(line.split()[1].split('|')[2].split('_')[0])

experiments = []
with open(experiments_file, 'r') as filehandle:
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
    print("number of overlaps:", overlaps[index], '\n')
