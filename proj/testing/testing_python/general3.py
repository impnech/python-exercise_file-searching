from typing import *

T = TypeVar('T')
Iter = TypeVar('Iter', bound=Iterable)


def map_same_type(func: Callable[[T], T], iterable: Iter) -> Iterable[T]:
    """Maps a function over an iterable and returns the same collection type."""
    # type() identifies the collection (list, tuple, etc.) and passes the iterator
    return type(iterable)(map(func, iterable))


def create(t: Type, *args) -> Any:
    return t(*args)


from Organizing.TermCounterInDocument import TermCounterInDocument

print(create(int, "33"))

# Examples
print(map_same_type(lambda x: x + x, [1, 2, 3]))
print(map_same_type(lambda x: x + x, (1, 2, 3)))
print(map_same_type(lambda x: x + x, {1, 2, 3}))
