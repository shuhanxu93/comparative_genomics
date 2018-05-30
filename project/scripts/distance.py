import sys
import math
import numpy as np

filename1 = sys.argv[1]
filename2 = sys.argv[2]
filename3 = sys.argv[3]
filename4 = sys.argv[4]
filename5 = sys.argv[5]

with open(filename1) as filehandle1:
    text = filehandle1.read().splitlines()
    GC_content_1=text[0]
    frequencies_1=[text[1],text[2],text[3],text[4],text[5],text[6],text[7],text[8],text[9],text[10],text[11],text[12],text[13],text[14],text[15]]
    frequencies_1=np.array(frequencies_1, dtype="float")

with open(filename2) as filehandle2:
    text = filehandle2.read().splitlines()
    GC_content_2=text[0]
    frequencies_2=[text[1],text[2],text[3],text[4],text[5],text[6],text[7],text[8],text[9],text[10],text[11],text[12],text[13],text[14],text[15]]
    frequencies_2=np.array(frequencies_2,dtype="float")

with open(filename3) as filehandle3:
    text = filehandle3.read().splitlines()
    GC_content_3=text[0]
    frequencies_3=[text[1],text[2],text[3],text[4],text[5],text[6],text[7],text[8],text[9],text[10],text[11],text[12],text[13],text[14],text[15]]
    frequencies_3=np.array(frequencies_3,dtype="float")

with open(filename4) as filehandle4:
    text = filehandle4.read().splitlines()
    GC_content_4=text[0]
    frequencies_4=[text[1],text[2],text[3],text[4],text[5],text[6],text[7],text[8],text[9],text[10],text[11],text[12],text[13],text[14],text[15]]
    frequencies_4=np.array(frequencies_4, dtype="float")

with open(filename5) as filehandle5:
    text = filehandle5.read().splitlines()
    GC_content_5=text[0]
    frequencies_5=[text[1],text[2],text[3],text[4],text[5],text[6],text[7],text[8],text[9],text[10],text[11],text[12],text[13],text[14],text[15]]
    frequencies_5=np.array(frequencies_5, dtype="float")


# Distances GC content #

D_12_GC = math.sqrt ((float(GC_content_1) - float(GC_content_2))**2)

D_13_GC = math.sqrt ((float(GC_content_1) - float(GC_content_3))**2)

D_14_GC = math.sqrt ((float(GC_content_1) - float(GC_content_4))**2)

D_15_GC = math.sqrt ((float(GC_content_1) - float(GC_content_5))**2)

D_23_GC = math.sqrt ((float(GC_content_2) - float(GC_content_3))**2)

D_24_GC = math.sqrt ((float(GC_content_2) - float(GC_content_4))**2)

D_25_GC = math.sqrt ((float(GC_content_2) - float(GC_content_5))**2)

D_34_GC = math.sqrt ((float(GC_content_3) - float(GC_content_4))**2)

D_35_GC = math.sqrt ((float(GC_content_3) - float(GC_content_5))**2)

D_45_GC = math.sqrt ((float(GC_content_4) - float(GC_content_5))**2)


# Distances dinucleotides #

D_12_dd= math.sqrt(np.sum((frequencies_1-frequencies_2)**2))

D_13_dd= math.sqrt(np.sum((frequencies_1-frequencies_3)**2))

D_14_dd= math.sqrt(np.sum((frequencies_1-frequencies_4)**2))

D_15_dd= math.sqrt(np.sum((frequencies_1-frequencies_5)**2))

D_23_dd= math.sqrt(np.sum((frequencies_2-frequencies_3)**2))

D_24_dd= math.sqrt(np.sum((frequencies_2-frequencies_4)**2))

D_25_dd= math.sqrt(np.sum((frequencies_2-frequencies_5)**2))

D_34_dd= math.sqrt(np.sum((frequencies_3-frequencies_4)**2))

D_35_dd= math.sqrt(np.sum((frequencies_3-frequencies_5)**2))

D_45_dd= math.sqrt(np.sum((frequencies_4-frequencies_5)**2))


# Distance matrix #

distances_GC = [[0, D_12_GC, D_13_GC, D_14_GC, D_15_GC], [D_12_GC, 0, D_23_GC, D_24_GC, D_25_GC], [D_13_GC, D_23_GC, 0, D_34_GC, D_35_GC], [D_14_GC, D_24_GC, D_34_GC, 0, D_45_GC], [D_15_GC, D_25_GC, D_35_GC, D_45_GC, 0]]

distances_dd = [[0, D_12_dd, D_13_dd, D_14_dd, D_15_dd], [D_12_dd, 0, D_23_dd, D_24_dd, D_25_dd], [D_13_dd, D_23_dd, 0, D_34_dd, D_35_dd], [D_14_dd, D_24_dd, D_34_dd, 0, D_45_dd], [D_15_dd, D_25_dd, D_35_dd, D_45_dd, 0]]

genome_names = [filename1, filename2, filename3, filename4, filename5]
genome_names = [name.replace("GC_freq_","") for name in genome_names]

with open ("distances_GC.txt","w") as f1:
    names=" ".join(genome_names)
    print (names, file=f1)
    for line in distances_GC:
        string=""
        for x in line:
            x=x*100
            x=str(x)
            string=string+x+" "
        print (string.strip(), file=f1)

f1.close()

with open ("distances_dd.txt","w") as f2:
    names=" ".join(genome_names)
    print (names, file=f2)
    for line in distances_dd:
        string=""
        for x in line:
            x=x*100
            x=str(x)
            string=string+x+" "
        print (string.strip(), file=f2)

f2.close()
