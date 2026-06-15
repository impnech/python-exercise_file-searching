from abc import *
from typing import *
from numbers import Number

T = TypeVar('T', bound=Hashable)
S = TypeVar('S', bound=Sized)


def foo(t1: T, t2: T) -> None:
    print(hash(t1) + t2.__hash__())


s: str = "as"
i: int = 4
print(foo(s, i))
foo("as", 6)


class A(Generic[T]):

    def __eq__(self, other):
        if not isinstance(other, str | int | A):
            print("bad type")
            return False
        print("Good type")
        return True

    def __init__(self):
        self.log: S = tuple()

    def foo(self, t1: T, t2: T) -> None:
        self.log += (t1, t2)
        print(self.log.__len__())
        print(hash(t1) + t2.__hash__())


a = A()
a.foo(3, "r")
print(f"{a == 's'= }")


class B:
    @property
    @abstractmethod
    def val(self) -> int:
        pass


class A(B):

    @property
    def val(self) -> int:
        return 34

    @val.setter
    def val(self, value):
        pass


b = B()
a = A()
print(a.val)
a.val = 78
print(a.val)
