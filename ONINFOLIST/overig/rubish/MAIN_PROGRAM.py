import random

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


def main():
	import pickle
	from nltk.tag import CRFTagger
	infolist = pickle.load(open('infolist.pickle','rb'))

	ct = CRFTagger()
	 
	train_data = [[(x,z) for [x,y,z] in infolist[:round(0.9*len(infolist))]]]
	    
	ct.train(train_data,'model.crf.tagger')
	ners = ct.tag_sents([[x for [x,y,z] in infolist[round(0.9*len(infolist)):]]])
	print(ners)
	   
	gold_sentences = [[(x,z) for [x,y,z] in infolist[round(0.9*len(infolist)):]]]

	ct.evaluate(gold_sentences) 
	print(ct.evaluate(gold_sentences))


