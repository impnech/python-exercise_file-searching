from Organizing.Observing import *
from Organizing.IDocument import *
# from Organizing.ICorpus import *
from Organizing.ICorpus import *

from typing import *
from abc import ABC, abstractmethod


class CorpusInfo:
    _corpus: ICorpus

    def __len__(self) -> int:
        return len(self._corpus)

    def get_doc_len(self, doc_id: DocumentIdentifier) -> int:
        """
        length (hm terms) of the document known by doc_id
        :param doc_id: the identifier of the document in question
        :return: how many terms does the document has.
        """
        return len(self._corpus[doc_id])

