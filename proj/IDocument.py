from abc import *
from typing import Generator, TypeVar, Hashable,Iterator
from ITerm import ITerm

Identifier = TypeVar("Identifier", bound=Hashable)


class IDocument(ABC):
    _id: Identifier

    def __init__(self, doc_id: Identifier):
        self._id = doc_id

    @abstractmethod
    def get_id(self) -> Identifier:
        pass

    @abstractmethod
    def get_terms(self) -> Iterator[ITerm]:
        pass
