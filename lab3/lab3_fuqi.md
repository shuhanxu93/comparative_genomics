# Exercise 1
There are 3 complete bacterial genomes in our sampels, 09,49,51

## DNA Tree Reconstruction

1. 
Firstly, we parse the sequence data into binary files and prepare them for blast by building a blast database.

makeblastdb -in <inputfile.fa> -dbtype nucl

-in: a flag indicating the input file

<inputfile.fa>: the name of the input file

-dbtype: a flag indicateing the molecule type of the input file

nucl: the input file are nucleoc acid sequences.

2. 
# what is the purpose of this step

3. 
3.1?

3.2
I used the blastResultParser.py file to extract the first hit in the blast result and used it as the 16sRNA files.

3.2.1
blastn -outfmt 5 -query <query file.fa> -db <database file.fa> -out <outputfile>

-outfmt : the output file uses XML BLAST output format.
https://www.biostars.org/p/88944/

-query <query file.fa> : the query we are going to blast with

-db <database file.fa>: the database to blast agains

-out <outputfile>: the name of the blast output.

Besides, we also used some default parameters:

-gapopen 0 : the gap open penalty is 0

-gapextend 0: the gap extend penalty is 0

      <Parameters_expect>10</Parameters_expect>
      <Parameters_sc-match>1</Parameters_sc-match>
      <Parameters_sc-mismatch>-2</Parameters_sc-mismatch>
      <Parameters_gap-open>0</Parameters_gap-open>
      <Parameters_gap-extend>0</Parameters_gap-extend>
      <Parameters_filter>L;m;</Parameters_filter>

3.2.2 
The output file contains detailed information of the blast search and the blast result. It includes infomation about the query, the dataset and the parameters we used. Several high score hits are also listed with their scores, the sequence of the hit and the alignment details.

# Exercise 2

B

a. 
Firstly, it build a iteractor blast record storing all alignment hit infomation. For every element in the iteractor, it contains the discription of the sequence and the alignment result. Then, it locates the first hit and returns the name and the aligned sequence in fasta format.

b. 
A Blast record stores the information of all hits the blast returns. It stores data in a 'dataframe' like format, in which every element can be searched and operated using index. And every element contains similar data structure. Differents hits are the elements in the record and each hit contains alignment, sequence and discription infomation.

c.
It assumes that the first hsp is the single best BLAST result.

d.
The script printes the first hit in the blast in fasta format, including the name of the hit and its aligned sequence.

## Exercise 3
We used a file containing all resulting sequeneces to make a multiple alignment.

1.1
Gaps are unfavorable in alignment, so when we introduce a gap, we need to decrease the alignment score accordingly, which is called gap penalty. Gap penalty includes two major parts: gap open penalty and gap extend penalty. Gap open penalty is the cost to introduce a new gap. Gap extension is the cost to enlong the existing gap. Also, if the gap locates at the beginning or the end of the alignment, which is more unfavorable, termial gap penalty should be included. Bonus score is added to every pair of aligned residues.

In our alignment, KALIGN gap open score = 217, gap extension score =39.40000153, terminal gap score = 292.60000610 , bonus score = 283. The alignment with the highest score would be the best alignment.

1.2?

## Exercise 4
1. 


 



