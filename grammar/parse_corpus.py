import re, nltk
lines = open("corpus.txt","r").readlines()

def POS_tagger(word_phrase):
	patterns = [
	# cardinal numbers
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
	#Modals
	(r'^can$', 'MD'), (r'^could$', 'MD'), (r'^to$', 'MD'), (r'^must$', 'MD'), (r'^should$', 'MD'), (r'^might$', 'MD'), 
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
# verbs = ['am','are','were','was','is','been','being','be']
verbs = ['am']

for line in lines:
	for v in verbs:
		strn = r'(\w+) %s (\w+) (\w+)' % (v)
		result = re.findall( strn, line.strip(), re.M|re.I)
		if len(result) != 0:
			print v, result
# print POS_tagger(['to', 'proclaimed', 'Inca'])