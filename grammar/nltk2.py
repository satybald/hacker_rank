import nltk, re

# https://developers.google.com/edu/python/regular-expressions
# http://www.dotnetperls.com/re
# http://blog.quibb.org/2010/01/nltk-regular-expression-parser-regexpparser/
# http://www.eecis.udel.edu/~trnka/CISC889-11S/lectures/armstrong-nltk-tagging.pdf

text = '''
When the modern Olympics began in 1896, the initiators and organizers ---- looking for a great popularizing event, recalling the ancient glory of Greece. The idea of a marathon race came from Michel Breal, who wanted the event to feature in the first modern Olympic Games in 1896 in Athens. This idea was heavily supported by Pierre de Coubertin, the founder of the modern Olympics, as well as by the Greeks. The Greeks staged a selection race for the Olympic marathon on 10 March 1896 that ---- won by Charilaos Vasilakos in 3 hours and 18 minutes (with the future winner of the introductory Olympic Games marathon coming in fifth). The winner of the first Olympic Marathon, on 10 April 1896 (a male-only race), was Spyridon "Spyros" Louis, a Greek water-carrier, in 2 hours 58 minutes and 50 seconds. The women's marathon ---- introduced at the 1984 Summer Olympics (Los Angeles, USA) and ---- won by Joan Benoit of the United States with a time of 2 hours 24 minutes and 52 seconds. Since the modern games were founded, it has become a tradition for the men's Olympic marathon to be the last event of the athletics calendar, with a finish inside the Olympic stadium, often within hours of, or even incorporated into, the closing ceremonies. The marathon of the 2004 Summer Olympics revived the traditional route from Marathon to Athens, ending at Panathinaiko Stadium, the venue for the 1896 Summer Olympics. Since the modern games ---- founded, it has become a tradition for the men's Olympic marathon to be the last event of the athletics calendar, with a finish inside the Olympic stadium, often within hours of, or even incorporated into, the closing ceremonies. The marathon of the 2004 Summer Olympics revived the traditional route from Marathon to Athens, ending at Panathinaiko Stadium, the venue for the 1896 Summer Olympics. The Olympic men's record ---- 2:06:32.  
'''
# with open("corpus.txt", "r"):

f = open("corpus.txt","r")

# ['am','are','were','was','is','been','being','be']
for line in f.read().split("."):
	matchObj = re.findall( r'(.*) are (.*?) .*', line.strip(), re.M|re.I)

	if matchObj:
	   # print "matchObj.group() : ", matchObj.group()
	   # print "matchObj.group(1) : ", matchObj.group(1)
	   # print "matchObj.group(2) : ", matchObj.group(2)
	   print [x for x in matchObj]
	else:
	   print "No match!!"


