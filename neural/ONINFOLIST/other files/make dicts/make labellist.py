import pickle

def main():
	infolist = pickle.load(open('infolist.pickle','rb'))
	labels = []	
	for item in infolist:
		if item[2] == "O":
			labels.append("0")
		else:
			labels.append("1")

	pickle.dump(labels,open("labellist.pickle","wb"))
main()
