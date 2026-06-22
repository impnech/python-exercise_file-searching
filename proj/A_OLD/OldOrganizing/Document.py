from Building.IDocument import *
from typing import Iterable


class Document(IDocument):
    """
    SOLID-Warning: again, holds _terms as list, it's not so bad here since it's just one implementation of IDocument
    """
    def __init__(self, doc_id: DocumentIdentifier, terms: Iterable[ITerm] | None = None) -> None:
        self._id: DocumentIdentifier
        IDocument.__init__(self, doc_id)
        if terms is None:
            self._terms = []
            return
        self._terms: list[ITerm] = list(terms)

    '''
    def add_terms(self, terms: Iterable[ITerm]) -> None:
        self.terms.extend(terms)
    '''

    def __iter__(self) -> Iterator[ITerm]:
        for term in self._terms:
            yield term

    def __len__(self):
        return len(self._terms)

    def get_terms(self) -> Iterator[ITerm]:
        return self.__iter__()
