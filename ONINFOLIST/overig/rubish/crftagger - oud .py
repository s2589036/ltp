import pickle
from nltk.tag import CRFTagger

def oninfolist():
	

	"""NU DOEN: KIJK NAAR FORMAT VAN GEGEVEN INFORMATIE OP INTERNET IN VOORBEELD, CHECK ALLE LIJSTEN DIE IK GEMAAKT HEB OF ZE OVEREENKOMEN MET DE VORM"""
	

	#SEE: http://www.nltk.org/_modules/nltk/tag/crf.html	
	infolist = pickle.load(open('sentencelist.pickle','rb')) 
	limit = round(len(infolist)*0.4)
	train_data = infolist[0:limit]
	#print("train_data = ", train_data[0:10])
	
	ct = CRFTagger()
	#print(infolist[0:10])

	realsentences = []
	realsentence = ""
	"""
	for sentence in infolist[limit:]:
		for (word,nertag) in sentence:
			realsentence = realsentence +" "+ word
		realsentences.append(realsentence)
		realsentence = ""
	pickle.dump(realsentences,open("realsentences.pickle","wb"))
	print("pickle-bestand gemaakt")
	"""
	realsentences = pickle.load(open("realsentences.pickle","rb"))
	print("REALSENTENCES:", realsentences[0:10])
	splitsentences = [] #[['dog','is','good'],['cat','eat','meat']]
	for r in realsentences:
		splitsentence = r.split()
		splitsentences.append(splitsentence)


	#print("train_data:", infolist[0:10])
	#print("sentences for tag_sents:", splitsentences[0:10])
	ct.tag_sents(splitsentences[limit:])
	gold_sentences = infolist[limit:]
	print("GOLD SENTENCES:", infolist[10:20])
	print(ct.evaluate(gold_sentences))
	    
oninfolist()

def ontweetdata():
	tweetinfolist = pickle.load(open('tweetinfolist.pickle','rb')) #data from tweets
	counter = 0	
	for item in tweetinfolist:
		if item[1] == "O":
			counter = counter + 1
	print("BASELINE: ", (counter)/len(tweetinfolist))

	ct = CRFTagger()
	train_data = [[(x.lower(),y.lower()) for [x,y] in tweetinfolist[round(0.9*len(tweetinfolist)):]]]
	ct.set_model_file('model.crf.tagger')    
	ct.train(train_data,'model.crf.tagger')
	   
	gold_sentences = [[(x.lower(),y.lower()) for [x,y] in tweetinfolist[:round(0.9*len(tweetinfolist))]]]
  
	
	print(ct.evaluate(gold_sentences))

#ontweetdata()

"""INFORMATION ABOUT SCORES - on infolist """
	#with captialization information and 90% train data/10% test data: accuracy = 0.95

	#without capitalization information: 0.93


"""INFORMATION ABOUT SCORES - on tweets  """
	#BASELINE (everything = O ): 0.8484584060500291
	
	#on tweets including capitalization information (polluted): 0.857 - 31 tweets more good than baseline - 
	
	#on tweets without capitalization information: 0.855



	#FIND OUT IF IT CLASSIFIES EVERY THING AS O, HOW MANY PERCENT IS O, C
	#ALCULATE PRECISION/RECALL F-SCORE, WRITE EVERYTHING DOWN AND START WORKING ON NEURALNETWORK THING

