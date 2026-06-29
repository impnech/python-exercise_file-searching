from abc import abstractmethod
from typing import Iterator, Iterable
from CorpusStructure.ITerm import ITerm

class StringStreamTransformer:
    @classmethod
    @abstractmethod
    def transform(cls, original: Iterator[ITerm] | Iterable[ITerm]) -> Iterator[ITerm]:
        pass
