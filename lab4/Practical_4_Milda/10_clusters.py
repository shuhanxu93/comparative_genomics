# Open multi FASTA files with protein sequences
sequences9=open("09_oneline.fa.txt.pfa","r")
sequences17=open("17_oneline.fa.txt.pfa","r")
sequences24=open("24_oneline.fa.txt.pfa","r")
sequences49=open("49_oneline.fa.txt.pfa","r")
sequences51=open("51_oneline.fa.txt.pfa","r")

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

#Join all those lists together into one 
all_sequences=[]
all_sequences.extend(new_list_9)
all_sequences.extend(new_list_17)
all_sequences.extend(new_list_24)
all_sequences.extend(new_list_49)
all_sequences.extend(new_list_51)

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

#print sequences for each ortholog
count=0
for x in separated_clusters:
    count+=1
    count2=str(count)
    f=open(count2,"w")
    for y in x:
        for z in all_sequences:
            if z=="%s%s" % ('>', y):
                index=all_sequences.index(z)
                print (">",y,file=f)
                print (all_sequences[index+1], file=f)
    f.close()
