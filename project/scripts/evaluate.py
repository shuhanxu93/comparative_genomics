import sys

genome_file = sys.argv[1]
true_file = sys.argv[2]
pred_file = sys.argv[3]

with open(genome_file, 'r') as filehandle:
    genome = filehandle.read().splitlines()[1]

with open(true_file, 'r') as filehandle:
    true_orfs = filehandle.read().splitlines()[1:]

with open(pred_file, 'r') as filehandle:
    pred_orfs = filehandle.read().splitlines()[1:]

true_f1 = []
true_f2 = []
true_f3 = []
true_r1 = []
true_r2 = []
true_r3 = []
for orf in true_orfs:
    orfname, sbegin, send, rf, score = orf.split()
    sbegin = int(sbegin)
    send = int(send)
    rf = int(rf)
    if rf == 1:
        true_f1.append([sbegin, send])
    elif rf == 2:
        true_f2.append([sbegin, send])
    elif rf == 3:
        true_f3.append([sbegin, send])
    elif rf == -1:
        true_r1.append([send, sbegin])
    elif rf == -2:
        true_r2.append([send, sbegin])
    else:
        true_r3.append([send, sbegin])

pred_f1 = []
pred_f2 = []
pred_f3 = []
pred_r1 = []
pred_r2 = []
pred_r3 = []
for orf in pred_orfs:
    orfname, sbegin, send, rf, score = orf.split()
    sbegin = int(sbegin)
    send = int(send)
    rf = int(rf)
    if rf == 1:
        pred_f1.append([sbegin, send])
    elif rf == 2:
        pred_f2.append([sbegin, send])
    elif rf == 3:
        pred_f3.append([sbegin, send])
    elif rf == -1:
        pred_r1.append([send, sbegin])
    elif rf == -2:
        pred_r2.append([send, sbegin])
    else:
        pred_r3.append([send, sbegin])

TP = 0
TN = 0
FP = 0
FN = 0

intersection = []
true_index = 0
pred_index = 0
while true_index < len(true_f1) and pred_index < len(pred_f1):
    if true_f1[true_index][0] < pred_f1[pred_index][1] and true_f1[true_index][1] > pred_f1[pred_index][0]:
        intersection.append([max(true_f1[true_index][0], pred_f1[pred_index][0]), min(true_f1[true_index][1], pred_f1[pred_index][1])])
    if true_f1[true_index][1] < pred_f1[pred_index][1]:
        true_index += 1
    elif pred_f1[pred_index][1] < true_f1[true_index][1]:
        pred_index += 1
    else:
        true_index += 1
        pred_index += 1
