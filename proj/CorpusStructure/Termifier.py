from typing import Iterator,Iterable
from CorpusStructure.ITerm import ITerm
from CorpusStructure.StreamTermifier import StreamTermifier, abstractmethod

class Termifier(StreamTermifier):
    @classmethod
    @abstractmethod
    def _transform(cls, original_s: Iterator | Iterable) -> Iterator | Iterable:
        pass
    @classmethod
    def termify(cls, original: Iterator | Iterable) -> Iterator[ITerm]:
        return (cls.termify_by_one(x) for x in cls._transform(original))
    @classmethod
    def termify_by_one(cls, o_value) -> ITerm:
        raise NotImplementedError("Termifier is generic")

