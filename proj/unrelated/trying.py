from abc import *
from abc import ABC
from typing import *
from numbers import Number


class A(ABC):
    @abstractmethod
    def foo(self):
        print(self)


class M(Mapping[int, int]):
    def __len__(self) -> int:
        pass

    def __iter__(self) -> Iterator[str]:
        def gen():
            for i in range(10):
                yield i

        return gen()

    def __getitem__(self, __key: int) -> int:
        return __key + 6

m=M()
for k in m.items():
    print(k)


class B(Number):
    def __hash__(self) -> int:
        return 6

    def __getitem__(self, item):
        return item + 3


# a = A()
b = B()
