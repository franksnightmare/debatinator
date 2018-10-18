import helper as helper
import sys

def getFirstHitRanking(responseA, responseB, url):
    responses = helper.divideResponses(responseA, responseB)
    
    for response in responses:
		result = response['result']
		print(("Title: " + result.title + " URL: " + result.url).encode(sys.stdout.encoding, errors='replace'))
		if result.url in url:
			return 10 - response['rank']
		
    return 0
