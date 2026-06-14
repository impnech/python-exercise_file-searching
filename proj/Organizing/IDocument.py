from abc import *
from typing import Generator, TypeVar, Hashable, Iterator, Generic
from typing import *
from Organizing.ITerm import ITerm

DocumentIdentifier = TypeVar('DocumentIdentifier', bound=Hashable)


class IDocument(ABC, Generic[DocumentIdentifier], Iterable[ITerm]):
    _id: DocumentIdentifier

    def __init__(self, doc_id: DocumentIdentifier):
        self._id = doc_id

    @abstractmethod
    def get_id(self) -> DocumentIdentifier:
        pass

    @abstractmethod
    def get_terms(self) -> Iterator[ITerm]:
        pass

    @abstractmethod
    def __len__(self):
        pass
