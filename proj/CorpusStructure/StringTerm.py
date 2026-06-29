from CorpusStructure.ITerm import *


class StringTerm(ITerm):
    """
    SOLID-Warning: Should be just generic type, with Generic, but it will not be noticed anywhere except in the factory, so deal with it later.
    also, it's just one implementation, it's allowed to be bound to some specific
    """

    def __init__(self, val: str):
        if not isinstance(val, str | StringTerm):
            raise ValueError(f"val (the value of {StringTerm.__name__}) should be a string")
        # if not val: raise ValueError("val should not be empty")
        self._val: str = str(val)

    def __hash__(self) -> int:
        return hash(self._val)

    def __eq__(self, other: 'StringTerm'):
        if not isinstance(other, StringTerm | str):
            return False
        return self._val == str(other)

    def __str__(self):
        return self._val

    def __getattr__(self, item):
        return self._val.__getattribute__(item)


