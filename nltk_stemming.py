from nltk import PorterStemmer

sentence = ["This","sentence","was","transformed", "using", "Porter", "Stemmer"]
porterStemmer = PorterStemmer()

print (" ".join([porterStemmer.stem(word) for word in sentence]))