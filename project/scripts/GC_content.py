import sys

genome = sys.argv[1]

with open (genome, "r") as genome:
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

G_and_C=G+C
GC_content=G_and_C/length
   
# Dinucleotide frequencies #

dList = [genome[x:x+2] for x in range(length)]

all_dinucleotides = length-1

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


print (A_freq, C_freq, G_freq, T_freq, GC_content, AA, AC, AG, AT, CA, CC, CG, CT, GA, GC, GG, GT, TA, TC, TG, TT)