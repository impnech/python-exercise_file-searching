from StringStreamTransformer import *
from typing import *


class WordBasedStreamStringTransformer(StringStreamTransformer):
    @classmethod
    def transform(cls, original: Iterator[str] | Iterable[str]) -> Iterator[str]:
        return map(cls._str_transform, original)

    @classmethod
    @abstractmethod
    def _str_transform(cls, o_string: str) -> str:
        pass
