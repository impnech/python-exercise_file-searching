import os; print(f"current working directory: {os.getcwd()} ") 
import sys; 
for p in sys.path: print(p)
from InfoLogic.InfoPerDocument import InfoPerDocument, DocumentIdentifier
from InfoLogic.InvertedIndexCounter import InvertedIndex, InvertedIndexCounter
from CorpusStructure.DocumentsHolder import DocumentsHolder

class MaxFtd(InfoPerDocument[DocumentIdentifier, int]):
    """
    Calculates the maximum frequency of any term in each document.
    """
    def reset(self):
        docs = DocumentsHolder()
        counter: InvertedIndex = InvertedIndexCounter()
        for doc_id in docs.document_ids():
            doc = docs[doc_id]
            biggest = 0
            for t in doc.stream_terms():
                cur = counter[t][doc_id]
                if cur > biggest: biggest = cur

            self._dict_handler[doc_id] = max(counter[term][doc_id] for term in DocumentsHolder()[doc_id].stream_terms())




if __name__ == '__main__':
    from Dicts.DictHandlerFactory import DictHandlerFactory
    MaxFtd().init(DictHandlerFactory.get_dict_handler())
    x = MaxFtd()
    print(id(x) == id(MaxFtd()))
    for k in x.items():
        print(k)
    pass


