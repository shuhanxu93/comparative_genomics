import sys

filename = sys.argv[1]

with open (filename, "r") as genome:
    genome=genome.readlines()
    genome=genome[1]

# Nucleotide frequencies #
    
G=genome.count("G")
C=genome.count("C")
A=genome.count("A")
T=genome.count("T")

length=len(genome)

A_freq=A/length
C_freq=C/length
G_freq=G/length
T_freq=T/length

# GC content #

f=open("GC_freq_%s" % filename,"w")
G_and_C=G+C
GC_content=G_and_C/length
print (GC_content, file=f)

# Dinucleotide frequencies #

dList = [genome[x:x+2] for x in range(length)]

dNumber = length-1

dinucleotides= ["AA", "AC", "AG", "AT", "CA", "CC", "CG", "CT", "GA", "GC", "GG", "GT", "TA", "TC", "TG", "TT"]

for x in dinucleotides:
    freq = dList.count(x)/dNumber
    print (freq, file=f)

f.close()
