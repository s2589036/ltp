import pickle 
import numpy as np
def makedata():
	train = open('train.txt',"r")
	infolist = []
	#218736 lines in file
	for line in train.readlines():
		line = line.rstrip("\n")
		if len(line)>0:
			info = line.split()
			infolist.append(info)
	pickle.dump(infolist,open("infolist.pickle","wb"))
	print(infolist[18:22])
makedata()
