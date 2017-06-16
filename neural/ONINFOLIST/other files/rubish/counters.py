import pickle
infolist = pickle.load(open('sentencelist.pickle','rb'))
nerdict = {}
total = 0
for item in infolist:
    for (word,nertag) in item:
        total = total + 1
        if nertag not in nerdict:
            nerdict[nertag] = 0
        else:
            nerdict[nertag] += 1


for nertag in nerdict:
    print(nertag, nerdict[nertag])
print(183632/total)
