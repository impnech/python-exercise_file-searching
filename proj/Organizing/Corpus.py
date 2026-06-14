from typing import *
from typing import _T_co

from IDocument import IDocument, DocumentIdentifier

from ICorpus import *


class Corpus(ICorpus):

    _documents: dict[DocumentIdentifier, IDocument[DocumentIdentifier]]

    def __init__(self, documents: Iterable[IDocument[DocumentIdentifier]]):
        self._documents = {}
        for doc in documents:
            self._documents[doc.get_id()] = doc

    def __len__(self):
        return len(self._documents)

    def __iter__(self) -> Iterator[DocumentIdentifier]:
        def gen():
            for k in self._documents:
                yield k
        return gen()

    def __getitem__(self, __key: DocumentIdentifier) -> IDocument:
        return self._documents[__key]
