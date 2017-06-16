from nltk.tag import CRFTagger
ct = CRFTagger()
 
train_data = [[('Universiteit','Noun'), ('is','Verb'), ('een','Det'), ('goed','Adj'),('goede','Adj' ),('plek','Noun'),('hond','Noun'),('eet','Verb'),('vlees','Noun')]]
    
ct.train(train_data,'model.crf.tagger')
ct.tag_sents([['hond','is','goed'], ['kat','eet','vlees']])
   
gold_sentences = [[('hond','Noun'),('is','Verb'),('goed','Adj')] , [('kat','Noun'),('eet','Verb'), ('vlees','Noun')]] 
ct.evaluate(gold_sentences) 
    
ct = CRFTagger() 
ct.set_model_file('model.crf.tagger')
print(ct.evaluate(gold_sentences))
 
