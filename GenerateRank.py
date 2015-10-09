import sys;
import codecs;
import csv;
import math;
import pickle;

dictionary = {}
outputFile = open(sys.argv[2], 'wb');
with open(sys.argv[1], 'rU') as f:
	reader = csv.reader(f, delimiter=',')
	try:
		for row in reader:
			if len(row) >= 7:
				words = row[6].split(' ')
				for word in words:
					if not '#' in word and not '@' in word and not "http" in word:
						w = word.lower().rstrip('?:!.,;');
						if w in dictionary:
							dictionary[w]+=1;
						else:
							dictionary[w]=1;
	except:
		pass


# print(json.dumps(dictionary, indent =2))

# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
if len(dictionary)>1:
	sortedFrequencies = []
	sortedWords = []
	wordRanks = {}
	rank = 1;
	for w in sorted(dictionary, key=dictionary.get, reverse = True):
		sortedWords.append(w)
  		sortedFrequencies.append(dictionary[w])

	size = len(sortedWords)

	wordRanks[sortedWords[0]] = rank;
	for i in range(1,size):
		if(sortedFrequencies[i]==sortedFrequencies[i-1]):
			wordRanks[sortedWords[i]] = rank;
		else:
			rank = rank +1;
			wordRanks[sortedWords[i]] = rank;

# for w in sorted(wordRanks, key=wordRanks.get):
# 	print(w, wordRanks[w])

	pickle.dump(wordRanks, outputFile)


	

