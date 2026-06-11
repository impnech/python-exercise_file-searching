from ITerm import *


class StringTerm(ITerm):
    """
    SOLID-Warning: Should be just generic type, with Generic, but it will not be noticed anywhere except in the factory, so deal with it later
    """

    def __init__(self, val: str):
        if not isinstance(val, str):
            raise ValueError(f"val (the value of {ITerm.__name__}) should be a string")
        # if not val: raise ValueError("val should not be empty")
        self.val: str = val

    def __hash__(self) -> int:
        return hash(self.val)
