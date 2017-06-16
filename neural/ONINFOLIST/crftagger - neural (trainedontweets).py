import pickle
from keras.models import Sequential
from collections import defaultdict
import numpy as np
from keras.utils import np_utils

from keras.preprocessing import sequence

import keras.backend as K

def f1_score(y_true, y_pred):

    # Count positive samples.
    c1 = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    c2 = K.sum(K.round(K.clip(y_pred, 0, 1)))
    c3 = K.sum(K.round(K.clip(y_true, 0, 1)))

    # If there are no true samples, fix the F1 score at 0.
    if c3 == 0:
        return 0

    # How many selected items are relevant?
    precision = c1 / c2

    # How many relevant items are selected?
    recall = c1 / c3

    # Calculate f1_score
    f1_score = 2 * (precision * recall) / (precision + recall)
    return f1_score

def main():
    sentencelist = pickle.load(open("sentencelist.pickle","rb"))
    bigsentencelist = []
    bigtaglistsentences = []
    for sentence in sentencelist:
        bigsentencelist.append([word for (word,tag) in sentence])
        bigtaglistsentences.append([tag for (word,tag) in sentence])

    tweetlist = pickle.load(open("nertweetlist.pickle","rb"))
    bigtweetlist = []
    bigtaglisttweets = []
    for tweet in tweetlist:
        bigtweetlist.append([word for (word,tag) in tweet])
        bigtaglisttweets.append([tag for (word,tag) in tweet])
    
    X_train = bigtweetlist #the words of the tweets
    y_train = bigtaglisttweets #the tags of the tweets

    X_test = bigsentencelist #the words of the sentencelist
    y_test = bigtaglistsentences #the tags of the sentencelist

        
    w2i = defaultdict(lambda: len(w2i))
    PAD = w2i["<pad>"] # index 0 is padding
    UNK = w2i["<unk>"] # index 1 is for UNK
    t2i = defaultdict(lambda: len(t2i))
    TPAD = w2i["<pad>"]

    # convert words to indices, taking care of UNKs
    X_train_num = [[w2i[word] for word in sentence] for sentence in X_train]
    w2i = defaultdict(lambda: UNK, w2i) # freeze
    X_test_num = [[w2i[word] for word in sentence] for sentence in X_test]

    # same for labels/tags
    y_train_num = [[t2i[tag] for tag in sentence] for sentence in y_train]
    t2i = defaultdict(lambda: UNK, t2i) # freeze
    y_test_num = [[t2i[tag] for tag in sentence] for sentence in y_test]

    num_labels = len(np.unique([y for sent in y_train for y in sent ]))
    y_train_1hot = [np_utils.to_categorical([t2i[tag] for tag in instance_labels], num_classes=num_labels) for instance_labels in y_train]
    y_test_1hot  = [np_utils.to_categorical([t2i[tag] for tag in instance_labels], num_classes=num_labels) for instance_labels in y_test]

    max_sentence_length = 100 #DIT NOG AANPASSEN

    X_train_pad = sequence.pad_sequences(X_train_num, maxlen=max_sentence_length, value=PAD)
    X_dev_pad = sequence.pad_sequences(X_test_num, maxlen=max_sentence_length, value=PAD)

    y_train_1hot_pad = sequence.pad_sequences(y_train_1hot, maxlen=max_sentence_length, value=TPAD)
    y_dev_1hot_pad = sequence.pad_sequences(y_test_1hot, maxlen=max_sentence_length, value=TPAD)

    np.random.seed(113) #set seed before any keras import

    from keras.models import Sequential
    from keras.layers import Dense, Activation, Embedding, LSTM
    from keras.layers.wrappers import TimeDistributed
    
    vocabulary_size = 100000 #DIT NOG AANPASSEN
    embeds_size = 100
     
    model = Sequential()
    model.add(Embedding(vocabulary_size, embeds_size, input_length=max_sentence_length,mask_zero=True))
    model.add(LSTM(32, return_sequences=True)) # return_sequences=TRUE! 
    model.add(TimeDistributed(Dense(num_labels))) # TimeDistributed 
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy', f1_score])

    
    model.fit(X_train_pad, y_train_1hot_pad, batch_size=10)
    print(model.evaluate(X_dev_pad, y_dev_1hot_pad))


    #https://github.com/bplank/ltp-notebooks-2017/blob/master/08_Classification_And_Structured_Prediction_with_Keras.ipynb

    #DO THIS NOW ^ then for tweets
        
main()
     
