from typing import Iterator

from General.InvertedIndex import TermInfo
from TF import *


class StandardTF(TF):
    @classmethod
    def calc_tf(cls, term: ITerm) -> float:
        pass

    @classmethod
    def __getitem__(cls, __key: ITerm) -> TermInfo:
        pass

    @classmethod
    def __len__(cls) -> int:
        pass

    @classmethod
    def __iter__(cls) -> Iterator[TermInfo]:
        pass


