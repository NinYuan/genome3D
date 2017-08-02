# read genome From  HomoGeno
def  readgenomes(filepath):
	file_object = open(filepath)
	try:
		all_the_text = file_object.read( )
	finally:
		file_object.close( )
	if  all_the_text:
		#print all_the_text
		
		return all_the_text
	else:
		return False

# filepath="/home/hong/Pku/bio/Homo_sapiens/Homo_sapiens.GRCh38.dna.chromosome.X.fa"
# readgenomes(filepath)

#write resultDataFrequency to txt for later look
def  writeFrequency(filepath,nMatrix):
	text=trasToText(nMatrix)
	f = open(filepath, 'a')
	f.write(text)
	f.close()

#[[0.38461538461538464, 0, 0, 0.15384615384615385], [0.07692307692307693, 0, 0.07692307692307693, 0], [0, 0, 0, 0.07692307692307693], [0.07692307692307693, 0.07692307692307693, 0, 0.07692307692307693]]
#to   0.38461538461538464, 0, 0, 0.15384615384615385*0.07692307692307693, 0, 0.07692307692307693, 0*0, 0, 0, 0.07692307692307693*0.07692307692307693, 0.07692307692307693, 0, 0.07692307692307693]]

def   trasToText(Matrix):
	ilist=[]
	for each in Matrix:
		ilist.append(",".join(str(i) for i in each))
	s="*".join(ilist)
	stext="&"+s
	
	return stext

# Matrix=[[0.38461538461538464, 0, 0, 0.15384615384615385], [0.07692307692307693, 0, 0.07692307692307693, 0], [0, 0, 0, 0.07692307692307693], [0.07692307692307693, 0.07692307692307693, 0, 0.07692307692307693]]
# trasToText(Matrix)
# filepath="/home/hong/Pku/bio/resultData/hello"
# writeFrequency(filepath)


def  transToMatix(s):
	retMatrix=[]
	ilist=s.split("*")
	for each in ilist:
		jlist=each.split(",")
		zlist=[]
		for  x in jlist:
			zlist.append(float(x))
		retMatrix.append(zlist)

	return retMatrix
	#print retMatrix

# s="0.384615384615,0,0,0.153846153846*0.0769230769231,0,0.0769230769231,0*0,0,0,0.0769230769231*0.0769230769231,0.0769230769231,0,0.0769230769231"
# transToMatix(s)

def  transToSmatix(s):
	retMatrix=[]
	ilist=s.split("*")
	for each in ilist:
		jlist=each.split(",")
		zlist=[]
		for  x in jlist:
			zlist.append(x)
		retMatrix.append(zlist)

	return retMatrix
#
#from resultData read Matrix to show the result
#
def  readResultData(filepath):
	text=readgenomes(filepath)
	print "ok"

	ltex=text.split("&")
	print len(ltex)
	if [] in ltex:
		ltex.remove([])
	print ltex[1]

	fmatrix=transToMatix(ltex[1])
	smatrix=transToSmatix(ltex[2])
	# matrix=transToMatix(text)
	return fmatrix,smatrix