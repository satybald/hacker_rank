import random

# nt = int(raw_input())
nt = 6

for x in xrange(nt):
	verbs = ['am','are','were','was','is','been','being','be']

	idx = random.randint(0, len(verbs)-1)
	print verbs[idx]