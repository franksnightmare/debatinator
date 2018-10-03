def writeArguments(fstream, arguments):
	fstream.write("Pro:\n")
	for arg in arguments["pro"]:
		fstream.write('\t' + arg + '\n')

	fstream.write("Con:\n")
	for arg in arguments["con"]:
		fstream.write('\t' + arg + '\n')
	fstream.write('\n')
