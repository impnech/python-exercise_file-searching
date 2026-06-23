from typing import *
from abc import abstractmethod, ABC

KT = TypeVar('KT', bound=Hashable)
VT = TypeVar('VT')
class DictHandler(Mapping[KT, VT]):
    @abstractmethod
    def __setitem__(self, key: KT, value: VT):
        pass


if __name__ == '__main__':
    class A(DefaultDict):
        def __init__(self):
            pass
    a = A()