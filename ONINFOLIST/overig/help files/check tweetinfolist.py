def main():
	import pickle
	nertaggedwords = pickle.load(open('tweetinfolist.pickle','rb')) #data from tweets
	tweetinfolist = []	
	print(len(nertaggedwords)/200)
main()


