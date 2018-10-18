import numpy as np

import matplotlib.pyplot as plt

def main():
	my_data = np.genfromtxt('tally.csv', dtype=int, delimiter=',', names=True)
	
	QmeansAfull = []
	QmeansAnltk = []
	QmeansAspacy = []
	QmeansAaverage = []
	
	QmeansBfull = []
	QmeansBnltk = []
	QmeansBspacy = []
	QmeansBaverage = []
	
	QmeansCfull = []
	QmeansCnltk = []
	QmeansCspacy = []
	QmeansCaverage = []
	
	for index in range(1,7+1):
		Q_data = my_data[my_data['Q']==index]
		A_data = Q_data[Q_data['fullA']!=0]
		B_data = Q_data[Q_data['fullB']!=0]
		
		QmeansAfull.append(np.mean(A_data['fullA']))
		QmeansAnltk.append(np.mean(A_data['nltkA']))
		QmeansAspacy.append(np.mean(A_data['spacyA']))
		Atotal = A_data['fullA'].tolist() + A_data['nltkA'].tolist() + A_data['spacyA'].tolist()
		QmeansAaverage.append(np.mean(Atotal))
		
		QmeansBfull.append(np.mean(B_data['fullB']))
		QmeansBnltk.append(np.mean(B_data['nltkB']))
		QmeansBspacy.append(np.mean(B_data['spacyB']))
		Btotal = B_data['fullB'].tolist() + B_data['nltkB'].tolist() + B_data['spacyB'].tolist()
		QmeansBaverage.append(np.mean(Btotal))
		
		QmeansCfull.append(np.mean(A_data['fullA'].tolist() + B_data['fullB'].tolist()))
		QmeansCnltk.append(np.mean(A_data['nltkA'].tolist() + B_data['nltkB'].tolist()))
		QmeansCspacy.append(np.mean(A_data['spacyA'].tolist() + B_data['spacyB'].tolist()))
		Ctotal = A_data['fullA'].tolist() + A_data['nltkA'].tolist() + A_data['spacyA'].tolist() + B_data['fullB'].tolist() + B_data['nltkB'].tolist() + B_data['spacyB'].tolist()
		QmeansCaverage.append(np.mean(Ctotal))
	
	plt.plot(range(1,7+1), QmeansAaverage, c='red')
	plt.scatter(range(1,7+1), QmeansAfull)
	plt.scatter(range(1,7+1), QmeansAnltk)
	plt.scatter(range(1,7+1), QmeansAspacy)
	plt.xlabel("Question")
	plt.ylabel("Search Ranking")
	plt.legend(["Average", "None", "NLTK", "Spacy"])
	plt.title("The search ranking per question for procon.org sites.")
	plt.show()
	
	plt.plot(range(1,7+1), QmeansBaverage, c='red')
	plt.scatter(range(1,7+1), QmeansBfull)
	plt.scatter(range(1,7+1), QmeansBnltk)
	plt.scatter(range(1,7+1), QmeansBspacy)
	plt.xlabel("Question")
	plt.ylabel("Search Ranking")
	plt.legend(["Average", "None", "NLTK", "Spacy"])
	plt.title("The search ranking per question for prosancons.com sites.")
	plt.show()
	
	plt.plot(range(1,7+1), QmeansCaverage, c='red')
	plt.scatter(range(1,7+1), QmeansCfull)
	plt.scatter(range(1,7+1), QmeansCnltk)
	plt.scatter(range(1,7+1), QmeansCspacy)
	plt.xlabel("Question")
	plt.ylabel("Search Ranking")
	plt.legend(["Average", "None", "NLTK", "Spacy"])
	plt.title("The average search ranking per question.")
	plt.show()
	
	TmeansAfull = []
	TmeansAnltk = []
	TmeansAspacy = []
	TmeansAaverage = []
	
	TmeansBfull = []
	TmeansBnltk = []
	TmeansBspacy = []
	TmeansBaverage = []
	
	TmeansCfull = []
	TmeansCnltk = []
	TmeansCspacy = []
	TmeansCaverage = []
	
	for index in range(1,8+1):
		T_data = my_data[my_data['topic']==index]
		A_data = T_data[T_data['fullA']!=0]
		B_data = T_data[T_data['fullB']!=0]
		
		TmeansAfull.append(np.mean(A_data['fullA']))
		TmeansAnltk.append(np.mean(A_data['nltkA']))
		TmeansAspacy.append(np.mean(A_data['spacyA']))
		Atotal = A_data['fullA'].tolist() + A_data['nltkA'].tolist() + A_data['spacyA'].tolist()
		TmeansAaverage.append(np.mean(Atotal))
		
		TmeansBfull.append(np.mean(B_data['fullB']))
		TmeansBnltk.append(np.mean(B_data['nltkB']))
		TmeansBspacy.append(np.mean(B_data['spacyB']))
		Btotal = B_data['fullB'].tolist() + B_data['nltkB'].tolist() + B_data['spacyB'].tolist()
		TmeansBaverage.append(np.mean(Btotal))
		
		TmeansCfull.append(np.mean(A_data['fullA'].tolist() + B_data['fullB'].tolist()))
		TmeansCnltk.append(np.mean(A_data['nltkA'].tolist() + B_data['nltkB'].tolist()))
		TmeansCspacy.append(np.mean(A_data['spacyA'].tolist() + B_data['spacyB'].tolist()))
		Ctotal = A_data['fullA'].tolist() + A_data['nltkA'].tolist() + A_data['spacyA'].tolist() + B_data['fullB'].tolist() + B_data['nltkB'].tolist() + B_data['spacyB'].tolist()
		TmeansCaverage.append(np.mean(Ctotal))
	
	plt.plot(range(1,8+1), TmeansAaverage, c='red')
	plt.scatter(range(1,8+1), TmeansAfull)
	plt.scatter(range(1,8+1), TmeansAnltk)
	plt.scatter(range(1,8+1), TmeansAspacy)
	plt.xlabel("Topic")
	plt.ylabel("Search Ranking")
	plt.legend(["Average", "None", "NLTK", "Spacy"])
	plt.title("The search ranking per topic for procon.org sites.")
	plt.show()
	
	plt.plot(range(1,8+1), TmeansBaverage, c='red')
	plt.scatter(range(1,8+1), TmeansBfull)
	plt.scatter(range(1,8+1), TmeansBnltk)
	plt.scatter(range(1,8+1), TmeansBspacy)
	plt.xlabel("Topic")
	plt.ylabel("Search Ranking")
	plt.legend(["Average", "None", "NLTK", "Spacy"])
	plt.title("The search ranking per topic for prosancons.com sites.")
	plt.show()
	
	plt.plot(range(1,8+1), TmeansCaverage, c='red')
	plt.scatter(range(1,8+1), TmeansCfull)
	plt.scatter(range(1,8+1), TmeansCnltk)
	plt.scatter(range(1,8+1), TmeansCspacy)
	plt.xlabel("Topic")
	plt.ylabel("Search Ranking")
	plt.legend(["Average", "None", "NLTK", "Spacy"])
	plt.title("The average search ranking per topic.")
	plt.show()
		

if __name__ == "__main__":
	main()
