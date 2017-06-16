from nltk import word_tokenize
import pickle
nertaggedtweets = []

namedtweetdict = pickle.load(open("namedtweetdict.pickle","rb"))
nertaggedwords = pickle.load(open("nertaggedwords.pickle","rb"))

for id in sorted(namedtweetdict):
	if id not in nertaggedwords:
		print(len(nertaggedwords)," tweets are already completely NER-tagged")		
		nertaggedwords[id] = []
		tweet = namedtweetdict[id]
		print("\n\n",tweet)
		listofwords = word_tokenize(tweet)
		for word in listofwords:
			nertag = "-"
			while nertag not in ["","O","B-per","I-per","B-loc","I-loc","B-org","I-org","B-misc","I-misc"]:
				print("\n",word)			
				nertag = str(input("What nertag is this? (O (enter),B-per,I-per,B-loc,I-loc,B-org,I-org,B-misc,I-misc) \n"))		
				if nertag == "":			
					nertaggedwords[id].append((word,"O"))
				else:
					if nertag in ["","O","B-per","I-per","B-loc","I-loc","B-org","I-org","B-misc","I-misc"]:
						nertaggedwords[id].append((word,nertag))
	pickle.dump(nertaggedwords,open("nertaggedwords.pickle","wb"))

