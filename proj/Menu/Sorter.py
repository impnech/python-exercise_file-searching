from typing import Iterable, Callable

from Menu.GetNBest import GetNBest

class Sorter(GetNBest):
    @classmethod
    def get_n_best(cls, n: int, sortable, key: Callable = None) -> Iterable:
        super().get_n_best(n, sortable)
        return sorted(sortable, key=key, reverse=True)[:n]
