# this script takes the output of a blast run
# and outputs a fasta file with the best hit
# to the query in all database files where there is a hit
# as such, it makes sense only to use with single query sequences
# and mainly for databases that are genome files
# to find homologs to one or a set of genes in those genomes

import sys
import re
from Bio.Blast import NCBIXML

blastOutputXMLFile = sys.argv [1]

tag_ref = sys.argv [2]

tag_targ = sys.argv [3]

blastOutputXMLHandle = open (blastOutputXMLFile)

listOfBlastRecords = NCBIXML.parse (blastOutputXMLHandle)

f = open ("best_orthologs","w")

for aSingleBlastRecord in listOfBlastRecords:

	if len (aSingleBlastRecord.alignments) > 0:
                description = aSingleBlastRecord.descriptions [0]
                title_query = aSingleBlastRecord.query
                title_target = re.compile ("gnl\|BL_ORD_ID\|\d* ").sub ("", description.title)
	
                print (tag_ref, title_query, tag_targ, title_target, file=f)

f.close()
