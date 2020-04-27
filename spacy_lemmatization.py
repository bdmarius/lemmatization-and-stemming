import spacy

nlp_model = spacy.load('en_core_web_sm')
tokens = nlp_model("This sentence was transformed using Spacy Lemmatization")
print (" ".join(token.lemma_ for token in tokens))