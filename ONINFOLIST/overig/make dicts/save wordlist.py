def main():
	import pickle
	infolist = pickle.load(open('infolist.pickle','rb'))
	wordlist = []
	for item in infolist:
		word = item[0]
		if word not in wordlist:
			wordlist.append(word)
	pickle.dump(wordlist, open('wordlist.pickle','wb'))
main()


