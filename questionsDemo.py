import sys

import questionLoader.loader as loader
import questionParser.parser as parser

def main():
	questions = loader.loadFile("questionFile.txt")
	keywords = parser.parse(questions)
	
	for keyword in keywords:
		print(keyword)

if __name__ == "__main__":
	main()
