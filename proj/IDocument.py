from abc import *
from typing import List, Generator
from Term import ITerm


class IDocument(ABC):
    @abstractmethod
    def get_terms(self) -> Generator[ITerm]:
        pass
