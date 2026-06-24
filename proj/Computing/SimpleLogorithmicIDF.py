from Computing.IDF import IDF
from Computing.InvertedIndexCounter import InvertedIndexCounter
from General.InvertedIndex import InvertedIndex, ITerm, Mapping
from Building.DocumentsHolder import DocumentsHolder, DocumentIdentifier

import math

class SimpleLogorithmicIDF(IDF):
    """
    Calculates the inverse document frequency using the formula: log(N/df_t)
    where N is the total number of documents in the corpus and df_t is the number of documents containing the term t.
    """
    @classmethod
    def calc_idf(cls, term: ITerm) -> float:
        counter: InvertedIndex[Mapping[DocumentIdentifier,int]] = InvertedIndexCounter()
        N = len(DocumentsHolder())
        df_t = len(counter[term])
        if df_t == 0:
            return 0.0  # or handle this case as appropriate
        return math.log(N / df_t)
    
if __name__ == '__main__':
    idf = SimpleLogorithmicIDF()
    for term in idf:
        print(f"Term: {term}, IDF: {idf[term]}")