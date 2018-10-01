import sys
import re
import urllib2
import math
from bs4 import BeautifulSoup
from pprint import pprint
from threading import Thread
from collections import deque
from time import sleep
        
class GoogleSearch:
    USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 58.0.3029.81 Safari/537.36"
    SEARCH_URL = "https://google.com/search"
    RESULT_SELECTOR = "h3.r a"
    TOTAL_SELECTOR = "#resultStats"
    RESULTS_PER_PAGE = 10
    DEFAULT_HEADERS = [
            ('User-Agent', USER_AGENT),
            ("Accept-Language", "en-US,en;q=0.5"),
        ]
    
    def search(self, query, num_results = 10, prefetch_pages = True, prefetch_threads = 10):
        searchResults = []
        pages = int(math.ceil(num_results / float(GoogleSearch.RESULTS_PER_PAGE)));
        fetcher_threads = deque([])
        total = None;
        for i in range(pages) :
            start = i * GoogleSearch.RESULTS_PER_PAGE
            opener = urllib2.build_opener()
            opener.addheaders = GoogleSearch.DEFAULT_HEADERS
            response = opener.open(GoogleSearch.SEARCH_URL + "?q="+ urllib2.quote(query) + ("" if start == 0 else ("&start=" + str(start))))
            soup = BeautifulSoup(response.read(), "lxml")
            response.close()
            if total is None:
                totalText = soup.select(GoogleSearch.TOTAL_SELECTOR)[0].children.next().encode('utf-8')
                total = long(re.sub("[', ]", "", re.search("(([0-9]+[', ])*[0-9]+)", totalText).group(1)))
            results = self.parseResults(soup.select(GoogleSearch.RESULT_SELECTOR))
            if len(searchResults) + len(results) > num_results:
                del results[num_results - len(searchResults):]
            searchResults += results
            if prefetch_pages:
                for result in results:
                    while True:
                        running = 0
                        for thread in fetcher_threads:
                            if thread.is_alive():
                                running += 1
                        if running < prefetch_threads:
                            break
                        sleep(1)
                    fetcher_thread = Thread(target=result.getText)
                    fetcher_thread.start()
                    fetcher_threads.append(fetcher_thread)
        for thread in fetcher_threads:
            thread.join()
        return SearchResponse(searchResults, total);
        
    def parseResults(self, results):
        searchResults = [];
        for result in results:
            url = result["href"];
            title = result.text
            searchResults.append(SearchResult(title, url))
        return searchResults

class SearchResponse:
    def __init__(self, results, total):
        self.results = results;
        self.total = total;

class SearchResult:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.__text = None
        self.__markup = None
    
    def getText(self):
        if self.__text is None:
            soup = BeautifulSoup(self.getMarkup(), "lxml")
            for junk in soup(["script", "style"]):
                junk.extract()
                self.__text = soup.get_text()
        return self.__text
    
    def getMarkup(self):
        if self.__markup is None:
            opener = urllib2.build_opener()
            opener.addheaders = GoogleSearch.DEFAULT_HEADERS
            response = opener.open(self.url);
            self.__markup = response.read()
        return self.__markup
    
    def __str__(self):
        return  str(self.__dict__)
    def __unicode__(self):
        return unicode(self.__str__())
    def __repr__(self):
        return self.__str__()

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

def searchGoogle(keyword):
    return GoogleSearch().search('site:procon.org arguments \"' + keyword + '\"', num_results = 10)
	
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

def main():
	keyword = getKeyword(sys.argv)
	
	print(keyword)
	
	response = searchGoogle(keyword)
	arguments = getArguments(response)
	printArguments(arguments)
	
	


if __name__ == "__main__":
	main()
