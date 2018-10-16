import re

def countResponses(responseA, responseB):
	count = {'A':0, 'B':0, 'total':0}
	for result in responseA.results:
		count['A'] += 1
	for result in responseB.results:
		count['B'] += 1
	count['total'] = count['A'] + count['B']
	return count

def divideResponses(responseA, responseB):
	count = countResponses(responseA, responseB);
	
	print(count)
	
	responses = [{'result':None, 'site':None, 'rank':0}]*(count['total'])
	
	i = 0
	j = 0
	for result in responseA.results:
		responses[i]['result'] = result
		responses[i]['site'] = 'procon.org'
		responses[i]['rank'] = i + 1
		i += 2
		j += 1
		if (j > count['B']):
			i -= 1
	
	i = 1
	j = 0
	for result in responseB.results:
		responses[i]['result'] = result
		responses[i]['site'] = 'prosancons.com'
		responses[i]['rank'] = i + 1
		i += 2
		j += 1
		if (j > count['A']):
			i -= 1
	
	return responses

def procondotorg(content):
	arguments = {"pro":[], "con":[]}
	
	proBlock = re.findall(r'pro-quote-box">(.+?)</div', content)

	if not (proBlock and \
		(re.search(r'bolded-intro">(.+?)</span', proBlock[0]) or \
		re.search(r'Top 10', result.title))):
		return None
           
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
	
	return arguments

def prosanconsdotorg(content):
	arguments = {"pro":[], "con":[]}
	
	proBlock = re.findall(r'Pros:</h2>(.+?)<h2>Cons', content)

	if not proBlock:
		return None
	
	args = re.search(r'/strong></span>(.+?)</p>', case)
	for case in args:
		arguments["pro"].append(case.group(1))
		
	conBlock = re.findall(r'<h2>Cons +:</h2>(.+?)<footer>', content)
	args = re.search(r'bolded-intro">(.+?)</span', case)
	for case in args:
		arguments["con"].append(case.group(1))
	
	return arguments
