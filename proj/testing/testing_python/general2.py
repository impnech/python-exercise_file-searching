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


a = A[list]()
a.foo("r", 3)
print(f"{a == 's' = }")


class C(Callable[[int], int]):
    def __call__(self, *args, **kwargs):
        pass

    pass


c = C()


class B:
    @property
    @abstractmethod
    def val(self) -> int:
        pass


class A(B):
    # A.x = "static field A.x of A"
    x = "static field x of A"

    def __init__(self):
        pass

    @property
    def val(self) -> int:
        return 34

    @val.setter
    def val(self, value):
        pass


b = B()
a = A()
a2 = A(a)
print(A.x)
# print(A.)
print(a.val)
a.val = 78
print(a.val)
