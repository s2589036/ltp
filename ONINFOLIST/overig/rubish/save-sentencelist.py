import pickle

def main():
    train = open("train data.txt","r")
    sentencelist = []
    sentence = []
    for line in train.readlines():
        if len(line.split()) == 3:
            [word,postag,nertag] = line.split()
            sentence.append((word,nertag))
        else:
            sentencelist.append(sentence)
            sentence = []
    pickle.dump(sentencelist,open("sentencelist.pickle","wb"))
main()
            
