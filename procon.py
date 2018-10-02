import sys

import searcher.search as searcher
import searcher.parse as parser

def main():
	keyword = parser.getKeyword(sys.argv)
	
	print(keyword)
	
	response = searcher.searchGoogle(keyword)
	arguments = parser.getArguments(response)
	parser.printArguments(arguments)

if __name__ == "__main__":
	main()
