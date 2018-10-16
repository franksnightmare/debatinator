import sys
import time

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
	
	NLTKKeywords = nltkParser.parse(questions)
	spacyKeywords = spacyParser.parse(questions)
	
	fstream = open("tallyFile.csv", 'w')
	fstream.write("Plaintext,NLTK,Spacy")
	
	for i in range(0, len(questions)):
		print("\n" + NLTKKeywords[i] + " / " + spacyKeywords[i])
		
		tally = [0, 0, 0]
		keywords = [questions[i], NLTKKeywords[i], spacyKeywords[i]]
		
		for j in range(0, len(tally)):
			# Either check with a site included or no?
			responseA = searcher.searchGoogle('procon.org', keywords[j])
			time.sleep(5)
			responseB = searcher.searchGoogle('prosancons.com', keywords[j])
			time.sleep(5)
			
			# Not used
			# response = searcher.searchGoogle(None, keywords[j])
			
			ranking = tester.getFirstHitRanking(responseA, responseB, targets[i])
			
			# Not used
			# ranking = parser.getHitRanking(response, targets[i])
			
			tally[j] = ranking
			
			# just gotta sleep real good to avoid suspicion
			time.sleep(10)
		
		print(tally)
		fstream.write(str(tally[0])+","+str(tally[1])+","+str(tally[2]))
	
	fstream.close()

if __name__ == "__main__":
	main()
