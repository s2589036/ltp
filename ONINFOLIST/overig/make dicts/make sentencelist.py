#maak: van traindata:
#[[(w,n),(w,n)],[(w,n),(w,n)],[(w,n),(w,n)(w,n),(w,n)]]
import pickle

def makesentencelist():
    """sentencelist contains nertaged sentences"""
    train = open("train.txt","r")
    sentencelist = []
    sentence = []
    for line in train.readlines():
        if len(line.split()) == 3:
            [word,postag,nertag] = line.split()
            sentence.append((word,nertag))
        else:
            sentencelist.append(sentence)
            sentence = []
    print(sentencelist[0:5])
    pickle.dump(sentencelist,open("sentencelist.pickle","wb"))

def makewordsentencelist():
    """sentencelist contains nertaged sentences"""
    train = open("train.txt","r")
    wordsentencelist = []
    wordsentence = []
    for line in train.readlines():
        if len(line.split()) == 3:
            [word,postag,nertag] = line.split()
            wordsentence.append(word)
        else:
            wordsentencelist.append(wordsentence)
            wordsentence = []
    print(wordsentencelist[0:5])
    pickle.dump(wordsentencelist,open("wordsentencelist.pickle","wb"))

makewordsentencelist()
