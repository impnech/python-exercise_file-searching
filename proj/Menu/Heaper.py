from typing import Iterable, Callable

from Menu.GetNBest import GetNBest
import heapq

class Heaper(GetNBest):
    # generally it's better to use heap, for O(n) time instead of O(n*log(n)) of sorting.
    # the extraction of the k first will take k*log(n) and it's reasonable to assume k is small (3 in our case, unlike n, which is a whole 4),
    # so the whole operation is O(k)
    # (but i'm not going to vouch for python implementation efficiency, sorted() was optimized to death)
    @classmethod
    def get_n_best(cls, n: int, sortable: Iterable, key: Callable = None) -> Iterable:
        super().get_n_best(n,sortable)
        li = heapq.nlargest(n, sortable, key)
        return li

if __name__ == '__main__':
    li = [4,2,5,13,65,3,32,5,2,1,3,2,]
    best = Heaper.get_n_best(5,li)
    print(best)