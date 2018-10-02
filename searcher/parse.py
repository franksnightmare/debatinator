import sys
import re
import urllib2
import math
from bs4 import BeautifulSoup
from pprint import pprint
from threading import Thread
from collections import deque
from time import sleep

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
	
def getArguments(response):
    arguments = {"pro":[], "con":[]}
    for result in response.results:
		print(("Title: " + result.title).encode(sys.stdout.encoding, errors='replace'))
		content = ''.join(repr(result.getMarkup()).split('\n'))
		
		proBlock = re.findall(r'pro-quote-box">(.+?)</div', content)

		if not (proBlock and \
			(re.search(r'bolded-intro">(.+?)</span', proBlock[0]) or \
			re.search(r'Top 10', result.title))):
			continue
            
		for case in proBlock:
			arg = re.search(r'bolded-intro">(.+?)</span', case)
			if not arg:
				arg = re.search(r'"(.+?)<br />', case)
			if arg:
				arguments["pro"].append(arg.group(1))
			
		conBlock = re.findall(r'con-quote-box">(.+?)</div', content)
		for case in conBlock:
			arg = re.search(r'bolded-intro">(.+?)</span', case)
			if not arg:
				arg = re.search(r'"(.+?)<br />', case)
			if arg:
				arguments["con"].append(arg.group(1))
		break
    return arguments

def printArguments(arguments):
	print("Pro:")
	for arg in arguments["pro"]:
		print(arg)

	print("Con:")
	for arg in arguments["con"]:
		print(arg)
