import pickle
import numpy as np
from sklearn import svm


#initialize infolist, this will be filled with the information of the nex.txt-files (word, postag, nertag)
infolist = []
labels = []
wordvectors = []

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

	
	vectorizer = CountVectorizer(vocabulary=listofwords)
	vectors = [] 	
	for wordvector in wordvectors:
		print("BEKIJK DIT: "," ".join(wordvector))		
		vector = vectorizer.fit_transform(np.array(" ".join(wordvector)))
		print("BEKIJK DIT: ",vector)
		vectors.append(vector)

	return vectors,labels,wordvectors,infolist


def train(trainingvectors,traininglabels):
	clf = svm.SVC(kernel='linear', C = 1.0)
	X = np.array(trainingvectors)
	Y = np.array(traininglabels)
	clf.fit(X, Y)


def machinelearn():
	clf = svm.SVC(kernel='linear', C = 1.0)	
	vectors, labels, wordvectors,infolist = makevectorsnumeric()
	trainingsize = int(0.9*len(vectors))
	#print(trainingsize)
	traininglabels = labels[:trainingsize]
	testlabels = labels[trainingsize:]    

	trainingvectors = vectors[:trainingsize]
	testvectors = vectors[trainingsize:]    
	
	train(trainingvectors,traininglabels)

	#evaluating
	for item in testvectors:
        #print(item)
        	pred_label = clf.predict(item)
        	y_pred.append(pred_label)

	y_true = testlabels

	print("the accuracy score is ", accuracy_score(y_true, y_pred))

	
machinelearn()

