setwd('~/comparative_genomics/project/scripts/glimmer_evaluation')
library(ggplot2)
plotGlimmer = ​ function​ (file=​ '51.glimmer.predict'​ ) {
t = read.table(file, header = F, skip = ​ 1 ​ )
c = data.frame(size=abs(t[,​ 2 ​ ]-t[,​ 3 ​ ]))
ggplot(c, aes(size))+geom_histogram(binwidth=​ 50​ )+ggtitle(file)
}
plotGlimmer()
