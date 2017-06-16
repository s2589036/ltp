import pickle
def main():
        """sentencelist contains nertaged sentences"""
        nertweetlist = pickle.load(open('nertweetlist.pickle','rb'))
        tagdict = {}
        for tweet in nertweetlist:
                #I came across two invalid tags (at the end everything is
                #lowered, so the o is dismissed and only one error is left
                # printed these to see what happened
                if tag == "o":
                                print(tweet)
                        if tag == "B":
                                print(tweet)


                for (word,tag) in tweet:
                        if tag in tagdict:
                                tagdict[tag] += 1
                        else:
                                tagdict[tag] = 1

        for tag in sorted(tagdict, reverse=True):
                print(tag,"\t",tagdict[tag])

main()
