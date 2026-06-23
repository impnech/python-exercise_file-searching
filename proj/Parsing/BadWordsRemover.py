from typing import Iterator, Iterable
from Parsing.StringStreamTransformer import StringStreamTransformer

from abc import ABC, abstractmethod



class BadWordsRemover(StringStreamTransformer):

    _wordset: set[str]
    @classmethod
    @abstractmethod
    def transform(cls, original: Iterator[str] | Iterable[str]) -> Iterator[str]:
        raise NotImplementedError()

    @classmethod
    def _badwords(cls) -> set[str]:
        try:
            return cls._wordset
        except (AttributeError, NameError):
            cls._init_wordset()
            return cls._wordset

    @classmethod
    @abstractmethod
    def _init_wordset(cls, *args, **kwargs):
        raise NotImplementedError()

    @classmethod
    def add_bad_word(cls, w:str):
        cls._wordset.add(w)

    @classmethod
    def remove_bad_word_from_set(cls, w: str):
        cls._wordset.remove(w)


if __name__ == '__main__':
    from Parsing.BadPatternsRemover import BadPatternsRemover

    text = ["a_--23SGSDFSDFas", "a@#@DSDF345234sdf", "dfd#@DSDS"]

    res = list(BadPatternsRemover.transform(text))

    print(res)
