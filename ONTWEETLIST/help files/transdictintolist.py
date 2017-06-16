#make nertweetlist / tweetlist (instead of dict)
import pickle
tweetdict = pickle.load(open("tweetdict.pickle","rb"))
nertweetdict = pickle.load(open("nertweetdict.pickle","rb"))


tweetlist = []
for item in sorted(tweetdict):
    tweetlist.append(tweetdict[item])

nertweetlist = []
for item in sorted(nertweetdict):
    nertweetlist.append(nertweetdict[item])

pickle.dump(tweetlist,open("tweetlist.pickle","wb"))
pickle.dump(nertweetlist,open("nertweetlist.pickle","wb"))
