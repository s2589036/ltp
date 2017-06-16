import pickle
infolist = pickle.load(open('infolist.pickle','rb'))
from operator import itemgetter
labellist = []

def makeworddict(): 
	#there are 12 different POS-tags: ['Art', 'N', 'Prep', 'V', 'Adv', 'Adj', 'Conj', 'Punc', 'Num', 'Pron', 'Int', 'Misc']
	#there are 12 NER-tags: ['O', 'B-ORG', 'B-MISC', 'B-PER', 'I-PER', 'B-LOC', 'I-MISC', 'I-ORG', 'I-LOC']
	#for every word I will save the most frequent POS-tag and NER-tag as a baseline


	worddict = {}
	for item in infolist:
		word = item[0]
		nertag = item[2]
		if word not in worddict:			
			nerdict[word] = {nertag: 1}
			posdict[word] = {postag: 1}

		if word in worddict:
			word = item[0]
			nertag = item[2]
			postag = item[1]:
			if nertag not in worddict[word]:
				nerdict[word] = 1
			if nertag in worddict[word]:
				nerdict[word][nertag] +=1


			if postag not in worddict[word]:
				nerdict[word] = 1
			if postag in worddict[word]:
				nerdict[word][nertag] +=1

	return worddict

def main():
	worddict = makeworddict()
	tweet = "ik wil graag Tele2 aanklagen "
	for word in tweet.split():
		if word in worddict:
			print(word, ":", sorted(worddict[word].items(), key=itemgetter(1))[0])	
		else: 
			print(word, ":", "B-PER")
main()









