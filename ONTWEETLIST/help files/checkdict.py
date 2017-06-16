import pickle
ne = pickle.load(open("GOEDEtweetlist.pickle","rb"))
print(len(ne))
for item in ne:
    print(item)
