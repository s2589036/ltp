def most_common(lst):
    return max(set(lst), key=lst.count)

def ner_tag(word):
	from nltk.tag import CRFTagger
	ct = CRFTagger()

	import pickle
	infolist = pickle.load(open('infolist.pickle','rb'))
	infodict = {}
	posdict = {}
	nerdict = {}


	for [word,postag,nertag] in infolist:
		if word not in posdict:
			posdict[word] = [postag]
		if word in posdict:
			posdict[word].append(postag)


	for [word,postag,nertag] in infolist:
		if word not in nerdict:
			nerdict[word] = [nertag]
		if word in nerdict:
			nerdict[word].append(nertag)


	#print(most_common(posdict["van"]))
	ner_tag = most_common(nerdict[word])
	return ner_tag

