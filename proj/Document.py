from IDocument import *
from typing import Iterable


class Document(IDocument):
    """
    SOLID - Warning: again, holds _terms as list, it's not so bad here since it's just one implementation of IDocument
    """
    _id: Identifier
    _terms: list[ITerm]

    def get_id(self) -> Identifier:
        return self._id

    def __init__(self, doc_id: Identifier, terms: Iterable[ITerm]):
        IDocument.__init__(self, doc_id)
        self.terms: list[ITerm] = []
        self.terms.extend(terms)

    '''
    def add_terms(self, terms: Iterable[ITerm]) -> None:
        self.terms.extend(terms)
    '''

    def get_terms(self) -> Iterator[ITerm]:
        # raise NotImplemented("the types are still messy")
        def gen():
            for t in self.terms:
                yield t

        return gen()
