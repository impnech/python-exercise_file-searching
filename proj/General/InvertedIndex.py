
from Building.CorpusInfo import *

from General.ITerm import *
from typing import *

TermInfo = TypeVar('TermInfo')


class InvertedIndex(ICorpusInfo, Generic[TermInfo], Mapping[ITerm, TermInfo]):

    @classmethod
    @abstractmethod
    def __getitem__(cls,__key: ITerm) -> TermInfo:
        pass

    @classmethod
    @abstractmethod
    def __len__(cls) -> int:
        pass
    @classmethod
    @abstractmethod
    def __iter__(cls) -> Iterator[TermInfo]:
        pass

