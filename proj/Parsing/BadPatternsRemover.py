from typing import Iterator, Iterable
from Parsing.BadWordsRemover import BadWordsRemover
import re

class BadPatternsRemover(BadWordsRemover):
    @classmethod
    def _init_wordset(cls,):
        cls._wordset: set[str] = {r'\s*'}

    @classmethod
    def transform(cls, original: Iterator[str] | Iterable[str]) -> Iterator[str]:
        badpatterns: set[str] = cls._badwords()
        return filter(lambda w: not any(re.fullmatch(pattern=pa, string=w) for pa in badpatterns), original)


if __name__ == '__main__':
    li = ["text,adf ", "", "fds", " ", " \t"]
    print(list(BadPatternsRemover.transform(li)))