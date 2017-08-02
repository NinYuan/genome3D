import numpy as np
from mayavi import mlab
from mayavi.mlab import *
import mayavi
from getData.readGenome import *
from formMatrix.initMatric import *

def  test_barchart(fMatrix,charMat):
    """ Demo the bar chart plot with a 2D array.
    """
    
    s = np.array(fMatrix)
    barchart(s)
    #barchart(s,line_)
    mayavi.mlab.colorbar(object=None, title="gene", orientation=None, nb_labels=8, nb_colors=None, label_fmt=None)
    # mayavi.mlab.xlabel("G  C")
    # mayavi.mlab.ylabel("G  A")
    #mayavi.mlab.text(0.5,0.5,"ok")

    indexRange=len(fMatrix)

    print charMat
    for i in range(indexRange):
        for j in range(indexRange):
            mlab.text3d(i,j,fMatrix[i][j]+0.5,str(charMat[i][j]),scale=(0.1,0.1,0.1))
            # mlab.text3d(i,j,fMatrix[i][j],"G\n"+str(fMatrix[i][j]),scale=(0.1,0.1,0.1))
     # mlab.text3d(0,0,fMatrix[0][0],str(0.25),scale=(0.1,0.1,0.1))
            #mlab.text(xindex,yindex,str(fMatrix[i][j])

            #mlab.text3d(i, j, fMatrix[i][j], str( fMatrix[i][j]),line_width=0.5)
            
        
    # for i, x in enumerate(fMatrix):
    # #print x,i
    #     mlab.text3d(x[0], x[1], x[2], str(i))
    #     mlab.text3d(x[0], x[1], x[2], str(i))
    mlab.show()


def  printTestFromResultData(filePath):
    fMatrix,cMatric=readResultData(filePath)
    print fMatrix,cMatric
    test_barchart(fMatrix,cMatric)

# filepath="/home/hong/Pku/bio/resultData/hello"
# printTestFromResultData(filepath)

