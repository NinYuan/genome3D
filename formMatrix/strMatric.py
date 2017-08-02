#[G,C],[A,T]]*[G,C],[A,T]]=[['GG', 'GC', 'CG', 'CC'], ['GA', 'GT', 'CA', 'CT'], ['AG', 'AC', 'TG', 'TC'], ['AA', 'AT', 'TA', 'TT']]
def  operMat(omat):
	list1=transMat(omat, "G")
	list2=transMat(omat, "C")
	list3=transMat(omat, "A")
	list4=transMat(omat, "T")
	nmat=linkMat(list1, list2, list3, list4)
	# print nmat
	return nmat

#omat=[["G","C"],["A","T"]]
# omat=[['GG', 'GC', 'CG', 'CC'], ['GA', 'GT', 'CA', 'CT'], ['AG', 'AC', 'TG', 'TC'], ['AA', 'AT', 'TA', 'TT']]
# operMat(omat)

#[G,C],[A,T]]*[G]=[[GG,GC],[GA,GT]
def  transMat(omat,elem):
	retList=[]
	for xlist in omat:
		eachList=[]
		for yelem in xlist:
			s=elem+yelem
			eachList.append(s)
		retList.append(eachList)
	#print retList
	return retList

#[['GG', 'GC'], ['GA', 'GT']]   [['CG', 'CC'], ['CA', 'CT']] =[[GG,GC,CG,CC],[GA,GT,CA,CT]] 
#inside func
def subLinkMat(G,C):
	retSubMat=[]
	for i in range(len(G)):
		ilist=[]
		ilist=G[i]+C[i]
		retSubMat.append(ilist)
	return retSubMat


#[['GG', 'GC'], ['GA', 'GT']] [['CG', 'CC'], ['CA', 'CT']] [['AG', 'AC'], ['AA', 'AT']] [['TG', 'TC'], ['TA', 'TT']]=[[GG,GC,CG,CC],[GA,GT,CA,CT],[AG,AC,TG,TC],[AA,AT,TA,TT]]
def  linkMat(G,C,A,T):
	list1=subLinkMat(G, C)
	list2=subLinkMat(A, T)
	retLinkMat=[]
	retLinkMat=list1+list2
	#print retLinkMat
	return retLinkMat

# G=[['GG', 'GC'], ['GA', 'GT']] 
# C=[['CG', 'CC'], ['CA', 'CT']]
# A= [['AG', 'AC'], ['AA', 'AT']]
# T= [['TG', 'TC'], ['TA', 'TT']]
# linkMat(G, C, A, T)

#kstring
def  FinalMatrix(kstring):
	omat=[["G","C"],["A","T"]]
	for i in range(kstring-1):
		omat=operMat(omat)
	
	return omat

# fmat=FinalMatrix(3)
# print fmat