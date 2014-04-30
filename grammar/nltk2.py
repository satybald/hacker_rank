import re, nltk, random

# https://developers.google.com/edu/python/regular-expressions
# http://www.dotnetperls.com/re
# http://blog.quibb.org/2010/01/nltk-regular-expression-parser-regexpparser/
# http://www.eecis.udel.edu/~trnka/CISC889-11S/lectures/armstrong-nltk-tagging.pdf


def pure_random():
	return ['am','are','were','was','is','been','being','be'][random.randrange(0, 8)]
def semi_random(l):
	return l[random.randrange(0, len(l)-1)]

def POS_tagger(word_phrase):
	patterns = [
	# cardinal numbers
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
    # singular nouns (default)
	(r'^she$', 'NNP'), (r'^he$', 'NNP'), (r'^it$', 'NNP'),

	# Have only
	(r'^have$', 'HAVE'), (r'^has$', 'HAVE'), (r'^had$', 'HAVE'),
	#Modals
	(r'^can$', 'MD'), (r'^may$', 'MD'), (r'^could$', 'MD'), (r'^to$', 'MD'), (r'^must$', 'MD'), (r'^should$', 'MD'), (r'^might$', 'MD'), (r'^will$', 'MD'),(r'^would$', 'MD'),
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

	# I only
	(r'^i$', 'NNP'),

	# plural proper nouns
	(r'^[A-Z].*s$', 'NNPS'), (r'^they$', 'NNPS'),(r'^we$', 'NNPS'),
	# plural nouns
	(r'.*s$', 'NNS'), 
	# singular proper nouns
	(r'^[A-Z].*$', 'NNP')
	
	]

	tagger = nltk.RegexpTagger(patterns)
	return tagger.tag(word_phrase)
# Strip Stop Words
# ['am','are','were','was','is','been','being','be']
# KK = int(raw_input())
# TEXT =  raw_input().replace(",", "").replace(".", "")
TEXT =  """
President Obama arrived in Seoul, South Korea, Friday to news that North Korea may ---- counting down to a nuclear weapons test. Such moves out of Pyongyang ---- no surprise and are typical for the North's behavior, Obama told reporters while in Tokyo, his previous stop on his Asia trip. The President said has ---- prepared to deliver a firm response, if a test ---- conducted during his visit. North Korea's heightened activity at its nuclear test site ---- already known. But now the final step needed for an underground detonation has ---- taken, a South Korean government official said Thursday. The North has closed off the entrance to the tunnel at the Punggye-ri nuclear test site, the official said. That gives Pyongyang 11 days to either detonate a nuclear device or cancel the test. It would ---- the North's fourth test of a nuclear weapon. Both Obama and South Korean President Park Geun-hye want to display a united front against North Korea, and the communist dictatorship has reacted to the American President's visit with condemnation.
""".replace(",", "").replace(".", "")

matchObj = re.findall( r'(\w+) ---- (\w+)', TEXT.strip(), re.M|re.I)
for x in matchObj:
	tags = POS_tagger(x)
	print tags
	# Modal
	if tags[0][1] == "MD":
		print "be"
	
	# elif tags[0][1] == "I":
	# 	if tags[1][1] == "I":
	# 	print semi_random(["was", "am", "is"])
	
	elif tags[0][1] == "HAVE":
		print "been"

	# Plurual Subject
	elif tags[0][1] == "NNS" or tags[0][1] == "NNPS": 
		# print semi_random(["were", "are"])
		if tags[1][1] == "VBG":
			print semi_random(["were", "are"])
		# past tense verbs
		elif tags[1][1] == "VBD":
			print semi_random(["were", "are"])
		else:
			print "are"
	elif tags[0][1] == "NN" or tags[0][1] == "NNP":
		print semi_random(["was", "is"])
	else:
		print semi_random(['been','being','be'])