from IDocument import Identifier, IDocument
from abc import *
from typing import *

ID = TypeVar('ID', bound=Hashable)


class ICorpus(ABC):

    @abstractmethod
    def get_documents(self) -> Iterator[IDocument]:
        pass

    def foo(self, doc: IDocument) -> ID:
        self.get_documents()
        return doc.get_id()

    @abstractmethod
    def __len__(self):
        pass
