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

# GC content #

length1=len(genome1)
G1=genome1.count("G")
C1=genome1.count("C")
G_and_C_1=G1+C1
GC_content_1=G_and_C_1/length1

length2=len(genome2)
G2=genome2.count("G")
C2=genome2.count("C")
G_and_C_2=G2+C2
GC_content_2=G_and_C_2/length2

length3=len(genome3)
G3=genome3.count("G")
C3=genome3.count("C")
G_and_C_3=G3+C3
GC_content_3=G_and_C_3/length3

length4=len(genome4)
G4=genome4.count("G")
C4=genome4.count("C")
G_and_C_4=G4+C4
GC_content_4=G_and_C_4/length4

length5=len(genome5)
G5=genome5.count("G")
C5=genome5.count("C")
G_and_C_5=G5+C5
GC_content_5=G_and_C_5/length5

# Distances #

D_12 = math.sqrt ((GC_content_1 - GC_content_2)**2)

D_13 = math.sqrt ((GC_content_1 - GC_content_3)**2)

D_14 = math.sqrt ((GC_content_1 - GC_content_4)**2)

D_15 = math.sqrt ((GC_content_1 - GC_content_5)**2)

D_23 = math.sqrt ((GC_content_2 - GC_content_3)**2)

D_24 = math.sqrt ((GC_content_2 - GC_content_4)**2)

D_25 = math.sqrt ((GC_content_2 - GC_content_5)**2)

D_34 = math.sqrt ((GC_content_3 - GC_content_4)**2)

D_35 = math.sqrt ((GC_content_3 - GC_content_5)**2)

D_45 = math.sqrt ((GC_content_4 - GC_content_5)**2)

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
