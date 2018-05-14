# this script takes the output of a blast run
# and outputs a fasta file with the best hit
# to the query in all database files where there is a hit
# as such, it makes sense only to use with single query sequences
# and mainly for databases that are genome files
# to find homologs to one or a set of genes in those genomes

# the name of the output file is “refGeno——targetGeno_blastp_parsed_out”
import sys
import re
from Bio.Blast import NCBIXML

blastOutputXMLFile = sys.argv [1]
referenceGenome = sys.argv [2]
targetGenome = sys.argv [3]

blastOutputXMLHandle = open (blastOutputXMLFile)

listOfBlastRecords = NCBIXML.parse (blastOutputXMLHandle)
filename=str(referenceGenome)+"_"+str(targetGenome)+"_blastp_parsed_out"
f = open(filename,"w+")
for aSingleBlastRecord in listOfBlastRecords: 
    for i in range (len (aSingleBlastRecord.alignments)):
        description = aSingleBlastRecord.descriptions [i]
        alignment = aSingleBlastRecord.alignments [i]
        targetTitle = re.compile ("gnl\|BL_ORD_ID\|\d* ").sub ("", description.title)
        f.write(">{0} {1} >{2} {3}\n".format(aSingleBlastRecord.query,
              alignment.hsps[0].query,
              targetTitle,
              alignment.hsps[0].sbjct))
f.close()