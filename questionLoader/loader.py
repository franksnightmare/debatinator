def loadFile(path):
	fstream = open(path, "r")
	questions = list(fstream)
	fstream.close()
	return questions
