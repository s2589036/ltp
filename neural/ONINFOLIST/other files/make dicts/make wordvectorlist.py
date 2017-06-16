import pickle 
def makedata():
	train = open('train.txt',"r")
	infolist = pickle.load(open('infolist.pickle','rb'))
	labels = pickle.load(open('labels.pickle','rb'))

	
	#info is for example: De Art O or Floralux N B-ORG
	index = 0
	for info in infolist:
		precedingwords = infolist[index-5][0] + " " + infolist[index-4][0] + " " + infolist[index-3][0] + " " + infolist[index-2][0] + " " + infolist[index-1][0] 			+ " " + infolist[index-1][0]		
		wordvectors.append(precedingwords)
		index = index+1
	print("infolist: ",len(infolist))
	print("labels: ",len(labels))
	print("wordvectors: ",len(wordvectors))
	pickle.dump(wordvectors,open("wordvectors.pickle","wb")
