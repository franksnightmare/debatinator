import sys
import re
from googlesearch.googlesearch import GoogleSearch

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
	
	response = GoogleSearch().search("site:procon.org " + keyword, num_results = 1)
	arguments = {"pro":[], "con":[]}
	
	# Work in progress and also a mess
	# On top of that either google or procon.org does not like the scraping and maybe blocked me once?
	# 
	for result in response.results:
		print(("Title: " + result.title).encode(sys.stdout.encoding, errors='replace'))
		content = ''.join(repr(result.getMarkup()).split('\n'))
		
		proBlock = re.findall(r'pro-quote-box">(.+?)</div', content)
		
		for case in proBlock:
			arguments["pro"].append(re.findall(r'bolded-intro">(.+?)</span', case))
			
		conBlock = re.findall(r'con-quote-box">(.+?)</div', content)
		for case in conBlock:
			arguments["con"].append(re.findall(r'bolded-intro">(.+?)</span', case))
		
		# print(word.encode(sys.stdout.encoding, errors='replace'))
		break
	
	print(arguments)

if __name__ == "__main__":
	main()
