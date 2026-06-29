from abc import ABC, abstractmethod
from typing import *

class StringStreamTransformer(ABC):
    @classmethod
    @abstractmethod
    def transform(cls, original: Iterator[str] | Iterable[str]) -> Iterator[str]:
        pass
