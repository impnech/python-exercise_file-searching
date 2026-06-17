from OldOrganizing.NumericTermInfoInDocument import *
from collections import defaultdict


class TermCounterInDocument(NumericTermInfoInDocument):
    """
    The type of information about a term in some document, which just says how many times the term appears there.
    Some would say that it's completely redundant and can be replaced with int+documentation.
    But, the idea is, even if python doesn't enforce or even warns about it, that I_InverseIndex, should hold a subclass of TermInfoInDocument
    """

    def __init__(self, val: int = 0):
        self._count: int = val

    def __int__(self):
        return self._count

    def __hash__(self) -> int:
        return hash(self._count)

    def __str__(self) -> str:
        return str(self._count)

    def __add__(self, other):
        try:
            other_int: int = int(other)
        except TypeError:
            # TODO logger.error
            raise TypeError(f"cant' convert {other} of type {type(other)} to int in order to add it to int.")
        return TermCounterInDocument(self._count + other_int)
