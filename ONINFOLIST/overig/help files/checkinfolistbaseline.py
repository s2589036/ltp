def main():
	import pickle
	infolist = pickle.load(open('infolist.pickle','rb')) #data from tweets
	counter = 0
	for item in infolist:
		if item[2] == "O":
			counter = counter + 1 
	print(counter/len(infolist))
main()


