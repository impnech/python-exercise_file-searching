from Loggers.g_logging import g_logger 
try:
    import spacy
except ImportError as e:
    g_logger.error(f"couldn't import spacy lib")
    g_logger.exception(e)


# Load the small English model
nlp = spacy.load("en_core_web_sm")
print(nlp)
def lemmatize_query_spacy(text: str) -> str:
    doc = nlp(text)
    
    lemmas = [token.lemma_ for token in doc]

    return " ".join(lemmas)

def lemmatize_query_by_word(text: str):
    split = text.split()
    res=[]
    for w in split:
        doc = nlp(w)
        tok = doc[0]
        #print(f"{type(tok)=}\n{tok=}\n{tok.lemma_=}\n{tok.lang_=}\n{tok.lemma=}\n\n")
        res.append(tok.lemma_)
    return res


#query = "the running dogs are in the park's trees"
query = "I am running in the park with my deeping dogs stupid"
result = lemmatize_query_by_word(query)
print(result)
result = lemmatize_query_spacy(query)
print(result)

