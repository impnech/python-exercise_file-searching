import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


lemmatizer = WordNetLemmatizer()

def lemmatize_query_nltk(text: str) -> str:
    words = word_tokenize(text)
    
    # applies lemmatization to each word
    lemmas = [lemmatizer.lemmatize(word) for word in words]
    
    return " ".join(lemmas)


query = "the running dogs are in the park's trees"
result = lemmatize_query_nltk(query)
print(result)