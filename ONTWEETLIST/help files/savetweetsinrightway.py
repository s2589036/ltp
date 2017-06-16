#make nertweetlist / tweetlist (instead of dict)
import pickle
nertweetdict = pickle.load(open("nertweetdict.pickle","rb"))

tweetlist = []
for id in sorted(nertweetdict):
    nertweet = nertweetdict[id]
    tweet = []
    for (word,tag) in nertweet:
        tweet.append(word)
    tweetlist.append(tweet)

pickle.dump(tweetlist,open("GOEDEtweetlist.pickle","wb"))
