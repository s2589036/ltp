from nltk.tag.perceptron import PerceptronTagger

# This may take a few minutes. (But once loaded, the tagger is really fast!)
tagger = PerceptronTagger(load=False)
tagger.load('model.perc.dutch_tagger_small.pickle')

# Tag a sentence.
tagger.tag('Alle vogels zijn nesten begonnen , behalve ik en jij .'.split())

import nltk.data
from nltk.tokenize import word_tokenize

sent_tokenizer = nltk.data.load('tokenizers/punkt/dutch.pickle')
    
def tokenize(text):
    for sentence in sent_tokenizer.tokenize(text):
        yield word_tokenize(sentence)

sentences = tokenize('Alle vogels zijn nesten begonnen, behalve ik en jij. Waar wachten wij nu op?')

for sentence in sentences:
    print(tagger.tag(sentence))
