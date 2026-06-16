#from Organizing.ICorpus import *
from Organizing.ICorpus import *

from typing import *


class CorpusInfo:
    _corpus: ICorpus

    def __init__(self, corpus: ICorpus):
        self._corpus: ICorpus = corpus

    def amount_of_documents(self) -> int:
        return len(self._corpus)


    def get_document_ids(self) -> Iterator[DocumentIdentifier]:
        return self._corpus.__iter__()


    def get_doc_len(self, doc_id: IDocument[DocumentIdentifier]) -> int:
        """
        length (hm terms) of the document known by doc_id
        :param doc_id: the identifier of the document in question
        :return: how many terms does the document has.
        """
        return len(self._corpus[doc_id])

