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

true_all = true_f1 + true_f2 + true_f3 + true_r1 + true_r2 + true_r3

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

pred_all = pred_f1 + pred_f2 + pred_f3 + pred_r1 + pred_r2 + pred_r3

intersection = []

def add_intersection(true_list, pred_list):

    combined_list = true_list + pred_list
    combined_list.sort()
    for index in range(len(combined_list) - 1):
        if combined_list[index][0] <= combined_list[index + 1][1] and combined_list[index][1] >= combined_list[index + 1][0]:
            intersection.append([max(combined_list[index][0], combined_list[index + 1][0]), min(combined_list[index][1], combined_list[index][1])])

add_intersection(true_f1, pred_f1)
add_intersection(true_f2, pred_f2)
add_intersection(true_f3, pred_f3)
add_intersection(true_r1, pred_r1)
add_intersection(true_r2, pred_r2)
add_intersection(true_r3, pred_r3)

intersection_len = 0
for coord in intersection:
    intersection_len += coord[1] - coord[0] + 1

true_len = 0
for coord in true_all:
    true_len += coord[1] - coord[0] + 1

pred_len = 0
for coord in pred_all:
    pred_len += coord[1] - coord[0] + 1

TP = intersection_len
FN = true_len - intersection_len
FP = pred_len - intersection_len
TN = 6 * len(genome) - TP - FN - FP

true_num = len(true_all)
pred_num = len(pred_all)
true_len_ave = true_len / true_num
pred_len_ave = pred_len / pred_num
Sn = TP / (TP + FN)
Sp = TP / (TP + FP)
ACP = 0.25 * (TP / (TP + FN) + TP / (TP + FP) + TN / (TN + FP) + TN / (TN + FN))
AC = 2 * ACP - 1

print("number of true orf:", true_num)
print("number of predicted orf:", pred_num)
print("average true length:", true_len_ave)
print("average predicted length:", pred_len_ave)
print("sensitivity:", Sn)
print("specificity:", Sp)
print("approximate correlation coefficient:", AC)
