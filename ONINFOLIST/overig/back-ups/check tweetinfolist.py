def main():
        import pickle
        l = pickle.load(open('sentencelist.pickle','rb')) #data from tweets
        for item in l:
                print(item)
main()


