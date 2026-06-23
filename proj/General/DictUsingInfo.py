from collections.abc import Hashable


from General.ICorpusInfo import *
from General.DictHandler import DictHandler, KT, VT
from typing import TypeVar, Mapping, Iterable, Iterator, Generic

DH = TypeVar('DH', bound=DictHandler)


class DictUsingInfo(ICorpusInfo, Generic[KT, VT], Mapping):


    __dict_handler: DH

    @property
    def _dict_handler(self) -> DH:
        try:
            return self.__dict_handler
        except AttributeError:
            raise AttributeError("This interface doesn't yet have its internal _dict_handler. "
                                 "To initialize it, use the method init(cls, dh: DictHandler)")

    def init(self, dh: DH):
        self.__dict_handler: DH = dh
        self.reset()

    


    @abstractmethod
    def reset(self):
        raise NotImplementedError(f"don't have specific information to store in the generic {DictUsingInfo.__name__}")


    def __getitem__(self, __key: KT) -> VT:
        return self._dict_handler.__getitem__(__key)


    def __len__(self) -> int:
        return self._dict_handler.__len__()

    def __iter__(self) -> Iterator[VT]:
        return self._dict_handler.__iter__()
