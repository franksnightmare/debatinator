import spacy
import nltk
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords

tokenizer = RegexpTokenizer(r'\w+')
stopWords = set(stopwords.words('english'))
nlp = spacy.load('en')

def strip(sentence):
	clean_sentence = ""
	for character in sentence:
		if character.isalnum() or character in " '":
			clean_sentence += character
	return clean_sentence


def constructCompound(token):
	compound = token.text
	addition = ""
	switch = False
	for token2 in token.children:
		if token2.dep_ == u'prep':
			switch = True
		if switch:
			compound += " " + constructCompound(token2)
		addition += constructCompound(token2) + " "
	compound = addition + compound
	return compound

def parse(questions):
	keywords = []
	for question in questions:
		question = question.lower()
		words = tokenizer.tokenize(question)
		# words = word_tokenize(question)
		keyword = ""
		for w in words:
			if w not in stopWords:
				keyword = keyword + " " + w


		# doc = nlp(unicode(strip(question), "utf-8"))
		
		# keyword = "null"
		# extra = ""
		# possessive = False
		# for token in doc:
		# 	# print(token.text, token.pos_, token.dep_)
			
		# 	# Unused right now, just ignore
		# 	if token.dep_ == u'nsubj' or token.dep_ == u'nsubjpass':
		# 		extra = constructCompound(token)
			
		# 	if token.dep_ == u'poss':
		# 		possessive = True
		# 	if possessive and token.dep_ == u'dobj':
		# 		keyword = constructCompound(token)
		# 		break
		# 	if token.dep_ == u'ROOT' and token.pos_ == u'NOUN':
		# 		keyword = constructCompound(token)
		# 		break
		# 	if token.dep_ == u'pobj' or token.dep_ == u'npadvmod':
		# 		keyword = constructCompound(token)
		# 		break
		
		# if keyword == "null":
		# 	for token in doc:
		# 		if token.dep_ == u'dobj':
		# 			keyword = constructCompound(token)
		# 			break
		# 		if token.dep_ == u'nsubj' or token.dep_ == u'nsubjpass':
		# 			keyword = constructCompound(token)
		# 			break
		
		keywords.append(keyword)
	return keywords

if __name__ == "__main__":
	main()
