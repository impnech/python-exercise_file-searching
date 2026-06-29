from abc import *
from typing import *
from CorpusStructure.ITerm import ITerm

DocumentIdentifier = TypeVar('DocumentIdentifier', bound=Hashable)


class IDocument(ABC, Generic[DocumentIdentifier]):

    def __init__(self, doc_id: DocumentIdentifier):
        self._id: DocumentIdentifier = doc_id

    @property
    def doc_id(self) -> DocumentIdentifier:
        return self._id

    @abstractmethod
    def stream_terms(self) -> Iterator[ITerm]:
        pass

    @abstractmethod
    def raw_term_stream(self) -> Iterator[Any]:
        pass

    @property
    @abstractmethod
    def length(self) -> int:
        """
        :return: the length of the document, how many terms are there.
        """
        pass
