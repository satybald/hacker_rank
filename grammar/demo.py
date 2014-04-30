import re, nltk

text = "would must have can"

def POS_tagger(word_phrase):
	patterns = [
	# cardinal numbers
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
	#Modals
	(r'^can$', 'MD'), (r'^could$', 'MD'), (r'^to$', 'MD'), (r'^must$', 'MD'), (r'^should$', 'MD'), (r'^might$', 'MD'), (r'^will$', 'MD'), 
	#Verbs
	(r'^won$', 'VBD'),
	# past tense verbs
	(r'.*ed$', 'VBD'), 
	# adjectives
	(r'.*able$', 'JJ'), 
	# nouns formed from adjectives
	(r'.*ness$', 'NN'), 
	# adverbs
	(r'.*ly$', 'RB'), 
	# gerunds
	(r'.*ing$', 'VBG'), 

	# plural proper nouns
	(r'^[A-Z].*s$', 'NNPS'), 
	# plural nouns
	(r'.*s$', 'NNS'), 
	# singular proper nouns
	(r'^[A-Z].*$', 'NNP'), 
	# singular nouns (default)
	(r'.*', 'NN')]

	tagger = nltk.RegexpTagger(patterns)
	return tagger.tag(word_phrase)
print POS_tagger(["games", "founded"])