from abc import ABC, abstractmethod


class ITerm(ABC):
    @abstractmethod
    def __hash__(self) -> int:
        pass


class TermString(ITerm):
    def __init__(self, val: str):
        if not isinstance(val, str): raise ValueError("val should be a string")
        # if not val: raise ValueError("val should not be empty")
        self.val: str = val

    def __hash__(self) -> int:
        return hash(self.val)
