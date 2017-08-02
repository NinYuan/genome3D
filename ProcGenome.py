import sys
from ProcData.zMatrix import *
kstring=int(sys.argv[1])
print kstring
infilepath=sys.argv[2]
print infilepath
#infilepath="/home/hong/Pku/bio/Homo_sapiens/Homo_sapiens.GRCh38.dna.chromosome.X.fa"
textgenome=readgenomes(infilepath)
#print textgenome
genomelist=textgenome.split("\n")
genome="".join(genomelist)
print genome
outfilepath=sys.argv[3]
print outfilepath

#genome="ATCCCCCTTTTGGGGGGGA"
# outfilepath="/home/hong/Pku/bio/resultData/hello"
frequentMarix(kstring, genome,outfilepath)