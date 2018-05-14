# Open multi FASTA files with protein sequences
sequences9=open("09.fa.txt.pfa","r")
sequences17=open("17.fa.txt.pfa","r")
sequences24=open("24.fa.txt.pfa","r")
sequences49=open("49.fa.txt.pfa","r")
sequences51=open("51.fa.txt.pfa","r")

# Read lines from these files
sequences9=sequences9.readlines()
sequences17=sequences17.readlines()
sequences24=sequences24.readlines()
sequences49=sequences49.readlines()
sequences51=sequences51.readlines()

# Since lines end with line break, strip of that and create new lists
new_list_9=[]
for x in sequences9:
    new_x=x.strip("\n")
    new_list_9.append(new_x)

new_list_17=[]
for x in sequences17:
    new_x=x.strip("\n")
    new_list_17.append(new_x)

new_list_24=[]
for x in sequences24:
    new_x=x.strip("\n")
    new_list_24.append(new_x)

new_list_49=[]
for x in sequences49:
    new_x=x.strip("\n")
    new_list_49.append(new_x)

new_list_51=[]
for x in sequences51:
    new_x=x.strip("\n")
    new_list_51.append(new_x)

# Open file with clusters and read lines in it
clusters=open("10_clusters.txt","r")
clusters=clusters.readlines()

# Strip lines of line break
striped_clusters=[]
for x in clusters:
    striped_clusters.append(x.strip("\n"))

# Split orthologs into separate strings
separated_clusters=[]
for x in striped_clusters:
    strings=x.split(" ")
    separated_clusters.append(strings)

cluster_1=[]
for x in separated_clusters:
    for y in new_list_9:
        if y=="%s%s" % ('>', x[0]):
            index=new_list_9.index(y)
            sequence=""
            for i in range (20):
                if ">" not in new_list_9[index+i]:
                    print(new_list_9[index+i])
                

