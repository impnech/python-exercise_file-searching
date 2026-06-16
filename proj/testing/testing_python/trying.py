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
        for i in range(10):
            yield i

    def __getitem__(self, __key: int) -> int:
        li = [i * i for i in range(100)]
        try:
            return li[__key + 6]
        except(Exception):
            raise KeyError()


m = M()

print(4 in m)
print(2323 in m)
for k in m:
    print(k)
print("\n\n\n")
for k in m:
    print(k)


class B(Number):
    def __hash__(self) -> int:
        return 6

    def __getitem__(self, item):
        return item + 3


# a = A()
b = B()
