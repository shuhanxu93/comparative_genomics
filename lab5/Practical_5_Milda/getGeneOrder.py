import sys, re

# acquire first needed data

geneOrderList = []

aHandle = open (sys.argv [1])

lines = aHandle.readlines ()

for aLine in lines:

	aLine = aLine.replace ("\n", "")

	if aLine.startswith (">"):

		# print aLine [1:len (aLine)],
		geneOrderList.append (aLine [1:len (aLine)])

# acquire second needed data

partOfCluster = {}

bHandle = open (sys.argv [2])

lines = bHandle.readlines ()

id = 0

for aLine in lines:

	aLine = aLine.replace ("\n", "")
	words = aLine.split ()

	for aWord in words:

		if not partOfCluster.has_key (aWord):

			partOfCluster [aWord] = id

	id = id + 1

# put together

f=open("51_gene_order_2","w")

gene_order=""

for aGene in geneOrderList:

	if partOfCluster.has_key (aGene):

		gene_order=gene_order + str(partOfCluster[aGene]) + " "

print >>f,gene_order

f.close()
