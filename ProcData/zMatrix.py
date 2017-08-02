from formMatrix.strMatric import *
from formMatrix.initMatric import *
from ProcData.cmpMatrix import *
from showPic.printMatrx import *
from getData.readGenome import *
#kstring,genome, return zmatrix of sequence frequency
def  frequentMarix(kstring,genome,filepath):
	#get strMatric
	sMatric=FinalMatrix(kstring)
	#get initMatric
	nMatrix=iMatrix(kstring)

	slen=len(genome)
	#kstring=2#eg:AT
	irange=slen-kstring+1
	# print "nMatrix"
	#print nMatrix
	#get each kchars in genome
	for i in range(irange):
		estring=genome[i:i+kstring]
		nMatrix=cmpMat(estring, sMatric, nMatrix)
	print sMatric
	print nMatrix
	nMatrix=freMatrix(nMatrix, irange)
	print nMatrix
	
	charMat=printMat(nMatrix, sMatric, kstring)

	writeFrequency(filepath,nMatrix)
	writeFrequency(filepath,charMat)
	test_barchart(nMatrix,charMat)
	
	return nMatrix

def  freMatrix(nMatrix,irange):

	for  i in range(len(nMatrix)):
		for j in range(len(nMatrix[i])):
			if nMatrix[i][j]!=0:
				nMatrix[i][j]=float(nMatrix[i][j])/float(irange)

			
		
	return nMatrix

# kstring=2
# genome="GGGGGGATTCCCAA"

# # infilepath="/home/hong/Pku/bio/Homo_sapiens/Homo_sapiens.GRCh38.dna.chromosome.X.fa"
# # genome=readgenomes(infilepath)
# outfilepath="/home/hong/Pku/bio/resultData/hello"
# frequentMarix(kstring, genome,outfilepath)
