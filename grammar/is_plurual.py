import nltk

def POS_tagger(word_phrase):
	patterns = [(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), (r'.*able$', 'JJ'), (r'.*ness$', 'NN'), (r'.*ly$', 'RB'), (r'.*ing$', 'VBG'), (r'.*ed$', 'VBD'), (r'^[A-Z].*s$', 'NNPS'), (r'.*s$', 'NNS'), (r'^[A-Z].*$', 'NNP'), (r'.*', 'NN')]

	tagger = nltk.RegexpTagger(patterns)
	return tagger.tag(word_phrase)