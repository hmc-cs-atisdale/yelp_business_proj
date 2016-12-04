import json
from pprint import pprint
from string import punctuation
import numpy as np
import csv
import unicodedata

def getReviews():
	reviewList = []
	buildStr = ''
	buildID = None
	count = 0
	for line in open('yelp_academic_dataset_review.json'):
		if count > 300000:
			break
		count +=1
		review_json = json.loads(line)
		review_json_votes = review_json['votes']
		review_json['votes'] = '\t'.join(map(unicode, review_json_votes.values()))
		review = map(unicode, review_json.values())

		if buildID == review[4]:
			buildStr += review[3]
		
		else:
			reviewList.append((buildID, buildStr))
			buildID = review[4]
			buildStr = ''

	return reviewList[1:]

def formatReview(s):
    s = ''.join([i for i in s if not i.isdigit()])
    word = ''.join(c for c in s if c not in punctuation)
    word = word.lower()
    word = word.replace('\n',' ')
    word = word.replace('\t',' ')

    strType = type('hi')
    if not strType == type(word):
    	word = unicodedata.normalize('NFKD', word).encode('ascii','ignore')

    wlist = word.split()


    return wlist

def main():
	reviewList = getReviews()
	wordHash = {}
	freqList = []
	wordSum = []
	bids = []

	#Generate the general hash list and the hash for each bussiness
	for bid,word in reviewList:
		wlist = formatReview(word)
		bDict = {}

		sumWords = 0.0

		#for each bussiness conunt the number of occurnaces and the total number of words
		for key in wlist:
			sumWords += 1.0
			if key in bDict:
				bDict[key] += 1.0
			else:
				bDict[key] = 1.0


		#now go through the keys again and remove words that happen to frequently or too infreqeuntly
		wordsRemoved = 0
		for key in bDict.keys():
			if bDict[key] < 2 or bDict[key]/sumWords > .1:
				#Add the words removed 
				wordsRemoved += bDict[key]
				del bDict[key]

			#Otherwise make sure the word is in the dictonary
			else:
				wordHash[key] = True

		sumWords -= wordsRemoved
		freqList.append(bDict)
		bids.append(bid)
		wordSum.append(sumWords)

	#create an array which represents the words uses in the reveiw.
	wordMatrix = np.zeros((len(reviewList),len(wordHash.keys())))
	keys = wordHash.keys()
	for i in range(len(freqList)):
		for j in range(len(keys)):
			if keys[j] in freqList[i]:
				wordMatrix[i][j] = freqList[i][keys[j]] / wordSum[i]
				# if wordMatrix[i][j] > .01:
				# 	wordMatrix[i][j] = 0

	print(wordMatrix.shape)

	rowNum, colNum = wordMatrix.shape

	outputFile = open('reveiwFreq.csv','w+')
	csv_writer = csv.writer(outputFile)

	for i in range(rowNum):
		csv_writer.writerow(wordMatrix[i])

	outputFile.close()

	outputFile = open('reveiwBussinessID.csv','w+')
	csv_writer = csv.writer(outputFile)
	csv_writer.writerow(bids)
	outputFile.close()

	outputFile = open('reveiwWordList.csv','w+')
	csv_writer = csv.writer(outputFile)
	csv_writer.writerow(keys)
	outputFile.close()




if __name__ == '__main__':
	main()