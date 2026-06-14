from NumericTermInfoInDocument import *


class TermCounterInDocument(NumericTermInfoInDocument):
    _count: int

    def __init__(self, val: int = 0):
        self._count = val

    def __int__(self):
        return self._count

    def __hash__(self) -> int:
        return hash(self._count)
