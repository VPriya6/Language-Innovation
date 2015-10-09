import sys;
import codecs;
import csv;
import json;
import nltk;
import os;
import re;
import matplotlib.pyplot as plt
import scipy.special as sps
import numpy as np
import math;

dictionary = {}
directory = os.listdir(sys.argv[1])
extension = re.compile('.*csv');
for file in directory:
	if(extension.match(file)):
		# print("reading file ......." +file)
		with open(os.getcwd() + "/" + sys.argv[1] +"/"+file, 'rU') as f:
			reader = csv.reader(f, delimiter=',')
			try:
				for row in reader:
					if len(row) >= 7:
						words = row[6].split(' ')
						for word in words:
							if not '#' in word and not '@' in word and not "http" in word:
								if word.lower() in dictionary:
									dictionary[word.lower()]+=1;
								else:
									dictionary[word.lower()]=1;
			except:
				continue


# print(json.dumps(dictionary, indent =2))

# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
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

for w in sorted(wordRanks, key=wordRanks.get):
	print(w, wordRanks[w])




	

