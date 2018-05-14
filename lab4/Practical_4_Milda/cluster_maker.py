import sys

filename_1 = sys.argv [1]
filename_2 = sys.argv [2]
filename_3 = sys.argv [3]
filename_4 = sys.argv [4]

orthologs_1 = open (filename_1, 'r')
orthologs_2 = open (filename_2, 'r')
orthologs_3 = open (filename_3, 'r')
orthologs_4 = open (filename_4, 'r')

orthologs_1 = orthologs_1.readlines()
orthologs_2 = orthologs_2.readlines()
orthologs_3 = orthologs_3.readlines()
orthologs_4 = orthologs_4.readlines()


list1 = list()
list2 = list ()
list3 = list ()
list4 = list ()

for item in orthologs_1:
    item2 = item.split(' ')
    list1.append(item2)
for item in orthologs_2:
    item2 = item.split(' ')
    list2.append(item2)
for item in orthologs_3:
    item2 = item.split(' ')
    list3.append(item2)
for item in orthologs_4:
    item2 = item.split(' ')
    list4.append(item2)

dict_1=dict()
dict_2=dict()
dict_3=dict()
dict_4=dict()
for x in list1:
    key = x[1]
    dict_1.setdefault(key,[])
    dict_1[key].append(x[3])
for x in list2:
    key = x[1]
    dict_2.setdefault(key,[])
    dict_2[key].append(x[3])
for x in list3:
    key = x[1]
    dict_3.setdefault(key,[])
    dict_3[key].append(x[3])
for x in list4:
    key = x[1]
    dict_4.setdefault(key,[])
    dict_4[key].append(x[3])

for x in dict_1.keys():
    value=dict_1[x]
    if x in dict_2.keys():
        new_value=dict_2[x]
        value.extend(new_value)
    if x in dict_3.keys():
        new_value=dict_3[x]
        value.extend(new_value)
    if x in dict_4.keys():
        new_value=dict_4[x]
        value.extend(new_value)

f= open ("clusters","w")
for key in dict_1.keys():
    value_list=dict_1[key]
    strip_list=[]
    for a in value_list:
        strip_list.append(a.strip('\n'))
    value_string=" ".join(strip_list)
    print (key, value_string, file=f)
