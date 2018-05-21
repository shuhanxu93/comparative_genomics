# Part of the script which generates a dictionary with random amino acid sequences assigned to numbers up to certain value
import random
import sys
number=int(sys.argv[1])
length=int(sys.argv[2])
aas="ARNDCEQGHILKMFPSTWYV"

my_dict={}

def r20():
    return random.randrange(20)
for i in range(number):
    s=""
    for j in range(length):
        s+=aas[r20()]
    my_dict[i]=s

# Part of the script which makes a list of gene order and assigns an amino acid sequence to each number

f=open("09_gene_order", "r")
lines=f.readlines()
order=[]
for line in lines:
    line=line.strip()
    order.append(int(line))
f.close()

f2=open("17_gene_order", "r")
lines2=f2.readlines()
order2=[]
for line in lines2:
    line=line.strip()
    order2.append(int(line))
f2.close()

f3=open("49_gene_order", "r")
lines3=f3.readlines()
order3=[]
for line in lines3:
    line=line.strip()
    order3.append(int(line))
f3.close()

f4=open("51_gene_order", "r")
lines4=f4.readlines()
order4=[]
for line in lines4:
    line=line.strip()
    order4.append(int(line))
f4.close()


string=""
for x in order:
    string=string+my_dict[x]
ff=open("long_sequence_09","w")
print (string, file=ff)
ff.close()

string2=""
for x in order2:
    string2=string2+my_dict[x]
ff2=open("long_sequence_17","w")
print (string2, file=ff2)
ff2.close()

string3=""
for x in order3:
    string3=string3+my_dict[x]
ff3=open("long_sequence_49","w")
print (string3, file=ff3)
ff3.close()

string4=""
for x in order4:
    string4=string4+my_dict[x]
ff4=open("long_sequence_51","w")
print (string4, file=ff4)
ff4.close()



