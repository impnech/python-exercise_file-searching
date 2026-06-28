from abc import abstractmethod
from typing import *
class GetNBest:
    @classmethod
    @abstractmethod
    def get_n_best(cls, n: int, sortable, key: Callable = None) -> Iterable:
        if n > len(sortable): raise ValueError(f"{n=} represents how many top-results, but the list doesn't have that many.")
        pass

    @classmethod
    def gen_n_best_with_score(cls, n:int, sortable, key: Callable = None)->Iterable:
        return cls.get_n_best(n,[(x, key(x)) for x in sortable], key=lambda p: p[1])


