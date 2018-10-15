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
                soupSelector = soup.select(GoogleSearch.TOTAL_SELECTOR)
                
                if len(soupSelector):
                    totalText = soupSelector[0].children.next().encode('utf-8')
                    total = long(re.sub("[', ]", "", re.search("(([0-9]+[', ])*[0-9]+)", totalText).group(1)))
                else:
                    total = 0
            
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

def searchGoogle(site, keyword):
    return GoogleSearch().search('site:' + site + ' arguments \"' + keyword + '\"', num_results = 10)