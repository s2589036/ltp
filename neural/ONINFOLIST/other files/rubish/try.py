infolist = []
labels = []
wordvectors = []
import pickle 
import numpy as np
def makedata():

	train = open('train.txt',"r")
	for line in train.readlines():
		if len(line.split())>0:
			infolist.append(line.split())


	for item in infolist[0:1000]:
		if len(item)>0:
			#print(item)			
			#if last item is "O", it s not a named entity (label = 0)
			if item[2] == "O":
				labels.append("0")
			#else: (if last item is not "O", it s not a named entity (label = 1))
			else:
				labels.append("1")

	#info is for example: De Art O or Floralux N B-ORG
	for info in infolist[0:1000]:
		#print(info)
		index = infolist.index(info)+5
		wordvector = [infolist[index-1][0],infolist[index-2][0],infolist[index-3][0],infolist[index-4][0],infolist[index-5][0]]		
		if len(wordvector)==5:
			wordvectors.append(wordvector)
		else:
			print("NIET GELIJK")
	
	assert(len(labels)==len(wordvectors))
	

	return labels,wordvectors,infolist


from sklearn.feature_extraction.text import CountVectorizer
def makevectorsnumeric():
	listofwords = pickle.load(open("listofwords.pickle","rb"))
	print("Making data..")	
	labels,wordvectors,infolist = makedata() 
	print("Data made.")

	print(len(listofwords))
	vectorizer = CountVectorizer(vocabulary=listofwords)
	vectors = [] 	
	for wordvector in wordvectors:
		print("BEKIJK DIT: ",wordvectors)		
		vector = vectorizer.fit_transform(wordvector)
		print("BEKIJK DIT: ",vector)
		vectors.append(vector)

	return vectors,labels,wordvectors,infolist

makevectorsnumeric()

