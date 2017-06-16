import pickle
from nltk.tag import CRFTagger

from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
###DIT ALLEMAAL AANPASSEN VOOR TWEETS###
##-----eerst alle dictionaries hetzelfde
## vormgeven als in infolist, met tweetinfo, dan namen vervangen -----##

def onsentencelist():
        
        ct = CRFTagger()

              
        """nertweetlist contains ner-tagged tweets"""
        nertweetlist = pickle.load(open("nertweetlist.pickle","rb"))
        print(sorted(nertweetlist)[0:5])
        print(len(nertweetlist))
        
        """tweetlist contains the plain tweets """ 
        tweetlist = pickle.load(open('tweetlist.pickle','rb'))
        print(len(tweetlist))
        print(sorted(tweetlist)[0:5])
        
        """training size as percentage"""
        trainingsize = 0.9

        """ calculate where to split data """
        limit = round(trainingsize*len(nertweetlist))


        """train the data / choose one of the 2 blocks """
        #train_data = nertweetlist[:limit]
        #ct.train(train_data,'tweetmodel.crf.tagger')
        ct.set_model_file('tweetmodel.crf.tagger')
        

        """Test data and evaluate"""
        test_data = tweetlist[limit:]
        ct.tag_sents(test_data) # tagging sentences
        gold_sentences = nertweetlist[limit:]
        print("\nAccuracy:", ct.evaluate(gold_sentences))


        """ TURN TRAINED TAGGED LIST AND TEST LIST INTO ONE LIST CONTAINING
        ONLY THE TRUE AND PREDTAGS"""
        pred_nerlist = []
        for sentence in tweetlist[:limit]:
                #print("DIT:", sentence)
                for (word,nertag) in ct.tag(sentence):
                        pred_nerlist.append(nertag.lower())
                        
        true_nerlist = []
        #ct_true = gold_sentences
        for sentence in nertweetlist[:limit]:
                for (word,nertag) in sentence:
                        #true_nerlist.append((word,nertag))
                        true_nerlist.append(nertag.lower())

                        
                
        """ Print baseline """
        #TODO: calulate baseline
        
        """"Print F-score and confusion matrix """        
        print("\nF-score (micro):", f1_score(true_nerlist, pred_nerlist, average='micro') )
        print("\nF-score (macro):", f1_score(true_nerlist, pred_nerlist, average='macro') )
        print("\nF-score (weigthed):", f1_score(true_nerlist, pred_nerlist, average='weighted') )
        print("\nF-score (None):", f1_score(true_nerlist, pred_nerlist, average=None, labels = ["o","b-per","i-per","b-loc","i-loc","b-org","i-org","b-misc","i-misc"]) )
        
        
        print("\nConfusion matrix:\n")
        for item in ["O","B-per","I-per","B-loc","I-loc","B-org","I-org","B-misc","I-misc"]: print("  ",item,end="")
        print("\n",confusion_matrix(true_nerlist, pred_nerlist,labels = ["o","b-per","i-per","b-loc","i-loc","b-org","i-org","b-misc","i-misc"]))
        
onsentencelist()
