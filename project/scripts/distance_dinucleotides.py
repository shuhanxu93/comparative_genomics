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
    genome_name1 = text[0]
    genome1 = text [1]

with open(filename2) as filehandle2:
    text = filehandle2.read().splitlines()
    genome_name2 = text[0]
    genome2 = text [1]

with open(filename3) as filehandle3:
    text = filehandle3.read().splitlines()
    genome_name3 = text[0]
    genome3 = text [1]

with open(filename4) as filehandle4:
    text = filehandle4.read().splitlines()
    genome_name4 = text[0]
    genome4 = text [1]

with open(filename5) as filehandle5:
    text = filehandle5.read().splitlines()
    genome_name5 = text[0]
    genome5 = text [1]

# Dinucleotide frequencies #

all_frequencies=[]

def frequencies (genome):
    frequency_list=[]
    length = len(genome)
    dList = [genome[x:x+2] for x in range(length)]
    all_dinucleotides = length-1
    dinucleotides=[]
    AA = dList.count("AA")/all_dinucleotides
    AC = dList.count("AC")/all_dinucleotides
    AG = dList.count("AG")/all_dinucleotides
    AT = dList.count("AT")/all_dinucleotides
    CA = dList.count("CA")/all_dinucleotides
    CC = dList.count("CC")/all_dinucleotides
    CG = dList.count("CG")/all_dinucleotides
    CT = dList.count("CT")/all_dinucleotides
    GA = dList.count("GA")/all_dinucleotides
    GC = dList.count("GC")/all_dinucleotides
    GG = dList.count("GG")/all_dinucleotides
    GT = dList.count("GT")/all_dinucleotides
    TA = dList.count("TA")/all_dinucleotides
    TC = dList.count("TC")/all_dinucleotides
    TG = dList.count("TG")/all_dinucleotides
    TT = dList.count("TT")/all_dinucleotides
    frequency_list.append(AA)
    frequency_list.append(AC)
    frequency_list.append(AG)
    frequency_list.append(AT)
    frequency_list.append(CA)
    frequency_list.append(CC)
    frequency_list.append(CG)
    frequency_list.append(CT)
    frequency_list.append(GA)
    frequency_list.append(GC)
    frequency_list.append(GG)
    frequency_list.append(GT)
    frequency_list.append(TA)
    frequency_list.append(TC)
    frequency_list.append(TG)
    frequency_list.append(TT)
    all_frequencies.append(frequency_list)

frequencies(genome1)
frequencies(genome2)
frequencies(genome3)
frequencies(genome4)
frequencies(genome5)

arrays = np.asarray(all_frequencies)

D_12 = (arrays[0]-arrays[1])**2
D_13 = (arrays[0]-arrays[2])**2
D_14 = (arrays[0]-arrays[3])**2
D_15 = (arrays[0]-arrays[4])**2
D_23 = (arrays[1]-arrays[2])**2
D_24 = (arrays[1]-arrays[3])**2
D_25 = (arrays[1]-arrays[4])**2
D_34 = (arrays[2]-arrays[3])**2
D_35 = (arrays[2]-arrays[4])**2
D_45 = (arrays[3]-arrays[4])**2

D_12= math.sqrt(np.sum(D_12))
D_13= math.sqrt(np.sum(D_13))
D_14= math.sqrt(np.sum(D_14))
D_15= math.sqrt(np.sum(D_15))
D_23= math.sqrt(np.sum(D_23))
D_24= math.sqrt(np.sum(D_24))
D_25= math.sqrt(np.sum(D_25))
D_34= math.sqrt(np.sum(D_34))
D_35= math.sqrt(np.sum(D_35))
D_45= math.sqrt(np.sum(D_45))


# Distance matrix #

distances = [[0, D_12, D_13, D_14, D_15], [D_12, 0, D_23, D_24, D_25], [D_13, D_23, 0, D_34, D_35], [D_14, D_24, D_34, 0, D_45], [D_15, D_25, D_35, D_45, 0]]

genome_names = [genome_name1, genome_name2, genome_name3, genome_name4, genome_name5]
genome_names = [name.replace(">./","") for name in genome_names]

with open ("distances.txt","w") as f:
    names=" ".join(genome_names)
    print (names, file=f)
    for line in distances:
        string=""
        for x in line:
            x=str(x)
            string=string+x+" "
        print (string.strip(), file=f)

f.close()
