from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('wordnet')
sentence = ["This","sentence","was","transformed", "using", "WordNet", "Lemmatizer"]

lemmatizer = WordNetLemmatizer()

print (" ".join([lemmatizer.lemmatize(word) for word in sentence]))