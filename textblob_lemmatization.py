from textblob import TextBlob

sentence = TextBlob('This sentence was transformed using TextBlob Lemmatization.')

print (" ".join([word.lemmatize() for word in sentence.words]))