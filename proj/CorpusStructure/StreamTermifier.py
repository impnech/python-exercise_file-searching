from abc import abstractmethod
from typing import Iterator, Iterable
from CorpusStructure.ITerm import ITerm

class StreamTermifier:
    @classmethod
    @abstractmethod
    def transform(cls, original: Iterator | Iterable) -> Iterator[ITerm]:
        pass

