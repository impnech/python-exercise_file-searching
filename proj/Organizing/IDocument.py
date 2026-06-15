from abc import *
from typing import Generator, TypeVar, Hashable, Iterator, Generic
from typing import *
from Organizing.ITerm import ITerm

DocumentIdentifier = TypeVar('DocumentIdentifier', bound=Hashable)


class IDocument(ABC, Generic[DocumentIdentifier], Iterable[ITerm]):

    def __init__(self, doc_id: DocumentIdentifier):
        self._id: DocumentIdentifier = doc_id

    def get_id(self) -> DocumentIdentifier:
        return self._id

    @abstractmethod
    def get_terms(self) -> Iterator[ITerm]:
        pass

    @abstractmethod
    def __len__(self):
        """
        :return: the length of the document, in terms, how many terms are there.
        """
        pass
