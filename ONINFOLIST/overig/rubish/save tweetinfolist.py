def main():
	import pickle
	nertaggedwords = pickle.load(open('nertaggedwords.pickle','rb')) #data from tweets
	tweetinfolist = []	
	for id in nertaggedwords:
		for (word,nertag) in nertaggedwords[id]:
			tweetinfolist.append([word,nertag])

	pickle.dump(tweetinfolist,open('tweetinfolist.pickle','wb'))
main()


