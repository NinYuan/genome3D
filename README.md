software preneed:
ubuntu14.04
python 2.7
apt-get install python-vtk
pip install mayavi


usage
python ProcGenome.py 2 /home/hong/Pku/bio/Homo_sapiens/homoTest1.fa /home/hong/Pku/bio/resultData/homoTest1Res.txt 

ProcGenome.py : if  didn't calculate before then run this.    
2: the kstring num (2 refer to eg. GG   ;   3 refer to eg: GGG ;4 refer to eg GGGG; and so on)
/home/hong/Pku/bio/Homo_sapiens/homoTest1.fa  : the path where the genes you want to calculate and show
/home/hong/Pku/bio/resultData/homoTest1Res.txt   :   the path where the calculate result data you want to save 



 python showMatrixFromResult.py /home/hong/Pku/bio/resultData/homoTest1Res.txt
 showMatrixFromResult.py : if you have calculate before and you know the result data be saved somewhere then you can run this directly
 /home/hong/Pku/bio/resultData/homoTest1Res.txt  : the path where stored the calculated result data you want to see