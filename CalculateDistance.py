import pickle;
import sys;
import math;

tract_1 = pickle.load(open(sys.argv[1], 'rb'));
tract_2 = pickle.load(open(sys.argv[2], 'rb'));

distance = 0
numberOfCommonWords = 0

for word in tract_1:
	if word in tract_2:
		numberOfCommonWords = numberOfCommonWords + 1
		print(word, tract_1[word], tract_2[word])
		distance = distance + (tract_1[word]- tract_2[word])**2

print(math.sqrt(distance/numberOfCommonWords))
# print(tract_1.values()[len(tract_1)-1], tract_2.values()[len(tract_2)-1])