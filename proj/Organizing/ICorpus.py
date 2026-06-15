from Organizing.IDocument import DocumentIdentifier, IDocument
from Organizing.Observing import *
from abc import *
from typing import *


class ICorpus(Observable, Mapping[DocumentIdentifier, IDocument[DocumentIdentifier]]):
    """
    @abstractmethod
    def get_documents(self) -> Iterator[IDocument[Identifier]]:
        pass

    @abstractmethod
    def get_document(self, doc_id: Identifier) -> IDocument[Identifier]:
        pass

    """
    @abstractmethod
    def __len__(self) -> int:
        pass

