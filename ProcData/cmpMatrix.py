#cmp each seqStr in sMatric  add 1 to  nMatric
def  cmpMat(seqStr,sMatric,nMatric):
	# print nMatric
	for i in range(len(sMatric)):
		for j in range(len(sMatric[i])):
			if sMatric[i][j]==seqStr:
				nMatric[i][j]=nMatric[i][j]+1
				# print nMatric
				return nMatric
			
	return False

# seqStr="GA"
# sMatric=[["GG","GC","CG","CC"],["GA","GT","CA","CT"],["AG","AC","TG","TC"],["AA","AT","TA","TT"]]
# nMatric=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# cmpMat(seqStr, sMatric, nMatric)