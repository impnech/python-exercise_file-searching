# from OldOrganizing.ICorpus import *
from A_OLD.OldOrganizing.ICorpus import *


class CorpusInfo:

    def __init__(self, _corpus: ICorpus):
        self._corpus: ICorpus = _corpus

    def __len__(self) -> int:
        return self.amount_of_documents()

    def amount_of_documents(self):
        return len(self._corpus)

    def get_doc_len(self, doc_id: DocumentIdentifier) -> int:
        """
        length (hm terms) of the document known by doc_id
        :param doc_id: the identifier of the document in question
        :return: how many terms does the document has.
        """
        return len(self._corpus[doc_id])

