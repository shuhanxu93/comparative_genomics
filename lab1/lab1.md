# Comparative Genomics 2018
Practical 1: Basic Genome Analysis
Group 11
Shuhan Xu, Fuqi Xu, Milda Valiukonyte

## Exercise 1
1.
09.fa.txt: Escherichia coli
17.fa.txt: Streptomyces coelicolor
24.fa.txt: Saccharomyces cerevisiae
49.fa.txt: Rubrobacter xylanophilus
51.fa.txt: Spiribacter curvatus

2.
09.fa.txt: 5277676 bp
17.fa.txt: 8667507 bp
24.fa.txt: 1531933 bp
49.fa.txt: 3225748 bp
51.fa.txt: 1926631 bp

3.
09.fa.txt: 5358 genes
17.fa.txt: 7910 genes
24.fa.txt: 799 genes
49.fa.txt: 3257 genes
51.fa.txt: 1908 genes

4.
09.fa.txt: prokaryotic
17.fa.txt: prokaryotic
24.fa.txt: eukaryotic
49.fa.txt: prokaryotic
51.fa.txt: prokaryotic

## Exercise 2
1.
blastp: searches amino acid sequence against protein sequence database
blastn: searches nucleotide sequence against nucleotide sequence database
blastx: translates nucleotide sequence in all 6 reading frames and searches against protein database
tblastn: searches protein sequence against nucleotide sequence database translated in all 6 reading frames
tblastx: translates nucleotide sequence in all 6 reading frames and searches against nucleotide sequence database translated in all 6 reading frames.

2.
run blastp against refseq


3.
A protein family is a group of closely related homologs which perform the same function.
Protein families are then grouped into superfamily in which all members are homologs but may have different functions from one another.

3.1.
There is a superfamily for this protein.

3.2.
Ribosomal protein S5 domain 2-like superfamily
ref: http://supfam.org/SUPERFAMILY/cgi-bin/gene.cgi?genome=up;seqid=Q9CQN1

4.1
Similarity is a measure of relationship between aligned sequences based on the degree of identity or similarity of amino acids at the matched positions.

Homology means that sequences are similar in structure or sequence due to a common ancestry.

4.2
Homology is different from similarity. Homology comes from evolutionary relationship which may not be entirely evident from sequences, e.g. sequences which are distantly related may have low identity or similarity or sequences may be similar due to convergent evolution. Similarity is a quantitative method used to measure relationship between sequences based on alignment. Highly similar sequences with Evalue below a threshold are inferred to be homologous.

4.3
When we are performing BLAST search, we are looking for highly similar sequences. We assume that highly similar sequences with Evalues below a threshold are homologous.

5.
Max target sequences: 20 000
Expect threshold: 1

![Shuhan](/home/u2364/Downloads/2.png)

The taxonomic spread is extended to both eukaryote (464) and bacteria (291). However, this protein family is not represented in Archaea.

![Fuqi](/home/u2364/Downloads/1.png)

The taxonomic spread is extended to both bacteria (9436) and eukaryote(102). 
Ref:http://www.uniprot.org/uniprot/?query=family:%22heat+shock+protein+90+family%22#orgViewBy

No, no animalia kingdom.

6.1
The BLOSUM matrix is generated based on mutation information from highly conserved regions in sequences. And the PAM matrix is based on the substitution frequency of homologous protein sequences.
Ref: Zvelebil, Marketa J., and Jeremy O. Baum. Understanding bioinformatics. Garland Science, 2007.

6.2
PAM-N represents the substitution rate and the evolutionary distance. The larger N is, the lower the similarity is. For example, PAM 250 is used for sequences with around 20% similarities.

In BLOSUM, N represents the percentage identity between sequences,  the larger N is, the higher the similarity is. For example, BLOSUM 62 is used to compare sequences with 62% sequence similarities.

6.3
BLAST uses these substitution matrix to evaluate the aligning, measuring the favorably of the matches residue by residue. This way, we can calculate the score of different alignments and compare them.

7.1

8.1
E value stands for the probablitu that the similarity between sequences are by chance alone. A low E value indicates that the similarity is less likely to happen by chance, and the alignment is better.

8.2
 E = k*n*m*exp(-lamda*S)
k, S: constant depending on the model. n: the length of query,  m: the size of the sequence.

## Section 3
1.
A sequence search and alignment tool, searching/aligning sequence database for homologous sequences using HMM.

2.
Phmmer: searching for protein sequence against protein sequence database
Hmmscan: searching for protein sequence against profile-HMM database
Hmmsearch: protein alignment or do profile-HMM against protein sequence database
Jackhmmer: iterative search against protein sequence database

3.1
HMMER advantage: 
1.search in a certain taxonomy.  
2.Fast search in big database
3.presenting result according to taxonomy and domain. Better visualization method
About the algorithm: 
1.Gaps are weighted instead of calculating gap open and extend penalty.
2.Using position-specific probabilities instead of BLOSUM
(Ref:  https://doi.org/10.1093/nar/gkv397  https://doi.org/10.1093/nar/gkr367)

3.2
HMMER

3.3
Short sequences: BLAST
No taxonomy requirement: BLAST
Others: HMMER

## Excecise 4

