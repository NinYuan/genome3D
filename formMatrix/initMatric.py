import math
#kstring  return matrix of 0
def  iMatrix(kstring):
	grids=4**kstring
	rows=int(math.sqrt(grids))
	#grids=math.exp(1)
	retMat=[]
	for i in range(rows):
		irow=[]
		for j in range(rows):
			irow.append(0)

		retMat.append(irow)
	# print retMat
	return retMat
# kstring=2
# iMatrix(kstring)


def  printMat(fMat,sMat,kstring):
	iRange=len(sMat)
	retMat=iMatrix(kstring)
	print retMat
	for fi in range(iRange):
		for fj in range(iRange):
			retMat[fi][fj]=sMat[fi][fj]+"\n\n"+str(fMat[fi][fj])
	return retMat

	 