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
		keyword = ""
		for w in words:
			if w not in stopWords:
				keyword = keyword + " " + w
		
		keywords.append(keyword)
	return keywords

if __name__ == "__main__":
	main()
