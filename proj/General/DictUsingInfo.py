from collections.abc import Hashable

from General.DictHandlerFactory import DictHandlerFactory
from General.ICorpusInfo import *
from General.DictHandler import DictHandler, KT, VT
from typing import TypeVar, Mapping, Iterable, Iterator, Generic, Type

DH = TypeVar('DH', bound=DictHandler)


class DictUsingInfo(ICorpusInfo, Generic[KT, VT], Mapping):


    __dict_handler: DH

    @property
    def _dict_handler(self) -> DH:
        try:
            return self.__dict_handler
        except AttributeError as e:
            raise AttributeError(f"This interface doesn't yet have its internal _dict_handler. "
                                 "To initialize it, use the method init(cls, dh: DictHandler)"
                                 f"thus the exception {e}")

    def init(self, dh: DH):
        self.__dict_handler: DH = dh
        self.reset()

    from General.DictHandlerFactory import DictHandlerFactory
    def __init__(self):
        """
        temporary solution to not init every dict-using-info manugally
        """
        try:
            self._dict_handler
        except (AttributeError):
            dh: DictHandler = DictHandlerFactory.get_dict_handler()
            self.init(dh)

    @abstractmethod
    def reset(self):
        raise NotImplementedError(f"don't have specific information to store in the generic {DictUsingInfo.__name__}")


    def __getitem__(self, __key: KT) -> VT:
        return self._dict_handler.__getitem__(__key)


    def __len__(self) -> int:
        return self._dict_handler.__len__()

    def __iter__(self) -> Iterator[VT]:
        return self._dict_handler.__iter__()
