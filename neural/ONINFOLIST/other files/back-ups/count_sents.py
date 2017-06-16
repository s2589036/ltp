import pickle
def main():
        """sentencelist contains nertaged sentences"""
        infosentencelist = pickle.load(open('sentencelist.pickle','rb'))
        print(len(infosentencelist))

main()
