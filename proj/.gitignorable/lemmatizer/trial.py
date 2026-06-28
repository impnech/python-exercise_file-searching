import spacy

# Load the English language model
#nlp = spacy.load('en_core_web_sm')
nlp = spacy.load('en')

# Define a sample text
text = "Apple is looking at buying U.K. startup for $1 billion"

# Process the text with spaCy
doc = nlp(text)

print(doc)

