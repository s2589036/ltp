import pickle 
import numpy as np
def makedata():
	infolist = pickle.load(open('infolist.pickle','rb'))
	wordlist = pickle.load(open('wordlist.pickle','rb'))
	return infolist,wordlist

def makewordvectors():
	"""MAKES WORDVECTORS, [WORD1,WORD2,WORD3,WORD4,WORD5]"""
	infolist,wordlist = makedata()
#	infolist = [['O','O','O'],['O','O','O'],['O','O','O'],['O','O','O'],	['O','O','O']]+rawinfolist #add 5 non-namedentities
	Bpervectorlist,Ipervectorlist,Borgvectorlist,Iorgvectorlist,Blocvectorlist,Ilocvectorlist,Bmiscvectorlist,Imiscvectorlist = [[],[],[],[],[],[],[],[]]

	for i in range(5,len(infolist)): 
		listofwords = [infolist[i-5][0],infolist[i-4][0],infolist[i-3][0],infolist[i-2][0],infolist[i-1][0],infolist[i][0]]
		if infolist[i][2] == "B-PER":
			Bpervectorlist.append(listofwords)
		if infolist[i][2] == "I-PER":
			Ipervectorlist.append(listofwords)
		if infolist[i][2] == "B-ORG":
			Borgvectorlist.append(listofwords)
		if infolist[i][2] == "I-ORG":
			Iorgvectorlist.append(listofwords)
		if infolist[i][2] == "B-LOC":
			Blocvectorlist.append(listofwords)
		if infolist[i][2] == "I-LOC":
			Ilocvectorlist.append(listofwords)
		if infolist[i][2] == "B-MISC":
			Bmiscvectorlist.append(listofwords)
		if infolist[i][2] == "I-MISC":
			Imiscvectorlist.append(listofwords)
	return Bpervectorlist

makewordvectors()

def makenumbericvector(wordvector):
	infolist,wordlist = makedata()	
	for word in wordvector:
		numbericvector = [0]*len(wordlist)
		numbericvector[wordlist.index(word)] =+ 1
	return numbericvector
	
		
def makenumbericvectorlists():
	Bpervectorlist = makewordvectors()
	Bpernumbericvectorlist = []
	for item in Bpervectorlist:
		Bpernumbericvectorlist.append(makenumbericvector(item))
	print(Bpernumbericvectorlist)
makenumbericvectorlists()
		


