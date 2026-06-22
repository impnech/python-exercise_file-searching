from typing import Iterator, Iterable
from Parsing.StringStreamTransformer import StringStreamTransformer

from abc import ABC, abstractmethod



class BadWordsRemover(StringStreamTransformer):

    _wordset: set[str]
    @classmethod
    @abstractmethod
    def transform(cls, original: Iterator[str] | Iterable[str]) -> Iterator[str]:
        pass

    @classmethod
    def _badwords(cls) -> set[str]:
        if hasattr(cls, '_wordset'):
            return cls._wordset
        cls._init_wordset()
        return cls._wordset

    @classmethod
    @abstractmethod
    def _init_wordset(cls):
        pass

    @classmethod
    def add_bad_word(cls, w:str):
        cls._wordset.add(w)

    @classmethod
    def remove_bad_word_from_set(cls, w: str):
        cls._wordset.remove(w)
