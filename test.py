import sys
from googlesearch.googlesearch import GoogleSearch

def cleanWord(word):
	return word.strip("\n").strip("\t")

def getKeyword(stringList, skip = 1):
	strings = len(stringList)
	keyword = ""
	
	for i in range(0,strings):
		if (i < skip):
			continue
		
		keyword += stringList[i]
		if (i < strings - 1):
			keyword += " "
	
	return keyword

def main():
	keyword = getKeyword(sys.argv)
	
	print(keyword)
	
	try:
		response = GoogleSearch().search("site:procon.org " + keyword, num_results = 1)
		skipStep = 0
		startStep = 0
		start = False
		end = False
		
		arguments = 0
		argumentList = []
		
		# Work in progress and also a mess
		# On top of that either google or procon.org does not like the scraping and maybe blocked me once?
		# 
		for result in response.results:
			print(("Title: " + result.title).encode(sys.stdout.encoding, errors='replace'))
			
			for word in result.getText().split(" "):
				if (word):
					someWord = cleanWord(word)
					
					# Stop if the end is reached (did you know section)
					if skipStep >= 3:
						break
					
					# Finding the start of an argument
					if (not start and (someWord == "Pro" or someWord == "Con")):
						startStep = 1
						continue
					
					if startStep == 1:
						if word.isnumeric():
							startStep = 0
							start = True
							end = False
							startSkip = 2
							argumentList.append("")
						else:
							startStep = 0
					
					# Parsing the argument
					if start:
						if startSkip:
							startSkip -= 1
							continue
						
						if not end:
							print(arguments)
							print(someWord.encode(sys.stdout.encoding, errors='replace'))
							argumentList[arguments] += someWord.encode(sys.stdout.encoding, errors='replace') + " "
						
						# The first sentence should be all of the argument we want right now
						if "." in someWord:
							end = True
							arguments += 1
					
					# Should be the end of all the arguments (MAYBE)
					# I would check but since I can't do any requests anymore...
					# Only stop if any arguments were found
					if arguments != 0:
						if someWord == "Did":
							skipStep += 1
							continue
						if skipStep == 1:
							if someWord == "You":
								skipStep += 1
								continue
							else:
								skipStep = 0
						if skipStep == 2:
							if someWord == "Know?":
								skipStep += 1
								continue
							else:
								skipStep = 0
			
			# We are only interested in the first result right now
			break
	except HTTPError as httpError:
		print("WE MESSED UP")
		raise

if __name__ == "__main__":
	main()
