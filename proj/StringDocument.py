from IDocument import *
from typing import *


class StringDocument(IDocument):

    def __init__(self, terms: Iterable[ITerm]):
        self.terms: list[ITerm] = []
        self.terms.extend(terms)

    def add_terms(self, terms: Iterable[ITerm]) -> None:
        self.terms.extend(terms)

    def get_terms(self) -> Generator[ITerm]:
        raise NotImplemented("the types are still messy")

        def gen():
            for t in self.terms:
                yield t

        return gen()
