import sys

import questionLoader.loader as QLoader
import questionWriter.writer as Qwriter
import questionParser.parser as QParser

import searcher.search as searcher
import searcher.parse as parser

def main():
	questions = QLoader.loadFile("questionFile.txt")
	keywords = QParser.parse(questions)
	
	fstream = open("answerFile.txt", 'w')
	
	for keyword in keywords:
		print("\n" + keyword)
		fstream.write(keyword + '\n')
		responseA = searcher.searchGoogle('procon.org', keyword)
		responseB = searcher.searchGoogle('prosancons.com', keyword)
		
		arguments = parser.getFirstArgument(responseA, responseB)
		Qwriter.writeArguments(fstream, arguments)
	
	fstream.close()

if __name__ == "__main__":
	main()
