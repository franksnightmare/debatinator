import sys
import time

import urllib2

import questionLoader.loader as QLoader
import questionWriter.writer as Qwriter
import questionParser.parser as spacyParser
import questionParser.parser2 as nltkParser

import searcher.search as searcher
import searcher.parse as parser
import searcher.test as tester

def main():
	questions = QLoader.loadFile("questionFile.txt")
	targets = QLoader.loadFile("targetFile.txt")
	newTargets = []
	for target in targets:
		if ',' in target:
			newTargets.append(target.split(','))
		else:
			newTargets.append([target])
	
	NLTKKeywords = nltkParser.parse(questions)
	spacyKeywords = spacyParser.parse(questions)
	
	fstream = open("tallyFile.csv", 'w')
	fstream.write("Plaintext,NLTK,Spacy")
	
	for i in range(0, len(questions)):
		print("\n" + NLTKKeywords[i] + " / " + spacyKeywords[i])
		
		tally = [0, 0, 0]
		keywords = [questions[i], NLTKKeywords[i], spacyKeywords[i]]
		
		for j in range(0, len(tally)):
			try:
				# Either check with a site included or no?
				responseA = searcher.searchGoogle(keywords[j], 'procon.org')
				time.sleep(1)
				responseB = searcher.searchGoogle(keywords[j], 'prosancons.com')
				time.sleep(1)
				
				# Not used
				# response = searcher.searchGoogle(None, keywords[j])
				
				ranking = tester.getFirstHitRanking(responseA, responseB, targets[i])
				
				# Not used
				# ranking = parser.getHitRanking(response, targets[i])
				
				tally[j] = ranking
				
				# just gotta sleep real good to avoid suspicion
				time.sleep(1)
			except urllib2.HTTPError as err:
				print(err)
				print("They caught onto us!")
				time.sleep(5)
		
		print(tally)
		fstream.write(str(tally[0])+","+str(tally[1])+","+str(tally[2]))
	
	fstream.close()

if __name__ == "__main__":
	main()
