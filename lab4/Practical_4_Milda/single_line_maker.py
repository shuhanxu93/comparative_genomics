f= open ("51.fa.txt.pfa","r")
f2=open ("51_oneline.fa.txt.pfa","w")
currentline=""
for line in f:
    if line.startswith(">"):
        line=line.rstrip("\n")
        if currentline != "":
            print (currentline,file=f2)
        print (line,file=f2)
        currentline=""
    else:
        line=line.rstrip("\n")
        currentline=currentline+line
print (currentline, file=f2)
f.close()
f2.close()
