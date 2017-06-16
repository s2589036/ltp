import pickle
def main():
        """sentencelist contains nertaged sentences"""
        infosentencelist = pickle.load(open('sentencelist.pickle','rb'))
        tagdict = {}
        for sentence in infosentencelist:
                for (word,tag) in sentence:
                        if tag in tagdict:
                                tagdict[tag] += 1
                        else:
                                tagdict[tag] = 1

        for tag in sorted(tagdict, reverse=True):
                print(tag,"\t",tagdict[tag])

main()
