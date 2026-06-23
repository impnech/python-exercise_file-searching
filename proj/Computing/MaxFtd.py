from General.InfoPerDocument import InfoPerDocument, DocumentIdentifier
from Computing.InvertedIndexCounter import InvertedIndex, InvertedIndexCounter
from Building.DocumentsHolder import DocumentsHolder

class MaxFtd(InfoPerDocument[DocumentIdentifier, int]):
    def reset(self):
        counter: InvertedIndex = InvertedIndexCounter()
        for doc_id in DocumentsHolder().document_ids():
            self._dict_handler[doc_id] = max(counter[term][doc_id] for term in DocumentsHolder[doc_id].stream_terms())




if __name__ == '__main__':
    from General.DictHandlerFactory import DictHandlerFactory
    MaxFtd().init(DictHandlerFactory.get_dict_handler())
    x = MaxFtd()
    print(id(x) == id(MaxFtd()))

    pass


