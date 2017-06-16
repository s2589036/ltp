def main():
        import pickle
        l = pickle.load(open('nertweetlist.pickle','rb')) #data from tweets
        for item in l:
                print(item)
main()


