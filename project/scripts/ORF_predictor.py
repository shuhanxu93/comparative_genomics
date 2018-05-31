import argparse
import re
import sys

###########SYS_ARGV################
predictor = argparse.ArgumentParser(description='Do a simple ORF prediction.')
predictor.add_argument(	'inGeno',
			type=str, metavar='INGENO', default='.',
			help='genome file')			
predictor.add_argument(	'-t', dest='type',
			type=str, default='pro',
			help='eukaryotes or prokaryotes')
args = predictor.parse_args()


with open(args.inGeno) as f1:
    geno = f1.readlines()[1]

    # Check input file
    nuc = ['A','T','G','C']
    for i in geno:
        if i not in nuc:
            print(i)
            sys.exit("Wrong Input")

    # Read the genome in six reading frames
    print('Building reading frames')
    allCodons = []
    for k in [0,1,2]:
        codons = []
        for i in range(k,len(geno)-2-k):
            codons.append(geno[i]+geno[i+1]+geno[i+2])
        allCodons.append(codons)

    geno_rev = geno[::-1]
    for k in [0,1,2]:
        codons = []
        for i in range(k,len(geno)-2-k):
            codons.append(geno_rev[i]+geno_rev[i+1]+geno_rev[i+2])
        allCodons.append(codons)

    # Stroing all positions of start codons
    print ('Searching for start and stop codons')
    start = ['TAC']
    start_locs = []
    for i in range(len(allCodons)):
        start_loc = []
        for index, elem in enumerate(allCodons[i]):
            if elem in start:
                start_loc.append(index)
        start_locs.append(start_loc)
        
    # Stroing the positions of all stop codons
    stop = ['ATT','ACT','ATC']
    stop_locs = []
    for i in range(len(allCodons)):
        stop_loc = []
        for index, elem in enumerate(allCodons[i]):
            if elem in stop:
                stop_loc.append(index)
        stop_locs.append(stop_loc) 
  
######LENGTH#############
    # Finding all poteintial genes,
    # Assumption1: All genes > 100bp
    print('Selecting gene length')
    all_genes = []
    for i in range(len(start_locs)):
        genes = []
        for j in start_locs[i]:
            for k in range(len(stop_locs[i])):
                if j>stop_locs[i][k] and j<stop_locs[i][k+1]:
                    if stop_locs[i][k+1]-j >100:
                        gene = [j,stop_locs[i][k+1]]
                        genes.append(gene)        
        all_genes.append(genes)
        
    
#######OVERLAPPING############ 
    # Listing all overlap genes-mark the stop sites
    print('Searching for all overlap genes')
    stopSites = []
    for i in range(len(all_genes)):
        stopSite = []
        for j in all_genes[i]:
            stopSite.append(j[1])
        stopSites.append(stopSite)
    
    allOverlapGenes = []
    for i in range(len(all_genes)): 
        overlapGenes = []
        for stop in stopSites[i]:
            overlapGene =[]
            if sum(x.count(stop) for x in all_genes[i])>1:
            #if all_genes[i].count(stop)>1:
                #print(stop)
                for j in all_genes[i]:
                    print(j[1])
                    if j[1]== stop and j not in overlapGene:
                        overlapGene.append(j)
                overlapGenes.append(overlapGene)
        # Deleting duplictes
        list1= []
        for overlapGene in overlapGenes:
            if overlapGene not in list1:
                list1.append(overlapGene)
            #list1 = set(overlapGenes)
        allOverlapGenes.append(list1)

                
#######PROMOTERS#######
    # http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0007526
    # The majority of the putative TSSs were located between 20 to 40 nucleotides from the translational start site.
    print('applying promoter information')       
    # In overlapping genes, if one promoter appears at the right location upstream
    #the start codon, then that start codon is selected.
    # Finding tata box in eukaryotes
    # from 5'-3', the index is of bases instead of codons.
    # the tatabox is 25-30 bp upstream the transcriptional start sites
    # We 
    if args.type == 'euk':
        tataBox = ['TATAAAA','TATATAT','TATATAA','TATAAAT']
        tata_locs = []
        # Locating TATABoxs
        for i in tataBox:
            tata_loc = [m.start() for m in re.finditer(i, geno)]
            tata_locs.extend(tata_loc)
        # Distance(TATA box,start codon) = 45-70bp
        for startcodon in genome :
            if startcodon in [(tata_loc-45),(tata_loc-70):
                trueStartcodon.append(startcodon)

                            # If two start codon meets the same standard,select the one corresponding to longer gene.
                            break
            promoter_selects.append(promoter_select)
####!!!!!!for different reading frames there are overlaps!!!!!!!!!!!!!!!!        
            
    # Finding pribnow box in prokaryotes
    # pribnow box is usually -10bp from TSSs
    # We assume the distance between start codons and pribnow box is 30-70bp
    if args.type == 'pro':
        pribBox = ['TATAAT']
        prib_locs = []
        for i in pribBox:
            prib_loc = [m.start()//3 for m in re.finditer(i, geno)]
            prib_locs.extend(prib_loc)
        
        promoter_selects = []
        for i in [0,1,2]:
            promoter_select = []
            for prib in prib_loc:
                for item in allOverlapGenes[i]:
                    for k in item :
                        if k[0] >(prib-10) and k[0] < (prib+35):
                            promoter_select.append(k)
                            # If two start codon meets the same standard,select the one corresponding to longer gene.
                            break
            promoter_selects.append(promoter_select)

allgenes = allgenes -alloverlap + promoter_select

    
